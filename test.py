import os
import subprocess

server = []

for i in range(1000, 1004, 2):
    server.append(i)


print(server)

# os.system( "node /Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js --port %s" % 2000)

subprocess.Popen("node /Applications/Appium.app/Contents/Resources/app/node_modules/appium/build/lib/main.js --port %s" % 2000, shell=True)