import os, sys
p = os.path.abspath('..')
sys.path.insert(1, p)
import unittest
from translator import english_to_french, french_to_english

class frenchToEnglish(unittest.TestCase): 
    def test1(self):
        self.assertNotEqual(english_to_french("Hello").get("translations")[0].get("translation"), "Hello") 
        self.assertEqual(english_to_french("Hello").get("translations")[0].get("translation"), "Bonjour")


class englishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertNotEqual(french_to_english("Bonjour").get("translations")[0].get("translation"), "Bonjour")  
        self.assertEqual(french_to_english("Bonjour").get("translations")[0].get("translation"), "Hello") 

unittest.main()