#import all needed modules here
import unittest
from app import interpret_score


#write all your tests below this line


#write your test suite here, in the main() function
def main():
    #call all your tets here, one on each line
    print("Starting tests suite...")

class TestInterpretScore(unittest.TestCase):
    def test_interpret_score(self):
        self.assertEqual(interpret_score(5), "Low")
        self.assertEqual(interpret_score(6), "Moderate")
        self.assertEqual(interpret_score(7), "Moderate")
        self.assertEqual(interpret_score(11), "Moderate")
        self.assertEqual(interpret_score(12), "High")
        self.assertEqual(interpret_score(13), "High")

#please do not change the lines below
if __name__ == "__main__":
    unittest.main()
