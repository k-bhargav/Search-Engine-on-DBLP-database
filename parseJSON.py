# importing libraries
#import numpy as np
import os
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
#from natsort import natsorted
import string
import json

def preprocessing(final_string):
	# Tokenize.
	tokenizer = TweetTokenizer()
	token_list = tokenizer.tokenize(final_string)

	# Remove punctuations.
	table = str.maketrans('', '', '\t')
	token_list = [word.translate(table) for word in token_list]
	punctuations = (string.punctuation).replace("'", "")
	trans_table = str.maketrans('', '', punctuations)
	stripped_words = [word.translate(trans_table) for word in token_list]
	token_list = [str for str in stripped_words if str]

	# Change to lowercase.
	token_list =[word.lower() for word in token_list]
	return token_list

# Initialize the stemmer.
stemmer = PorterStemmer()

# Initialize the file no.
fileno = 0

# Initialize the dictionary.
pos_index = {}

# Initialize the file mapping (fileno -> file name).
file_map = {}



def json_parser(filename):
    with open(filename) as json_file:
        data = json.load(json_file)

    for fileno in range(50000):
        #We take each and every title and add it to the positional index.
        text = data[fileno]["title"]
        #print(text)
        if text is not None:
            final_token_list = preprocessing(text)
            
        
        """ if text is not None:
            final_token_list = text.split(" ") """
        
        #For position and term in the tokens
        for pos, term in enumerate(final_token_list):
            # First stem the term.
            term = stemmer.stem(term)

            # If term already exists in the positional index dictionary.
            if term in pos_index:
                # Increment total freq by 1.
                pos_index[term][0] = pos_index[term][0] + 1

                # Check if the term has existed in that DocID before.
                if fileno in pos_index[term][1]:
                    pos_index[term][1][fileno].append(pos)
                else:
                    pos_index[term][1][fileno] = [pos]
            
            # If term does not exist in the positional index dictionary
            # (first encounter).
            else:
                # Initialize the list
                pos_index[term] = []
                # The total frequency is 1
                pos_index[term].append(1)
                # The postings list is initially empty.
                pos_index[term].append({})
                # Add doc ID to postings list.
                pos_index[term][1][fileno] = [pos]

def parseJSON():
    json_parser(os.getcwd() + "\output.json")

    with open(os.getcwd() + '\posIndex.json' , 'w') as file1:
        file1.write(json.dumps(pos_index))







    



        

        
            



