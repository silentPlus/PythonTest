import unittest
import check


class MyTestCase(unittest.TestCase):
    def test_regular(self):
        rv = check.password('qwertyu')
        self.assertTrue(repr(rv) == 'simple')
        self.assertTrue('规则' in rv.message)

    def test_step(self):
        rv = check.password('abcdefg')
        self.assertTrue(repr(rv) == 'simple')
        self.assertTrue('规则' in rv.message)

    def test_common(self):
        rv = check.password('password')
        self.assertTrue(repr(rv) == 'simple')
        self.assertTrue('常见' in rv.message)

    def test_medium(self):
        rv = check.password('tdnwh01')
        self.assertTrue(repr(rv) == 'medium')
        self.assertTrue('不够强' in rv.message)

    def test_strong(self):
        rv = check.password('tdnWwh01')
        self.assertTrue(repr(rv) == 'strong')
        self.assertTrue('完美' in rv.message)

    def test_email(self):
        rv = check.email('123@qq.com')
        self.assertEqual(rv.isValiEmail(), True)

    def test_emailType(self):
        rv = check.email('123@qq.com')
        type = 'qq' or '163' or 'gmail' or '126' or 'sina'
        self.assertEqual(rv.isValiType(), type)
if __name__ == '__main__':
    unittest.main()
