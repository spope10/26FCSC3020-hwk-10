'''
CSC3020 - Software Engineering Fundamentals
Instructor: Thyago Mota
Student: 
Description: Homework 10 - Blackbox Testing
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DivisionTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.browser = webdriver.Chrome()
        self.browser.get('http://127.0.0.1:5000')

    # pre-condition: a=5, b=2
    # post-condition: result is displayed as 2.5
    def testFiveDividedByTwo(self):
        self.browser.find_element(By.NAME, "a").send_keys("5")
        self.browser.find_element(By.NAME, "b").send_keys("2")
        self.browser.find_element(By.NAME, "submit").click()

        result = self.browser.find_element(By.TAG_NAME, "p").text
        self.assertEqual(result, "Result: 2.5")

    # pre-condition: a=-5, b=2
    # post-condition: result is displayed as -2.5
    def testNegativeFiveDividedByTwo(self):
        raise ValueError()

    # pre-condition: a=-5, b=-2
    # post-condition: result is displayed as 2.5
    def testNegativeFiveDividedByNegativeTwo(self):
        raise ValueError()
            
    # pre-condition: a=1, b=3
    # post-condition: result is displayed as 0.33
    def testOneDividedByThree(self):
        raise ValueError()

    # pre-condition: a=5, b=0
    # post-condition: message "Denominator cannot be zero" is displayed
    def testFiveDividedByZero(self):
        raise ValueError()

if __name__ == '__main__':
    unittest.main()
