import os
import signal
import requests
from flask import Flask, request,json,render_template
import  pymysql


app = Flask(__name__)

# #Main method is get_user_name ,and the route for the app called /users/get_user_data/<user_id>
@app.route('/users/get_user_data/<user_id>')
def get_user_name(user_id):
    try:
        conn = pymysql.connect(host='remotemysql.com', port=3306, user='cAcOOBMJ8V', passwd='Nqjg7fU9OB', db='cAcOOBMJ8V')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cAcOOBMJ8V.users where user_id=(%s);", user_id)
        userid = cursor.fetchone()
        if userid == None:

            return "<H1 id='error'>" "no such user:" + str(user_id) + "</H1>"
        else:
            cursor.execute("SELECT user_name FROM cAcOOBMJ8V.users where user_id=(%s);", user_id)
            user_name = cursor.fetchone()
            user_name=user_name[0]
            return "<H1 id='user'>" + user_name + "</H1>"

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

@app.route('/stop_server')
def stop_server():
    try:
        os.kill(os.getpid(),signal.CTRL_C_EVENT)
        return {'status': 'ok','frontend server' :'stopped'} ,200
    except Exception as e:
        print(e)




@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),404

app.run(host='127.0.0.1', debug=True, port=5001)






