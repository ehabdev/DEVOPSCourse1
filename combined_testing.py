import requests
import  pymysql
import random
import json
from selenium import webdriver
from selenium.webdriver.common.by import By


#combined testing module  for backend ,frontend and db .

def getuserid():
    finduser=True
    rid = random.randint(100, 1000)
    try:

        conn = pymysql.connect(host='remotemysql.com', port=3306, user='cAcOOBMJ8V', passwd='Nqjg7fU9OB', db='cAcOOBMJ8V')
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM cAcOOBMJ8V.users where user_id=(%s);", rid)
        userid = cursor.fetchone()
        if userid == None:
            return rid
        else:
            while finduserid:
                rid = random.randint(100, 1000)
                cursor.execute("SELECT user_id FROM cAcOOBMJ8V.users where user_id=(%s);", rid)
                userid = cursor.fetchone()
                if userid == None:
                    return rid
                    finduserid=False
    except Exception as e:
        print (e)

    finally:
        cursor.close()
        conn.close()

#method to generate the username concatantion of usid+string user .
def genusername(userid):
    return ('user'+str(userid))

#method for post req
def postreq(userid,username):
    res = requests.post('http://127.0.0.1:5000/users/'+str(userid), json={"user_name":username})
    if res.ok:
        print(res.json())
        return id
    else:
        print(res.json())

#method for get request
def getreq(userid):
    res = requests.get('http://127.0.0.1:5000/users/'+str(userid))
    if res.ok:
        print(res.json())
    else:
        print(res.json())



#method for veirfying the userid is exist

def chkmysql(userid,username):
    try:

        conn = pymysql.connect(host='remotemysql.com', port=3306, user='cAcOOBMJ8V', passwd='Nqjg7fU9OB', db='cAcOOBMJ8V')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cAcOOBMJ8V.users where user_id=(%s);", userid)
        userid = cursor.fetchone()
        print (userid)
        if userid[1] == username :
            print ("user name added successfully ")
        else :
            print("failed to insert user name")

    except Exception as e:
        print("test failed ")

    finally:
        cursor.close()
        conn.close()


#method for fronend testing

def verifyfront(userid):
    url='http://127.0.0.1:5001/users/get_user_data/'+str(userid)
    path='C:\\Users\\idavos\\Desktop\\Devopscourse\\chromedriver.exe'
    try:
        driver = webdriver.Chrome(executable_path=path)
        driver.implicitly_wait(3)
        driver.get(url)
        driver.maximize_window()


        iduser=driver.find_element_by_id("user")
        driver.implicitly_wait(3)
        if iduser.is_enabled():
            print(iduser.text)
        else:
            print ("Can not find element  ")

    except Exception as e :
            print("test failed")

    finally:

        driver.quit()


#call the getuserid
userid=getuserid()

#call the genusername
username=genusername(userid)

#call postreq
postreq(userid,username)

#call getreq
getreq(userid)

#call chkmysql
chkmysql(userid,username)

#call verify front
verifyfront(userid)
