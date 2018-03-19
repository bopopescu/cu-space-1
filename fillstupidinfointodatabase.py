from flask import Flask, render_template
from random import choice, randrange
import hashlib, uuid
#NOTE!!
#install flask-mysql first by writing in terminal "pip install flask-mysql"
from flaskext.mysql import MySQL
app = Flask('__CUSpace__')
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'cuspace'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
# --------------------------------------------------INSERTING CATEGORY NAME AND ID INTO DATABASE---------------------------------------
#ALTER_INCREMENT ALL THE TABLE FIRST!
cursor = conn.cursor()
# sql = """ALTER TABLE `dis_category` AUTO_INCREMENT = 1"""
# sql2 = """INSERT INTO `dis_category`(`Dis_cat_name`) VALUES ("Architecture"),("Arts"),("Business"),
# ("Communication_arts"),("Economic"),("Engineering"),("Psychology"),("Science"),("General_education"),("Activities")"""
# try:
#     # cursor.execute(sql)
#     cursor.execute(sql2)
#     conn.commit()
# except:
#     print("Fail to insert category list")
# cursor.close()
#
# #---------------------------------------------------INSERTING RANDOM DATA INTO CATEGORY DATA -------------------------------------------
# content = "hello world"
# topic = "hello"
#
# for i in range(100):
#     user_id = randrange(1,10000)
#     dis_id = 0
#     dis_cat_id = 0
#     cursor = conn.cursor()
#     oldsql = """SELECT * FROM `discussion` WHERE user_id = %s """
#     try:
#         cursor.execute(oldsql, str(user_id))
#         olddata = cursor.fetchall()
#         while cursor.rowcount != 0:
#             user_id = randrange(1, 10000)
#             oldsql = """SELECT * FROM `discussion` WHERE user_id = %s """
#             cursor = conn.cursor()
#             cursor.execute(oldsql, str(user_id))
#             olddata = cursor.fetchall()
#         #print(user_id)
#     except:
#         print("Cannot query user_id: "+user_id)
#     sql2 = "INSERT INTO `discussion`(`User_id`, `Topic`, `Content`) VALUES (%s,%s,%s)"
#     try:
#         cursor.execute(sql2, (user_id, topic, content))
#         conn.commit()
#     except:
#         print("SHIT")
#     sqlFordis_id = """SELECT `dis_id` FROM `discussion`"""
#     sqlFordis_cat_id = """SELECT `dis_cat_id` FROM `dis_category`"""
#     try:
#         cursor.execute(sqlFordis_id)
#         dis_idList = cursor.fetchall()
#         if(dis_idList.__len__() >1):
#             dis_idList = [i[0] for i in dis_idList]
#             dis_id = choice(dis_idList)
#         else:
#             dis_id = [i[0] for i in dis_idList][0]
#     except:
#         print("Cannot query dis_id")
#     try:
#         cursor.execute(sqlFordis_cat_id)
#         dis_cat_idList = cursor.fetchall()
#         if (dis_cat_idList.__len__() > 1):
#             dis_cat_idList = [i[0] for i in dis_cat_idList]
#             dis_cat_id = choice(dis_cat_idList)
#         else:
#             dis_cat_id = [i[0] for i in dis_cat_idList][0]
#     except:
#         print("cannot query dis_cat_id")
#     sql3 = "INSERT INTO `dis_category_group`(`Dis_id`, `Dis_cat_id`) VALUES ({},{})".format(dis_id,dis_cat_id)
#     try:
#         cursor.execute(sql3)
#         conn.commit()
#     except:
#         print("Cannot inesrt dis_cat_group")
#     cursor.close()
#     print(i)

#-------------------------------------- INSERT TUTOR AND USER DATA --------------------------------------
#USER INFO
password = "he11o".encode('utf-8')
user_key = hashlib.md5()
user_key.update(password)
user_key= user_key.hexdigest()
print(user_key)
firstname = "hello"
lastname = "world"
role ="helloing world"
ban_status ="0"

#TUTOR INFO
bio = "OH MY WORLD"
skill = "helloingworld"
achievement = "hello 3 time"
exp = "hello 3! time"
subject = "Chompoonuch"
video ="www.youtube.com/kokkok"
for i in range(30):
    #tutor_and_user = uuid.uuid4().hex
    tutor_and_user = randrange(1,100000000)
    user_and_tutor_cursor = conn.cursor()
    email = "hello" + str(randrange(1, 10000)) + "@world.com"
    username = "hello" + str(randrange(1, 10000)) + "world"
    try:
        insert_user__SQL = """INSERT INTO `user`(`User_id`, `Email`, `Username`, `User_key`, `Firstname`, `Lastname`, `Role`, `Ban_status`) 
                                  VALUES (%s,%s,%s,%s,%s,%s,%s,%s) """
        user_and_tutor_cursor.execute(insert_user__SQL, (tutor_and_user,email,username,user_key,firstname,lastname,role
                                          ,ban_status))
        try:
            insert_tutor_SQL = """INSERT INTO `tutor`(`User_id`, `Bio`, `Skill`, `Achievement`, `Experience`, `Subject`, `Video`) 
                                  VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            user_and_tutor_cursor.execute(insert_tutor_SQL,(tutor_and_user,bio,skill,achievement,exp,subject,video))
            conn.commit()
        except:
            print("Cannot insert into tutor")
    except:
        print("Cannot insert into User")
user_and_tutor_cursor.close()
conn.close()



