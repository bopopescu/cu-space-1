from flask import Flask, render_template
from random import choice, randrange
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
sql2 = """INSERT INTO `dis_category`(`Dis_cat_name`) VALUES ("Architecture"),("Arts"),("Business"),
("Communication_arts"),("Economic"),("Engineering"),("Psychology"),("Science"),("General_education"),("Activities")"""
try:
    # cursor.execute(sql)
    cursor.execute(sql2)
    conn.commit()
except:
    print("Fail to insert category list")
cursor.close()

#---------------------------------------------------INSERTING RANDOM DATA INTO CATEGORY DATA -------------------------------------------
content = "hello world"
topic = "hello"

for i in range(100):
    user_id = randrange(1,10000)
    dis_id = 0
    dis_cat_id = 0
    cursor = conn.cursor()
    oldsql = """SELECT * FROM `discussion` WHERE user_id = %s """
    try:
        cursor.execute(oldsql, str(user_id))
        olddata = cursor.fetchall()
        while cursor.rowcount != 0:
            user_id = randrange(1, 10000)
            oldsql = """SELECT * FROM `discussion` WHERE user_id = %s """
            cursor = conn.cursor()
            cursor.execute(oldsql, str(user_id))
            olddata = cursor.fetchall()
        #print(user_id)
    except:
        print("Cannot query user_id: "+user_id)
    sql2 = "INSERT INTO `discussion`(`User_id`, `Topic`, `Content`) VALUES (%s,%s,%s)"
    try:
        cursor.execute(sql2, (user_id, topic, content))
        conn.commit()
    except:
        print("SHIT")
    sqlFordis_id = """SELECT `dis_id` FROM `discussion`"""
    sqlFordis_cat_id = """SELECT `dis_cat_id` FROM `dis_category`"""
    try:
        cursor.execute(sqlFordis_id)
        dis_idList = cursor.fetchall()
        if(dis_idList.__len__() >1):
            dis_idList = [i[0] for i in dis_idList]
            dis_id = choice(dis_idList)
        else:
            dis_id = [i[0] for i in dis_idList][0]
    except:
        print("Cannot query dis_id")
    try:
        cursor.execute(sqlFordis_cat_id)
        dis_cat_idList = cursor.fetchall()
        if (dis_cat_idList.__len__() > 1):
            dis_cat_idList = [i[0] for i in dis_cat_idList]
            dis_cat_id = choice(dis_cat_idList)
        else:
            dis_cat_id = [i[0] for i in dis_cat_idList][0]
    except:
        print("cannot query dis_cat_id")
    sql3 = "INSERT INTO `dis_category_group`(`Dis_id`, `Dis_cat_id`) VALUES ({},{})".format(dis_id,dis_cat_id)
    try:
        cursor.execute(sql3)
        conn.commit()
    except:
        print("Cannot inesrt dis_cat_group")
    cursor.close()

    print(i)
