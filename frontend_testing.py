from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import pymysql



#This moudle will verify if the userid is exist on the DB then it will return it ,which will be input for the frontend veriefy .
# method getuserid(): that user id is avalible .

def verifytuserid():

    try:

        conn = pymysql.connect(host='remotemysql.com', port=3306, user='cAcOOBMJ8V', passwd='Nqjg7fU9OB', db='cAcOOBMJ8V')
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM cAcOOBMJ8V.users" )
        userid = cursor.fetchone()
        if userid != None:
            return userid
        else:
            print("db is empty no users found")
    except Exception as e:
        print (e)

    finally:
        cursor.close()
        conn.close()




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

userid=verifytuserid()
userid=userid[0]
verifyfront(userid)