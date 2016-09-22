#!/usr/bin/python
# coding=utf-8
__author__ = 'xuchu'
import os
import time
import json
from appium import webdriver
from LeHome.Lehome_if_test.android_appium_autotest.android_0_7_0.getVcode import getVcode
import LeHome.Lehome_if_test.android_appium_autotest.android_autotest.android_appium_base_def as abd
from selenium.common.exceptions import ElementNotVisibleException
from appium.webdriver.common.touch_action import TouchAction


wd = abd.wd
success = abd.success
wd.implicitly_wait(20)
getVcode = getVcode()#实例化验证码类

#GO
try:
    print abd.wd.get_window_size()              #dict
    x = abd.wd.get_window_size()['width']       #int
    y = abd.wd.get_window_size()['height']      #int
    abd.waitForDisplayed("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]")
    #欢迎导图
    for i in range(4):
        abd.ddd(1)
        abd.scorll_r_l()
        print "滑动第[%d]次" %(i+1)
    if abd.waitForDisplayed("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"):
        print "立即体验按钮出现鸟--------OK"
        print("点击立即体验->")
    else:
        #只是一个无聊的防滑机制
        print "再滑一次哦"
        abd.scorll_r_l()
    abd.click_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]")
    abd.ddd(3)
    areaName = abd.wd.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.ExpandableListView[1]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.TextView[1]").text.encode("utf-8")
    print("点击小区定位[%s]->") %str(areaName)
    abd.click_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.ExpandableListView[1]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]/android.widget.TextView[1]")
    abd.ddd(3)
    #登陆
    abd.login()
    #点击钱包
    abd.click_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.ImageButton[1]")
    abd.ddd(1)
    print abd.psw.__doc__
    abd.psw()

finally:
    # wd.quit()
    # wd.close_app()
    print "之前的操作都没报错，恭喜你英雄，反正有错也会打印这句话的。"
    if not success:
        raise Exception("Test failed.")