#!/usr/bin/env python
# coding=utf-8
#
# Imports Rundata file data into PGSQL DB
# By Victor Rådmark
# Updated: 2016-05-15

import json, argparse
from pyexcel_xls import get_data

def read_info(xls_filename):
    data = get_data(xls_filename)

    with open('test.txt', 'w') as outfile:
    	json.dump(data, outfile)

def main():
    parser = argparse.ArgumentParser(description='Import Rundata file data into PGSQL DB.')
    parser.add_argument('dir', help='the directory containing the Rundata files')
    
    args = parser.parse_args()
    
    dir_str = args.dir

    read_info(dir_str + "/RUNDATA.xls")

    #with open(example + "/FORNSPR", 'r') as f: 
    #	read_east_norse(f)

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("Ctrl-C during program execution.")