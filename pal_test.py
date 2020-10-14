  
import unittest
from pal import add
# import palindromeCheck

class MyTest(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(add(5,7), 12)
        #self.assertEqual(add(5,7), 15)
        
if __name__ == '__main__':
    unittest.main()
