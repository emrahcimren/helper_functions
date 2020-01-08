import unittest
import mock
from helpers import all_files_in_directory


class TestAllFileInDirectory(unittest.TestCase):

    @mock.patch('app.os.listdir')
    def test_all_files_in)directory(self, mock_listdir):
        mock_listdir.return_value = ['2017-02-18.RDS.csv', '2017-02-25.RDS.csv', '2017-02-11.RDS.csv']
        files = all_files_in_directory('.')
        #self.assertEqual(3, len(files))
        print(files)

if __name__ == '__main__':
    unittest.main()