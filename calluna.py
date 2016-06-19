#!/usr/bin/env python
# coding=utf-8
#
# Imports Rundata file data into Postgres DB
# Copyright (C) 2016  Victor Rådmark
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# Updated: 2016-06-18

import json, argparse, configparser, pg8000, xlrd

config = configparser.ConfigParser()
config.read('calluna.ini')

# read xls info file and insert into db
def read_info(xls):
    sheet = xlrd.open_workbook(xls).sheet_by_index(0)
    conn = pg8000.connect(host=config['db']['host'], database=config['db']['name'], user=config['db']['user'], password=config['db']['password'])
    cursor = conn.cursor()
    
    num_cols = sheet.ncols   # Number of columns
    col_data = []
    for row_idx in range(0, sheet.nrows):    # Iterate through rows
        #print('-'*40)
        #print('Row: %s' % row_idx)   # Print row number
        #for col_idx in range(0, num_cols):  # Iterate through columns
        for col_idx in range(0, 2):  # Iterate through columns
            cell_obj = sheet.cell(row_idx, col_idx)  # Get cell object by row, col
            #print('Column: [%s] cell_obj: [%s]' % (0, cell_obj.value))
            col_data.append(cell_obj.value)
        cursor.execute(
             "INSERT INTO rune_info (sign, place) VALUES (%s, %s)",
             (col_data[0], col_data[1]))
        del col_data[:]

    conn.commit()

    #with open('test.txt', 'w') as outfile:
    #	json.dump(data, outfile)
    
    #str_data = json.dumps(data).encode("utf-8")

def main():
    parser = argparse.ArgumentParser(description='Imports Rundata file data into Postgres DB.')
    parser.add_argument('--dir', help='the directory containing the Rundata files')
    
    args = parser.parse_args()
    
    if args.dir:
        dir_str = args.dir
    else:
        dir_str = config['calluna']['dir']

    read_info(dir_str + "/RUNDATA.xls")

    #with open(example + "/FORNSPR", 'r') as f: 
    #	read_east_norse(f)

if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    print("Ctrl-C during program execution.")