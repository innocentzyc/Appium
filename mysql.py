import pymysql

config={
    "host":"127.0.0.1",
    "user":"root",
    "password":"MIfeng888!",
    "database":"zyc"
}

connect = pymysql.connect(**config)
# 建立游标对象
cur = connect.cursor()
# 获取所有
sql_getall = "select * from userinfo"
# 添加参数
sql_add = "INSERT INTO userinfo(username,passwd) VALUES(%s,%s)"

cur.execute(sql_getall)

data = cur.fetchall()

for person in data:
    print(person)


print('--------------')



# cur.execute(sql_add, ("inocent","32232"))

#切记提交数据
# connect.commit()

# data_new = cur.execute(sql_getall)
#
# for person in data_new:
#     print(person)

cur.close()
connect.close()