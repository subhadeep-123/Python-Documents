import unittest
import main


class Testing(unittest.TestCase):
    def test_do_stuff1(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = -10
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, Exception)

    def test_do_stuff3(self):
        test_param = 'string'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, Exception)

    def test_do_stuff4(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, Exception)

    def test_do_stuff5(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, Exception)


if __name__ == '__main__':
    unittest.main()
