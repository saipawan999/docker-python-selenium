import json
import time
import unittest
import os
import urllib
from random import randint

import urllib3
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


class HackerNewsSearchTest(unittest.TestCase):


    def setUp(self):

        # randomint = 'Downloads_'+str(randint(111, 9999999999))
        # folder = r'D:/MapFolderForDocker/'+randomint
        # while(True):
        #     if(os.path.isdir(folder)):
        #         folder = folder+"1"
        #     else:
        #         os.mkdir(folder)
        #         break;

        fp=webdriver.FirefoxProfile()
        # fp.set_preference("browser.download.folderList",2)
        # fp.set_preference("browser.download.manager.showWhenStarting",False)
        # fp.set_preference("browser.download.dir",r'/home/seluser/'+randomint)
        # fp.set_preference("browser.helperApps.neverAsk.saveToDisk","octet/stream,text/csv;charset=utf-8;,"
        #                                                            "application/zip, application/octet-stream");
        opts=Options()
        opts.profile=fp
        capabilities=DesiredCapabilities.FIREFOX.copy()
        capabilities.update(opts.to_capabilities())
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=capabilities)
        self.browser.implicitly_wait(1000)


    def test_hackernews_search_for_testdriven1(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)

    def test_hackernews_search_for_testdriven2(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)

    def test_hackernews_search_for_testdriven3(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)

    def test_hackernews_search_for_testdriven4(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)

    def test_hackernews_search_for_testdriven5(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)
    def test_hackernews_search_for_testdriven6(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)
    def test_hackernews_search_for_testdriven7(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)
    def test_hackernews_search_for_testdriven8(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)
    def test_hackernews_search_for_testdriven9(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)
    def test_hackernews_search_for_testdriven10(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)
    def test_hackernews_search_for_testdriven11(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)
    def test_hackernews_search_for_testdriven12(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)

    def test_hackernews_search_for_testdriven13(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)

    def test_hackernews_search_for_testdriven14(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)

    def test_hackernews_search_for_testdriven15(self):

        browser = self.browser
        browser.get('https://news.ycombinator.com')

        search_box = browser.find_element_by_name('q')
        search_box.send_keys('testdriven')
        search_box.send_keys(Keys.RETURN)
          # simulate long running test
        time.sleep(3)
        print(browser.current_url)
        self.assertIn('testdriven', browser.page_source)


    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')