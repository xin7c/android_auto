#!/usr/bin/python
# coding=utf-8
__author__ = 'xuchu'
import os
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.multi_action import MultiAction

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'a2643548'
desired_caps['app'] = os.path.abspath(
    '/Users/xuchu/mycode/mypy/LeHome/Lehome_if_test/android_appium_autotest/android_autotest/beta_apk_yellow/lehome-dev_0.8.0-968-5597cbe-beta-qa.apk')
# desired_caps['appPackage'] = 'org.athrun.android.app'
desired_caps['waitForAppScript'] = '$.delay(2000); $.acceptAlert();'
wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False
def alert_accept():
    wd.switch_to_alert().accept()
    print '捕获弹出框并点击OK'
def swipe_start():
    '''欢迎页滑动'''
    wd.swipe(900, 800, 200, 800, 400)

def scorll_r_l():
    wd.swipe(900, 800, 200, 800, 400)

def click_by_xpath(xpath):
    wd.find_element_by_xpath(xpath).click()

def sendkeys_by_xpath(xpath,keys):
    wd.find_element_by_xpath(xpath).send_keys(keys)

def waitForDisplayed(xpath):
    '''等待元素出现'''
    return WebDriverWait(wd, 30, 1, (ElementNotVisibleException)).until(lambda x: x.find_element_by_xpath(xpath).is_displayed())

def ddd(seconds):
    time.sleep(seconds)

def getScreenshot():
    wd.get_screenshot_as_png()
    wd.get_screenshot_as_file('hi.jpeg')


#     print wd.get_window_size()
#     element = WebDriverWait(wd, 10).until(lambda x: x.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]"))
#     print element
#     is_disappeared = WebDriverWait(wd, 30, 1, (ElementNotVisibleException)).until(lambda x: x.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").is_displayed())
#     print is_disappeared
