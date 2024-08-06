import unittest
from change_csv import get_input, handle_csv_file
import os
import csv
from io import StringIO
import unittest.mock

class TestInputs(unittest.TestCase):
  
  def setUp(self):
    # Create a sample CSV file for testing
    self.test_file_path = "test_file.csv"
    with open(self.test_file_path, "w", newline='') as file:
      writer = csv.writer(file)
      writer.writerow(["name", "age", "email"])
      writer.writerow(["Sawyer", "30", "sawyer.doe@example.com"])
      writer.writerow(["Jane Smith", "25", "jane.smith@example.com"])
      
  def tearDown(self):
    # Remove the sample CSV file and the modified file after tests
    if os.path.exists(self.test_file_path):
      os.remove(self.test_file_path)
    modified_file_path = self.test_file_path.replace(".csv", "_modified.csv")
    if os.path.exists(modified_file_path):
      os.remove(modified_file_path)
      
  def test_handle_csv_file(self):
    # Test the handle_csv_file function
    regex_old = "Sawyer"
    regex_new = "FUCKOFF!!!"
    handle_csv_file(self.test_file_path, regex_old, regex_new)
    
    modified_file_path = self.test_file_path.replace(".csv", "_updated.csv")
    self.assertTrue(os.path.exists(modified_file_path))
    
    with open(modified_file_path, "r") as file:
      reader = csv.reader(file)
      rows = list(reader)
      self.assertEqual(rows[1][0], "FUCKOFF!!!")
  def test_get_input(self):
    # Test the get_input function
    test_args = ["change_csv.py", "test_file.csv", "John Doe", "Jonathan Doe"]
    with unittest.mock.patch('sys.argv', test_args):
      file_path, regex_old, regex_new = get_input()
      self.assertEqual(file_path, "test_file.csv")
      self.assertEqual(regex_old, "John Doe")
      self.assertEqual(regex_new, "Jonathan Doe")

if __name__ == "__main__":
  unittest.main()
