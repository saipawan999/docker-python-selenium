# import json
# import time
# import unittest
# import os
# import urllib
# from random import randint
#
# import urllib3
# from selenium import webdriver
# from selenium.webdriver import DesiredCapabilities
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# class HackerNewsSearchTest(unittest.TestCase):
#
#
#     def setUp(self):
#
#         randomint = 'Downloads_'+str(randint(111, 9999999999))
#         folder = r'D:/MapFolderForDocker/'+randomint
#         while(True):
#             if(os.path.isdir(folder)):
#                 folder = folder+"1"
#             else:
#                 os.mkdir(folder)
#                 break;
#
#         options = webdriver.ChromeOptions()
#         prefs = {'download.default_directory': r'/home/seluser/'+randomint}
#         options.add_experimental_option('prefs', prefs)
#         capabilities = DesiredCapabilities.CHROME.copy()
#         capabilities.update(options.to_capabilities())
#         self.browser = webdriver.Remote(
#             command_executor='http://localhost:4444/wd/hub',
#             desired_capabilities=capabilities)
#         self.browser.implicitly_wait(50)
#
#     def test_hackernews_search_for_selenium1(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def test_hackernews_search_for_selenium2(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def test_hackernews_search_for_selenium3(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def test_hackernews_search_for_selenium4(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def test_hackernews_search_for_selenium5(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def test_hackernews_search_for_selenium6(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def test_hackernews_search_for_selenium7(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def test_hackernews_search_for_selenium8(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def test_hackernews_search_for_selenium9(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def test_hackernews_search_for_selenium10(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def test_hackernews_search_for_selenium11(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def test_hackernews_search_for_selenium12(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def test_hackernews_search_for_selenium13(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def test_hackernews_search_for_selenium14(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def test_hackernews_search_for_selenium15(self):
#
#         browser = self.browser
#         browser.get('https://chromedriver.storage.googleapis.com/81.0.4044.20/chromedriver_win32.zip')
#         #time.sleep(10)
#
#     def tearDown(self):
#         self.browser.close()
#         self.browser.quit()
#
# if __name__ == '__main__':
#     unittest.main(warnings='ignore')