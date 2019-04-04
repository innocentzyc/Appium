# coding=gbk
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import Tools

# 加群记录
APPLY_SUCCESS = 0
REQUAIR_INVITE = 0
REQUAIR_VERIFICATION = 0
# 加好友记录
ADD_SUCCESS = 0
ADD_FALURE = 0
# 滑动定义
SWIPE_START_X = 350
SWIPE_START_Y = 1275
SWIPE_DISTANCE = 1100
SWIPE_DURATION_LONG = 3000
SWIPE_DURATION_SHORT = 500
# 点击持续时间
LONG_TAP = 2500
NORMAL_TAP = 200
SHORT_TAP = 50

# 搜索关键词
KEYWORD = "交友"
# 发送的默认消息
MESSAGE = "你好呀 朋友介绍的 交个朋友嘛"
# 发送消息的次数
TIME = 1
# 滑动次数
SWIPE_TIME = 1
# 加群发送的验证消息
GROUP_MESSAGE_FLAG = True
ADD_GRPOUP_MESSAGE = "原来大家都在这呢"
# 加好友默认发送验证信息
FRIEND_MESSAGE_FLAG = True
ADD_FRIEND_MESSAGE = "朋友介绍的 你好呀"





class AddQQ():

  def __init__(self, drive, wait):

    self.driver = drive
    self.wait = wait
    global SWIPE_DISTANCE
    SWIPE_DISTANCE = self.driver.get_window_size()['height']




  def login(self, username, word):
      time.sleep(3)
      # 点击允许
      if Tools.findItem(self.driver, 'id', 'com.android.packageinstaller:id/permission_allow_button'):
          self.wait.until(EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button'))).click()
      time.sleep(0.5)
      if Tools.findItem(self.driver, 'id', 'com.android.packageinstaller:id/permission_allow_button'):
          self.wait.until(EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button'))).click()
      time.sleep(0.5)
      self.driver.wait_activity('.activity.LoginActivity', 60)
      # 点击登录
      self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mobileqq:id/btn_login'))).click()
      time.sleep(1)
      # 输入账号密码
      account = self.wait.until(
          EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@content-desc="请输入QQ号码或手机或邮箱"]')))
      account.set_text(username)
      password = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mobileqq:id/password')))
      password.set_text(word)
      # 点击登录
      login = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mobileqq:id/login')))
      login.click()
      time.sleep(15)

  def find_group(self, keyword = KEYWORD):
      # 点击加号
      self.driver.tap([(666, 95)], NORMAL_TAP)
      time.sleep(1)
      #  点击加好友/群
      self.driver.tap([(545, 299)], NORMAL_TAP)
      self.driver.wait_activity('.activity.contact.addcontact.AddContactsActivity', 20)
      time.sleep(1.5)

      # 点击找群
      self.driver.tap([(361, 191)], NORMAL_TAP)
      time.sleep(1)
      # 允许卫星
      self.driver.tap([(528, 1192)], NORMAL_TAP)
      time.sleep(2)
      # 点击搜索框
      self.driver.tap([(348, 312)], NORMAL_TAP)
      time.sleep(1)

      # 寻找输入框 并且输入
      keyword_text = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mobileqq:id/et_search_keyword')))
      keyword_text.set_text(keyword)
      time.sleep(1)
      # 点击第一行找群
      self.driver.tap([(230, 181)], NORMAL_TAP)
      time.sleep(10)
      i=0
      while i<3:
          self.driver.swipe(SWIPE_START_X, SWIPE_START_Y, SWIPE_START_X, SWIPE_START_Y - SWIPE_DISTANCE,
                            SWIPE_DURATION_SHORT)
          time.sleep(2.5)
          i = i + 1



  def add_group(self, add_message = ADD_GRPOUP_MESSAGE):
      sleep_time = 1.5
      time.sleep(sleep_time)
      i=0
      while i<5:
          # 点击每行
          self.driver.tap([(350, 250+220*i)], 100)
          time.sleep(sleep_time)
          # 判断是否申请加入按钮
          apply = Tools.findItem(self.driver, 'accessibility id', '消息免打扰')
          if apply:
              self.driver.back()
              self.driver.wait_activity('.activity.QQBrowserActivity', 10)
          else:
              # 申请加入
              self.driver.tap([(350, 1215)], NORMAL_TAP)
              time.sleep(2)
              is_edit_text = Tools.findItem(self.driver, 'xpath',
                                                  '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText')
              if is_edit_text == True:
                  global GROUP_MESSAGE_FLAG
                  if GROUP_MESSAGE_FLAG:
                      edit_text = self.driver.find_element_by_xpath(
                          '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText')
                      self.driver.keyevent(123)
                      edit_text.clear()
                      edit_text.set_text(add_message)
                      # GROUP_MESSAGE_FLAG = False
                  self.driver.tap([(658, 95)], NORMAL_TAP)
                  time.sleep(sleep_time)
                  self.driver.tap([(658, 95)], NORMAL_TAP)
                  time.sleep(sleep_time)
                  global APPLY_SUCCESS
                  APPLY_SUCCESS += 1
                  print('申请成功:', APPLY_SUCCESS)
              else:
                  time.sleep(3)
                  # 再次点击避免卡住
                  self.driver.tap([(350, 1215)], NORMAL_TAP)
                  time.sleep(2)
                  if self.driver.current_activity == '.activity.ChatSettingForTroop':
                      self.driver.back()
                      global REQUAIR_INVITE
                      REQUAIR_INVITE += 1
                      print('需要邀请进群:', REQUAIR_INVITE)
                  else:
                      self.driver.back()
                      self.driver.wait_activity('.activity.ChatSettingForTroop', 10)
                      self.driver.back()
                      global REQUAIR_VERIFICATION
                      REQUAIR_VERIFICATION = REQUAIR_VERIFICATION + 1
                      print('需要回答问题:', REQUAIR_VERIFICATION)
          i += 1
      self.swipe_group()






  def into_group(self):
      # 点击置顶群
      first = self.wait.until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.AbsListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout')))
      first.click()
      self.driver.wait_activity('.activity.SplashActivity', 10)
      time.sleep(1)
      # 点击右上角
      right_button = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mobileqq:id/ivTitleBtnRightImage')))
      right_button.click()
      time.sleep(3)
      # 点击群聊成员
      person = self.wait.until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.AbsListView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView[2]')))
      person.click()
      time.sleep(30)
      # 滑动调整位置
      self.driver.swipe(SWIPE_START_X, 230, SWIPE_START_X, 150, SWIPE_DURATION_SHORT)

  def into_group_again(self):
      # 点击置顶群
      if Tools.findItem(self.driver, 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.AbsListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout'):
          first = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.AbsListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout')))
          first.click()
      else:
          time.sleep(10)
          first = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.AbsListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout')))
          first.click()

      self.driver.wait_activity('.activity.SplashActivity', 10)
      time.sleep(1)
      # 点击右上角
      if Tools.findItem(self.driver, 'id', 'com.tencent.mobileqq:id/ivTitleBtnRightImage'):
          right_button = self.wait.until(
              EC.presence_of_element_located((By.ID, 'com.tencent.mobileqq:id/ivTitleBtnRightImage')))
          right_button.click()
      else:
          time.sleep(10)
          right_button = self.wait.until(
              EC.presence_of_element_located((By.ID, 'com.tencent.mobileqq:id/ivTitleBtnRightImage')))
          right_button.click()

      time.sleep(3)
      # 点击群聊成员
      if Tools.findItem(self.driver, 'xpath', '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.AbsListView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView[2]'):
          person = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.AbsListView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView[2]')))
          person.click()
      else:
          time.sleep(10)
          person = self.wait.until(EC.presence_of_element_located((By.XPATH,
                                                                   '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.AbsListView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView[2]')))
          person.click()


      time.sleep(10)
      # 滑动调整位置
      # self.driver.swipe(SWIPE_START_X, 230, SWIPE_START_X, 150, SWIPE_DURATION_SHORT)
      global TIME
      TIME = TIME + 1
      print(TIME)
      if TIME == 7:
          TIME = 0
          global SWIPE_TIME
          SWIPE_TIME = SWIPE_TIME + 1


      self.send_message(TIME)
  # TODO
  def send_message(self, times = 0, message = MESSAGE):
      for i in range(0, SWIPE_TIME):
          self.driver.swipe(SWIPE_START_X, SWIPE_START_Y, SWIPE_START_X, SWIPE_START_Y - SWIPE_DISTANCE,
                            SWIPE_DURATION_LONG)
      sleep_time = 0.25
      name_list = self.driver.find_elements_by_id('com.tencent.mobileqq:id/tv_name')
      if len(name_list)==0:
          time.sleep(10)
          name_list = self.driver.find_elements_by_id('com.tencent.mobileqq:id/tv_name')
      if self.driver.current_activity == '.activity.TroopMemberListActivity':
          name_list[times].click()
          time.sleep(3)
          result = Tools.findItem(self.driver, 'xpath', '//android.widget.Button[@content-desc="发消息"]')
          if result == True:
              send_button = self.wait.until(
                  EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="发消息"]')))
              send_button.click()
              time.sleep(sleep_time)
              input_text = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mobileqq:id/input')))
              input_text.set_text(message)
              time.sleep(sleep_time)
              send = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mobileqq:id/fun_btn')))
              send.click()
              time.sleep(sleep_time)
              self.driver.back()
              time.sleep(2)
              self.into_group_again()

          else:
              self.driver.back()





  def swipe(self):
      self.driver.swipe(SWIPE_START_X, SWIPE_START_Y, SWIPE_START_X, SWIPE_START_Y - SWIPE_DISTANCE, SWIPE_DURATION_LONG)
      self.add_friends()
  def swipe_group(self):
      self.driver.swipe(SWIPE_START_X, SWIPE_START_Y, SWIPE_START_X, SWIPE_START_Y - SWIPE_DISTANCE, SWIPE_DURATION_LONG)
      self.add_group()

  def add_friends(self ,add_message = ADD_FRIEND_MESSAGE):
      sleep_time = 0.25
      name_list = self.driver.find_elements_by_id('com.tencent.mobileqq:id/tv_name')
      for name in name_list:
          if self.driver.current_activity == '.activity.TroopMemberListActivity':
              name.click()
              time.sleep(sleep_time)
              result = Tools.findItem(self.driver, 'xpath', '//android.widget.Button[@content-desc="加好友"]')
              if result == True:
                  add_button = self.wait.until(
                      EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="加好友"]')))
                  add_button.click()
                  self.driver.wait_activity('.activity.AddFriendVerifyActivity', 10)
                  isdentity = Tools.findItem(self.driver, 'xpath',
                                                   '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.EditText')
                  if isdentity == True:
                      global FRIEND_MESSAGE_FLAG
                      if FRIEND_MESSAGE_FLAG:
                          dentity = self.driver.find_element_by_xpath(
                              '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.EditText')
                          self.driver.keyevent(123)
                          dentity.clear()
                          dentity.set_text(add_message)
                          FRIEND_MESSAGE_FLAG = False
                      self.driver.tap([(672, 102)], NORMAL_TAP)
                      self.driver.wait_activity('.activity.FriendProfileCardActivity', 10)
                      self.driver.back()
                      global ADD_SUCCESS
                      ADD_SUCCESS +=1
                      print('加成功:',ADD_SUCCESS)
                  else:
                      self.driver.tap([(80, 102)], NORMAL_TAP)
                      self.driver.wait_activity('.activity.FriendProfileCardActivity', 10)
                      self.driver.back()
                      global ADD_FALURE
                      ADD_FALURE +=1
                      print('加失败:',ADD_FALURE)

              else:
                  self.driver.back()
                  print('已是好友')
          else:
              # 没回到好友列表
              self.driver.back()
              print('回退')

      self.swipe()










