# coding=gbk
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import Tools

# ��Ⱥ��¼
APPLY_SUCCESS = 0
REQUAIR_INVITE = 0
REQUAIR_VERIFICATION = 0
# �Ӻ��Ѽ�¼
ADD_SUCCESS = 0
ADD_FALURE = 0
# ��������
SWIPE_START_X = 350
SWIPE_START_Y = 1275
SWIPE_DISTANCE = 1100
SWIPE_DURATION_LONG = 3000
SWIPE_DURATION_SHORT = 500
# �������ʱ��
LONG_TAP = 2500
NORMAL_TAP = 200
SHORT_TAP = 50

# �����ؼ���
KEYWORD = "����"
# ���͵�Ĭ����Ϣ
MESSAGE = "���ѽ ���ѽ��ܵ� ����������"
# ������Ϣ�Ĵ���
TIME = 1
# ��������
SWIPE_TIME = 1
# ��Ⱥ���͵���֤��Ϣ
GROUP_MESSAGE_FLAG = True
ADD_GRPOUP_MESSAGE = "ԭ����Ҷ�������"
# �Ӻ���Ĭ�Ϸ�����֤��Ϣ
FRIEND_MESSAGE_FLAG = True
ADD_FRIEND_MESSAGE = "���ѽ��ܵ� ���ѽ"





class AddQQ():

  def __init__(self, drive, wait):

    self.driver = drive
    self.wait = wait
    global SWIPE_DISTANCE
    SWIPE_DISTANCE = self.driver.get_window_size()['height']




  def login(self, username, word):
      time.sleep(3)
      # �������
      if Tools.findItem(self.driver, 'id', 'com.android.packageinstaller:id/permission_allow_button'):
          self.wait.until(EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button'))).click()
      time.sleep(0.5)
      if Tools.findItem(self.driver, 'id', 'com.android.packageinstaller:id/permission_allow_button'):
          self.wait.until(EC.presence_of_element_located((By.ID, 'com.android.packageinstaller:id/permission_allow_button'))).click()
      time.sleep(0.5)
      self.driver.wait_activity('.activity.LoginActivity', 60)
      # �����¼
      self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mobileqq:id/btn_login'))).click()
      time.sleep(1)
      # �����˺�����
      account = self.wait.until(
          EC.presence_of_element_located((By.XPATH, '//android.widget.EditText[@content-desc="������QQ������ֻ�������"]')))
      account.set_text(username)
      password = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mobileqq:id/password')))
      password.set_text(word)
      # �����¼
      login = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mobileqq:id/login')))
      login.click()
      time.sleep(15)

  def find_group(self, keyword = KEYWORD):
      # ����Ӻ�
      self.driver.tap([(666, 95)], NORMAL_TAP)
      time.sleep(1)
      #  ����Ӻ���/Ⱥ
      self.driver.tap([(545, 299)], NORMAL_TAP)
      self.driver.wait_activity('.activity.contact.addcontact.AddContactsActivity', 20)
      time.sleep(1.5)

      # �����Ⱥ
      self.driver.tap([(361, 191)], NORMAL_TAP)
      time.sleep(1)
      # ��������
      self.driver.tap([(528, 1192)], NORMAL_TAP)
      time.sleep(2)
      # ���������
      self.driver.tap([(348, 312)], NORMAL_TAP)
      time.sleep(1)

      # Ѱ������� ��������
      keyword_text = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mobileqq:id/et_search_keyword')))
      keyword_text.set_text(keyword)
      time.sleep(1)
      # �����һ����Ⱥ
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
          # ���ÿ��
          self.driver.tap([(350, 250+220*i)], 100)
          time.sleep(sleep_time)
          # �ж��Ƿ�������밴ť
          apply = Tools.findItem(self.driver, 'accessibility id', '��Ϣ�����')
          if apply:
              self.driver.back()
              self.driver.wait_activity('.activity.QQBrowserActivity', 10)
          else:
              # �������
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
                  print('����ɹ�:', APPLY_SUCCESS)
              else:
                  time.sleep(3)
                  # �ٴε�����⿨ס
                  self.driver.tap([(350, 1215)], NORMAL_TAP)
                  time.sleep(2)
                  if self.driver.current_activity == '.activity.ChatSettingForTroop':
                      self.driver.back()
                      global REQUAIR_INVITE
                      REQUAIR_INVITE += 1
                      print('��Ҫ�����Ⱥ:', REQUAIR_INVITE)
                  else:
                      self.driver.back()
                      self.driver.wait_activity('.activity.ChatSettingForTroop', 10)
                      self.driver.back()
                      global REQUAIR_VERIFICATION
                      REQUAIR_VERIFICATION = REQUAIR_VERIFICATION + 1
                      print('��Ҫ�ش�����:', REQUAIR_VERIFICATION)
          i += 1
      self.swipe_group()






  def into_group(self):
      # ����ö�Ⱥ
      first = self.wait.until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.AbsListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout')))
      first.click()
      self.driver.wait_activity('.activity.SplashActivity', 10)
      time.sleep(1)
      # ������Ͻ�
      right_button = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mobileqq:id/ivTitleBtnRightImage')))
      right_button.click()
      time.sleep(3)
      # ���Ⱥ�ĳ�Ա
      person = self.wait.until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.AbsListView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView[2]')))
      person.click()
      time.sleep(30)
      # ��������λ��
      self.driver.swipe(SWIPE_START_X, 230, SWIPE_START_X, 150, SWIPE_DURATION_SHORT)

  def into_group_again(self):
      # ����ö�Ⱥ
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
      # ������Ͻ�
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
      # ���Ⱥ�ĳ�Ա
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
      # ��������λ��
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
          result = Tools.findItem(self.driver, 'xpath', '//android.widget.Button[@content-desc="����Ϣ"]')
          if result == True:
              send_button = self.wait.until(
                  EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="����Ϣ"]')))
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
              result = Tools.findItem(self.driver, 'xpath', '//android.widget.Button[@content-desc="�Ӻ���"]')
              if result == True:
                  add_button = self.wait.until(
                      EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="�Ӻ���"]')))
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
                      print('�ӳɹ�:',ADD_SUCCESS)
                  else:
                      self.driver.tap([(80, 102)], NORMAL_TAP)
                      self.driver.wait_activity('.activity.FriendProfileCardActivity', 10)
                      self.driver.back()
                      global ADD_FALURE
                      ADD_FALURE +=1
                      print('��ʧ��:',ADD_FALURE)

              else:
                  self.driver.back()
                  print('���Ǻ���')
          else:
              # û�ص������б�
              self.driver.back()
              print('����')

      self.swipe()










