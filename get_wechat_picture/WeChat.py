import time
from get_wechat_picture import get_num

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class AddWeChat():
  def __init__(self):
    server = 'http://localhost:4723/wd/hub'
    desired_caps = {
      "platformName": "Android",
      "deviceName": "35f711a67d94",
      "appPackage": "com.tencent.mm",
      "appActivity": ".ui.LauncherUI"
    }
    self.driver = webdriver.Remote(server, desired_caps)
    self.wait = WebDriverWait(self.driver, 1)



  def login(self):
    # 登录
    time.sleep(2)
    self.driver.tap([(503, 1186)], 5)
    time.sleep(1)
    self.driver.tap([(191,1180)])
    # 手机号登录
    # phone = self.wait.until(EC.presence_of_element_located((By.ID,'com.tencent.mm:id/kh')))
    # phone.set_text("18606522921")
    # time.sleep(1)
    # self.driver.tap([(657, 783)],500)
    # time.sleep(2)
    # password = self.wait.until(EC.presence_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText')))
    # password.set_text("mifeng888")
    # time.sleep(1)
    # self.driver.tap([(404, 774)], 500)


    # 账号密码登录
    time.sleep(2)
    self.driver.tap([(175, 637)],500)
    time.sleep(2)
    account = self.wait.until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText')))
    account.set_text("ayiya777")
    password = self.wait.until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText')))
    password.set_text("mifeng888")
    # 防止键盘弹出
    # self.driver.tap([(657, 662)], 500)
    # time.sleep(2)
    self.driver.tap([(417, 789)], 500)
    time.sleep(10)
    self.driver.tap([(341, 828)], 500)
    time.sleep(20)

    # 加号
    self.driver.tap([(660, 99)], 500)
    time.sleep(1.5)
    # 添加
    self.driver.tap([(532, 327)], 500)
    time.sleep(1.5)
    # 点击头部
    self.driver.tap([(339, 226)], 500)
    time.sleep(1.5)

  def addfriend(self, num):
    # 加好友
    # 寻找输入框
    number = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/kh')))
    # 输入
    number.set_text(num)
    time.sleep(2)
    # 点击第一条结果
    self.driver.tap([(332, 218)])
    time.sleep(1.5)
    try:

      layout = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/b3w')))
      # 点击头像
      layout.click()

      time.sleep(4)
      # 长按
      self.driver.tap([(341, 680)], 2000)

      time.sleep(1)
      # 保存
      self.driver.tap([(336, 671)], 500)
      time.sleep(4)
      self.driver.tap([(341, 680)], 100)
      time.sleep(2)
      self.driver.back()
      time.sleep(4)
      with open("useful_tel_new", "a", encoding="utf-8") as f:
        f.write(num)
        f.write("\n")
    except TimeoutException:
      with open("useless_tel_new", "a", encoding="utf-8") as f:
        f.write(num)
        f.write("\n")

      self.driver.back()
      time.sleep(2)


def start_add_wechat(num):
  doit = AddWeChat()
  doit.login()
  a = get_num.a
  len = get_num.length
  time.sleep(2)
  for i in range(num, len):
    doit.addfriend(a[i - 1])
