from HTMLTestRunner import HTMLTestRunner
import unittest,time
#123
test_dir = 'D:\\yunke_2018\\mail\\test_case'
test_report = 'D:\\yunke_2018\\mail\\report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern = '*_case.py')

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description="运行环境：windows 7, Chrome")
    runner.run(discover)
    fp.close()