#!/usr/bin/python
#
# extract_baby_names.py - extract baby names from html files
#
# Author: Maer Melo
#         salalbr@gmail.com

import sys, os, re

def extract(path):
  if os.path.isfile(path):
    f = open(path, 'rU')
    table = {}
    for line in f.readlines():
      year = re.findall(r'Popularity\ in\ (\d+)', line)
      names = re.findall(r'<td>(.+)</td><td>(.+)</td><td>(.+)</td>', line)
      if len(year):
        year_ret = year[0]
      if len(names):
        table[names[0][0]] = [names[0][1], names[0][2]]
    return (year_ret, table)
            
def print_ranking((year_ret, table)):
  print '======== Year: %s ========' % str(year_ret)
  keys = [key for key in table.keys()]
  keys.sort(key=int)
  for key in keys:
    print '#%s: %s, %s' % (str(key), table[key][0], table[key][1])

def main():
  args = sys.argv[1:]
  if not len(args):
    print '===Usage: extract_baby_names.py [<html_file>/<folder]'
  else:
    print_ranking(extract(args[0]))

if __name__ == '__main__':
  main()