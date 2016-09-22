#!/usr/bin/python
# coding=utf-8
__author__ = 'xuchu'
import os
import time
import android_autotest.android_appium_base_def as abd
wd = abd.wd
success = abd.success

#GO
try:
    print wd.get_window_size()              #dict
    x = wd.get_window_size()['width']       #int
    y = wd.get_window_size()['height']      #int
    abd.waitForDisplayed("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]")
    for i in (range(4)):
        print i+1
        time.sleep(1)
        abd.swipe_start()
    #点击立即体验
    abd.click_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]")
    arealist = wd.find_elements_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.ExpandableListView[1]/android.widget.LinearLayout[2]")
    for i in arealist:
        print i.tag_name
        print i.c
    #点击小区
    abd.click_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.ExpandableListView[1]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]")
    abd.click_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.ImageView[1]")
    abd.sendkeys_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.EditText[1]","18500008888")
    abd.click_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.Button[1]")
    abd.sendkeys_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]","000000")
    abd.click_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.Button[1]")

    #我的钱包
    abd.click_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.RelativeLayout[2]")
    time.sleep(2)
    #滑动手势密码
    act = abd.TouchAction(wd).press(x=530, y=700).wait(300).move_to(x=0, y=300).wait(300).move_to(x=0, y=300).wait(300).move_to(x=300,y=0).wait(300).release()
    act.perform()

    #检查余额
    myMoney = wd.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]").text
    print myMoney



finally:
    # wd.quit()
    pass
if not success:
    raise Exception("Test failed.")