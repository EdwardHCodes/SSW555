"""
The user story:
A complete look at a user's genealogical history.

These tests are to check the function in the python_gedcom_reader file will accurately count the number of lines, content of the file,
"""

import unittest


from python_gedcom_reader import gedcom_file_reader

class TestGedcomReader(unittest.TestCase):
    def test_order(self):
        self.assertEqual(gedcom_file_reader(gedcom_file_reader), )
    def test_length(self):
        self.assertEqual(gedcom_file_reader(gedcom_file_reader), 36) 
    def test_output_format(self):
        ##Checks the first line of the gedcom file
        self.assertEqual(gedcom_file_reader(gedcom_file_reader), "<--|NOTE|0|")
    def test_length_of_gedcom_file(self):
        self.assertEqual(gedcom_file_reader(gedcom_file_reader), "<--|INDI|1|")
    def test_length_of_gedcom_file(self):
        self.assertEqual(gedcom_file_reader(gedcom_file_reader), 36)
    
if __name__ == "__main__":
    unittest.main()
    print('Running unit tests')
