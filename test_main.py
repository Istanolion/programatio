import unittest #unit testing lib from python
import main #my code to test

class Testfunctions(unittest.TestCase):
    def testParenthesis(self):
        self.assertTrue(main.validParentheses("()"))
        self.assertFalse(main.validParentheses(")(()))"))
        self.assertFalse(main.validParentheses("("))
        self.assertTrue(main.validParentheses("(())((()())())"))

        self.assertFalse(main.validParentheses(")("))
        self.assertFalse(main.validParentheses("(()()))("))

    def testTime(self):
        self.assertEqual('1 minute and 2 seconds',main.formatDuration(62))
        self.assertEqual('1 hour, 1 minute and 2 seconds',main.formatDuration(3_662))
        self.assertEqual('now', main.formatDuration(0))

        self.assertEqual('1 year and 1 second', main.formatDuration(31_536_001))
        self.assertEqual('1 year, 25 days, 6 hours, 5 minutes and 3 seconds', main.formatDuration(33_717_903))

    def testCinema(self):
        self.assertEqual(43,main.cinema(500,15,0.9))
        self.assertEqual(24, main.cinema(100,10,0.95))

        self.assertEqual(2,main.cinema(0,10,0.95))


if __name__ == '__main__':
    unittest.main()
