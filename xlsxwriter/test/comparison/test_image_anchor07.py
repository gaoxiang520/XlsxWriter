###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013-2014, John McNamara, jmcnamara@cpan.org
#

import unittest
import os
from ...workbook import Workbook
from ..helperfunctions import _compare_xlsx_files


class TestCompareXLSXFiles(unittest.TestCase):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):
        self.maxDiff = None

        filename = 'image_anchor07.xlsx'

        test_dir = 'xlsxwriter/test/comparison/'
        self.image_dir = test_dir + 'images/'
        self.got_filename = test_dir + '_test_' + filename
        self.exp_filename = test_dir + 'xlsx_files/' + filename

        self.ignore_files = []
        self.ignore_elements = {}

    def test_create_file(self):
        """Test the creation of a simple XlsxWriter file with image(s)."""
        filename = self.got_filename

        ####################################################

        workbook = Workbook(filename)

        worksheet = workbook.add_worksheet()

        worksheet.insert_image('A1', self.image_dir + 'blue.png')
        worksheet.insert_image(
            'B3', self.image_dir + 'red.jpg', {'positioning': 3})
        worksheet.insert_image(
            'D5', self.image_dir + 'yellow.jpg', {'positioning': 2})
        worksheet.insert_image(
            'F9', self.image_dir + 'grey.png', {'positioning': 1})

        workbook.close()

        ####################################################

        got, exp = _compare_xlsx_files(self.got_filename,
                                       self.exp_filename,
                                       self.ignore_files,
                                       self.ignore_elements)

        self.assertEqual(got, exp)

    def tearDown(self):
        # Cleanup.
        if os.path.exists(self.got_filename):
            os.remove(self.got_filename)


if __name__ == '__main__':
    unittest.main()
