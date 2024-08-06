#!/usr/bin/env python3

import sys
import argparse
import os
import csv
import re

#This script will accept a srv file path and use regex to change the srv file
# data then create a srv output file.
#This script should be run on a command line (windows). 
# Ideally it should accept 2 command line arguments the path to the srv input file
# and the regex you need to change the file to how you want.

print("This is changeCsvFileScript!")

def get_input(): 
  """
  This gets the input from the user via arguments on the command line. The first argument
  is the the csv file path-the csv file to be changed. The next argument is the regular
  expression to be used to manipulate the file. A new csv file will be created in order to
  not overwrite the existing one. Make that you know what the crv file is you are editing to
  give the correct regular expressions. 
  """
  parser = argparse.ArgumentParser(description="Accepts a CRV path with file name as first argument and a regular expression pattern for the second.")
  parser.add_argument("csv_file_path", help="Path to the CSV file to be modified")
  parser.add_argument("old_regular_expression_pattern", help="Old regular expression to be replaced")
  parser.add_argument("new_regular_expression_pattern", help="New regular expression pattern to replace the old one")
  args = parser.parse_args()
  
  return args.csv_file_path.strip(), args.old_regular_expression_pattern.strip(), args.new_regular_expression_pattern.strip()
 

  #print("Number of args passed:", number_of_args)
  #print("The filePath is: ", file_path)
  #print("The regular expression is: ", regex)
  
 
def handle_csv_file(file_path, regex_old, regex_new):
  """
  The function will take in the file_path and regex from the get_input function.
  get_input() will return the values into global variables. This function will
  open the file path to the csv file, read it and store the data into placeholder lists.
  <more on this later>
  """
  try: 
    #opens and reads the crv file using the user inputted path
    with open(file_path, "r") as file:
      read_input_file = csv.reader(file)
      updated_rows = []
      #regex_new = "r" + regex_new 
      #regex_old = "r" + regex_old
      for row in read_input_file:
        
        #uses sub regex function for user inputted regular expressions
        updated_row = [re.sub(regex_old, regex_new, item) for item in row]
        updated_rows.append(updated_row)
        print(updated_row)
        #replaces the updated file name
    new_file_path = file_path.replace(".csv", "_updated.csv")
    # writes to the updated new "updated" crv file 
    with open(new_file_path, "w", newline="") as file:
      writer = csv.writer(file)
      writer.writerows(updated_rows)
      print(f"Regular expressions replaced successfully. The modified file is saved as {new_file_path}")
  except FileNotFoundError:
    print(f"Error. The file {file_path} does not exist!")  
  except Exception as e:
    print(f"Error: {e}")  
  
  
  #print("From function File Path: " + file_path)
  #print("From function New Regex: " + regex_old)
  #print("From function old Regex: " + regex_new)
  
  #this is the main function used to execute all the functions in order
if __name__ == "__main__":
  if len(sys.argv) != 4:
    sys.exit("ERROR: There must be 3 command-line parameters. The CSV file path, the old regular expression pattern, and last, the new regular expression pattern!")
    
  file_path, regex_old, regex_new = get_input()
  handle_csv_file(file_path, regex_old, regex_new) 








  
  
  
  
  