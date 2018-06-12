import unittest2 as unittest
from ipynb.fs.full.index import load_data

class TestPlotly(unittest.TestCase):
    def test_load_data_is_one_hundred_twenty_two(self):
        self.assertEqual(len(load_data()), 122)


    def test_load_data_is_one_hundred_twenty_two(self):
        self.assertEqual(load_data()[0]), {'foobar': 'baz'})
