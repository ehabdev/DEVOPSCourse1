import requests
import json
import random
import pymysql

#verify that user id is avalible .

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



def gen_username(userid):
    return ('user'+str(userid))

userid=getuserid()
username=gen_username(userid)



def postreq(userid,username):

    res = requests.post('http://127.0.0.1:5000/users/'+str(userid), json={"user_name":username})
    if res.ok:
        print(res.json())
        return userid
    else:
        print(res.json())


def getreq(userid):
    res = requests.get('http://127.0.0.1:5000/users/'+str(userid))
    if res.ok:
        print(res.json())
    else:
        print(res.json())


def verdb(userid,username):
    try:

        conn = pymysql.connect(host='remotemysql.com', port=3306, user='cAcOOBMJ8V', passwd='Nqjg7fU9OB', db='cAcOOBMJ8V')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cAcOOBMJ8V.users where user_id=(%s);", userid)
        userid = cursor.fetchone()


        if userid[1] == username:
            print ("user name added successfully ")
        else :
            print("failed to insert user name")

    except Exception as e:
        print("test failed ")

    finally:
        cursor.close()
        conn.close()



userid=getuserid()
username=gen_username(userid)
postreq(userid,username)
getreq(userid)
verdb(userid,username)