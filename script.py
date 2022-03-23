#! usr/bin/python3

""" The following two will provide the name of the script and
the file name being ran on as well as their paths """

import sys # for command arguments (files used)
import os # for paths

print('\nThe script being ran is named as ' + sys.argv[0] + ' located in ' + os.path.dirname(os.path.abspath(__file__)) + '\n')

print('The input file is ' + sys.argv[1] + ' located in ' + os.path.dirname(os.path.abspath(__file__)) + '\n')

""" for searching regex pattern involving
any word containing inherit* """


""" opening required files and writing out new file with search results """

if __name__ == "__main__":

   print('\nOpening origin.txt')
   with open('origin.txt', 'r') as in_stream:
      print('\nOpening inherit.txt\n')
      with open('inherit.txt', 'w') as out_stream:
        def main():
           for (line_num, line) in enumerate(in_stream):
             line = line.strip()
             words_list = line.split()
             import re
             words_list.sort()
             for word in words_list:
                if re.match("inherit[^,.;-]+$", word, flags=re.I): # re.I == re.IGNORECASE
                     print(word)
                     out_stream.write('%d\t%s\n' % (line_num, word))  # Tab delimited outstream of the line number and the word searched with regex

        main()

print("\nDone!")
print('\norigin.txt is closed?', in_stream.closed)
print('\ninherit.txt is closed?', out_stream.closed) 
print('\nYayyyyyyy. Now, open inherit.txt to see results. \n')

