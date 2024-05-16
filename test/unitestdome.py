import unittest
def setUpModule():
    print("===setUpModule===")
def tearDownModule():
    print("===tearDownModule===")
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        print("setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")
    def setUp(self) :
        print("setUp")
    def tearDown(self):
        print("tearDown")
    def test_01(self):
        print('test01')
        # 完全相等
        self.assertEqual(True, True)
    def test_02(self):
        print('test02')
#     包含a包含b中
        self.assertIn('w','why')

    def test_03(self):
        print('test03')
    #     判断他们的内存地址是否是一样的
        self.assertIsNot(1,1/1)
    def test_04(self):
        print('test04')
        # 比大小 小于
        self.assertLess(3,4)
    def test_05(self):
        print('test05')
        # 类型的判断
        # self.assertIsInstance([1,2],list)
        self.assertIsInstance({"us":"s2","ps":123456}, dict)

if __name__ == '__main__':
    unittest.main()
