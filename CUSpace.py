from flask import Flask, render_template
import math
#NOTE!!
#install flask-mysql first by writing in terminal "pip install flask-mysql" in order to use
from flaskext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'cuspace'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def index():
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = """SELECT * FROM `dis_category`"""
    cursor.execute(sql)
    data = cursor.fetchall()
    categoryList = [ i[1] for i in data]
    return render_template('index.html', catlist = categoryList)

@app.route('/tutor')
def tutor():
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = """SELECT * FROM `tutor` t 
             INNER JOIN `profile_picture` prof ON t.User_id = prof.user_id 
             INNER JOIN `subject_group` sub_grp ON t.user_id = sub_grp.user_id 
             INNER JOIN `subject` sub ON sub.subject_id = sub_grp.subject_id
             INNER JOIN `user` ON user.User_id = t.user_id """
    try:
        cursor.execute(sql)
        tutorData = cursor.fetchall()
        print(tutorData)
    except:
        print("Cannot query tutor data")
    return render_template('tutor2.html', tutorList = tutorData)

@app.route('/job')
def job():
    return render_template('job.html')

@app.route('/job-profile')
def jobProfile():
    return render_template('job-profile.html')

@app.route('/company')
def company():
    return render_template('company.html')

@app.route('/tutor/<tutor_id>')
def profile():
    return render_template('profile2.html')

@app.route('/newpost')
def newpost():
    return render_template('newpost.html')

@app.route('/registernewtutor')
def registernewtutor():
    return render_template('newtutor.html')


@app.route('/discussion/<category>/', defaults={'page':1})
@app.route('/discussion/<category>/<page>')
def discussion(category, page):
    numDataStart = ((int(page)-1)*15)
    numDataEnd = int(page)*15
    conn = mysql.connect()
    cursorCat = conn.cursor()
    sqlCat = """SELECT * FROM dis_category"""
    try:
        cursorCat.execute(sqlCat)
        categoryList = cursorCat.fetchall()
        categoryName = [i[1] for i in categoryList]
    except:
        print("Cannot query category name")
    if(category in categoryName):
        cursor = conn.cursor()
        # sqlListed = """SELECT catgrp.dis_cat_group_id
        #         ,catgrp.dis_id
        #         ,catgrp.dis_cat_id
        #         ,cat.Dis_cat_name
        #         ,dis.User_id
        #         ,dis.Topic
        #         ,dis.Content
        #         ,dis.Create_Time
        #         FROM `dis_category_group` catgrp
        #         INNER JOIN `dis_category` cat ON catgrp.dis_cat_id = cat.Dis_cat_id
        #         INNER JOIN `discussion` dis ON dis.Dis_id = catgrp.dis_id
        #         WHERE cat.Dis_cat_name = %s"""
        numOfDataSQL = """SELECT COUNT(*) 
                       FROM `dis_category_group` dis 
                       INNER JOIN dis_category cat ON dis.dis_cat_id = cat.Dis_cat_id 
                       WHERE cat.Dis_cat_name =  %s"""
        try:
            cursor.execute(numOfDataSQL,category)
            numOfData = cursor.fetchone()
            print(numOfData)
        except:
            print("Cannot query the data in Category: " + category)

        sqlWanted = """SELECT catgrp.dis_cat_group_id 
                ,catgrp.dis_id
                ,catgrp.dis_cat_id
                ,cat.Dis_cat_name
                ,dis.User_id
                ,dis.Topic
                ,dis.Content
                ,dis.Create_Time 
                FROM `dis_category_group` catgrp 
                INNER JOIN `dis_category` cat ON catgrp.dis_cat_id = cat.Dis_cat_id 
                INNER JOIN `discussion` dis ON dis.Dis_id = catgrp.dis_id 
                WHERE cat.Dis_cat_name = %s LIMIT %s,%s"""
        try:
            cursor.execute(sqlWanted, (category,numDataStart,numDataEnd))
            dataWanted = cursor.fetchall()
            numPage = int(math.ceil(float(numOfData[0])/float(15)))
            print(numPage)
        except:
            print("Cannot query the data in Category: "+category)
        cursor.close()
        return render_template('discussion.html',cat = category, discussion = dataWanted, numofPage = numPage)

if __name__ == '__main__':
    app.run()
