import unittest
import pandas as pd
# check if number of rows is 14894
# if not, fail, if yes, true

def row_count():
    file_path = "Armed Forces Data.csv"
    df = pd.read_csv(file_path)
    row_count = len(df)
    expected_row_count = 14893 
    #pandas reads in from -1, 1 less from actual row count.
    return row_count == expected_row_count

#check if number of columns is 5
#if not, fail, if yes, true
def column_count():
    file_path = "Armed Forces Data.csv"
    df = pd.read_csv(file_path)
    column_count = len(df.columns)
    expected_column_count = 5
    return column_count == expected_column_count


class TestFunction(unittest.TestCase):
    def test_row_count(self):
        result = row_count()
        self.assertEqual(result, True)

    def test_column_count(self):
        result = column_count()
        self.assertEqual(result, True)
    

if __name__ == '__main__':
    unittest.main()

