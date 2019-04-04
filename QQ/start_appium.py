import multiprocessing
import subprocess
import time

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import QQ

PHONES = 2

server = []

for i in range(1000, 1000+PHONES*2, 2):
    server.append(i)


devices_list = ['9MPBB18331150564',
                '192.168.20.242:5555',
                '35f711a67d94']

def appium_start(device, server, username, password):

    desired_caps = {
        "platformName": "Android",
        "deviceName": device,
        "appPackage": "com.tencent.mobileqq",
        "appActivity": ".activity.SplashActivity",
        "unicodeKeyboard": True,  # 使用unicodeKeyboard的编码方式来发送字符串
        "resetKeyboard": True,
        "udid": device
    }

    driver = webdriver.Remote('http://localhost:%s/wd/hub' %server, desired_caps)
    wait = WebDriverWait(driver, 2)
    send = QQ.AddQQ(driver, wait)
    send.login(username, password)
    send.into_group()
    send.send_message()


# 构建appium进程组

appium_process = []

thread_process = []

# 帐号密码
usernames = ['823860856', '495341828']
password = ['0323zyc*1216lyf', '614715703']

for i in range(len(server)):
    # 打开终端开启端口

    subprocess.Popen("node /Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js --port %s" %str(server[i]), shell=True)

    time.sleep(4)

    # target指向方法，args指向参数，且必须是一个元组的形式

    appium = multiprocessing.Process(target=appium_start, args=(devices_list[i], str(server[i]), usernames[i], password[i]))

    # 将进程从变量appium加载到进程内

    appium_process.append(appium)

if __name__ == '__main__':
    #同时启动多设备执行测
    for desired in appium_process:
        desired.start()  #每个进程去启动
    for desired in  appium_process:
        desired.join()
