import os
import argparse

from dblp_parser import parse_record
from parseJSON import parseJSON


#We basically parse the XML file and save it as a JSON file
if __name__ == "__main__":
    pparser = argparse.ArgumentParser()
    pparser.add_argument('--dblp', required=True, help='DBLP file')
    pparser.add_argument('--output', required=True, help='Output file')
    args = pparser.parse_args()
    if not os.path.exists(args.dblp):
        raise FileNotFoundError('{} does\' exist.'.format(args.dblp))
    parse_record(args.dblp, args.output)

#We now parse the JSON file to extract the titles and create the positional indexes.
parseJSON()
