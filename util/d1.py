# -*-coding:utf-8 -*-
# __author__ = 'xiaoxi'
# @time:2019/1/16 16:55
import unittest,HTMLTestRunner
class d1(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        a=2
        b=3
        self.assertEqual(a,b,msg=u"c")

    def tearDown(self):
        pass

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(d1('test1'))
    html_file = '../report/result.html'
    fp = file(html_file, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="吴洪彬_测试报告",
        description="金惠家ui自动化"
    )
    runner.run(suite)
    fp.close()