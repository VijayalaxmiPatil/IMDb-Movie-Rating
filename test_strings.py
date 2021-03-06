import sys
import pip

if not "xmlrunner" in sys.modules:
	pip.main(["install", "xmlrunner"])

if not "unittest" in sys.modules:
    pip.main(["install", "unittest"])

if not "shutil" in sys.modules:
	pip.main(["install", "shutil"])

import xmlrunner
import unittest
import shutil

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'fOO')  #Here FOO is replaced by foo for testing failure
        print("completed test_upper test")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        print("completed test_isupper test")

    def test_split(self):
        s = 'hello world d'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
       
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
	#shutil.rmtree('./test-reports')
