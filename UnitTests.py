import unittest
import pandas as pd
# check if number of rows is 1876
# if not, fail, if yes, true


class TestFunction(unittest.TestCase):
    def test_row_count(self):
        file_path = "Births outside of marriage.csv"
        df = pd.read_csv(file_path)
        row_count = len(df)
        expected_row_count = 1877
    

if __name__ == '__main__':
    unittest.main()
