"""
The user story:
A complete look at a user's genealogical history.

These tests are to check the function in the python_gedcom_reader file will accurately count the number of lines, 
"""

import unittest


from python_gedcom_reader import gedcom_file_reader

class TestGedcomReader(unittest.TestCase):
    def test_order(self):
        self.assertEqual(gedcom_file_reader(gedcom_file_reader), )
    def test_keywords(self):
        self.assertEqual(gedcom_file_reader(gedcom_file_reader), 36) 
    
    




if __name__ == "__main__":
    unittest.main()
    print('Running unit tests')
