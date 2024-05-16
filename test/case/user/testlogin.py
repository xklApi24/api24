import unittest
# from lib import xzslogin
from lib import xzslogin
class MyTestCase(unittest.TestCase):
    xs=xzslogin.login()
    def test_long_01(self):
        t=self.xs.slogin("s2","123456")
        self.assertIn("成功", t.text)
    def test_long_02(self):
        t=self.xs.slogin("s2","")
        self.assertIn("用户名或密码错误", t.text)

if __name__ == '__main__':
    unittest.main()
