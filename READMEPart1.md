#Project First Part

REST API (module name: rest_app.py):
The REST API gateway will be: 127.0.0.1:5000/users/<USER_ID>

Methods descriptions: 
All the methods of  REST API  are under main method called user(user_id)
1.	request.method == 'POST' :
•	Will accept user_name parameter inside the JSON payload.A new user will be created in the database .
•	Will call method inserttodb(user_name,user_id)- inserttodb :this method will accept userid and username as input and retrieve the username will return error message that user is already exist


2.	 request.method == GET :
•	returns the user name stored in the database for a given user id. 
•	Will call the method getfromdb:this method will accept userid  input and retrieve the username in case of the user is exist else it will return error message user is not exist  
•	Sample output  for get request : 


3.	request.method == PUT :
•	will modify existing user name (in the database).
•	Will call the method updatedb:this method will accept userid and username as input and retrieve the  updated username in case of the user is exist else it will return error message user is not exist

4.	request.method == DELETE :
•	will delete existing user (from database).
•	Will call the method : delfromdb:this method will accept userid  input and retrieve the userid after deleting the record related to  it  in case of the user not exist   will return error message.
•	Sample output  for delete request : 



Database (module name: db_connector.py):
I created the table users and  follow the requirement  what related to  fields name and  description . 
For each request method I defined a sperate methods this methods will be called on the REST_APP . 
1.	inserttodb(user_name,user_id)
2.	getfromdb(user_id)
3.	updatedb(user_name,user_id)
4.	delfromdb(user_id) 


Web interface (module name: web_app.py):
1.	The web interface will return the user name of a given user id stored inside users table
2.	It will user main method called : get_user_name(user_id)- it will first connect to the DB and then run select statement to check if the user id is exist – in no exist it will return the error message : return  no such user: + user_id


Testing  : 
1.	Frontend testing – for web interface testing :
     I created module frontend_testing.py -which it will start the webdriver and navigate to an existed user id  ,and search the element by user id and then it will validate if this element if enabled  and then it will extract the value by locator.text and print this value which it will represent the username  . 

2.	Backend testing – for REST API and Database testing 
I created the module backend_testing.py by  defining two methods for the post and get which the post  will  accept username and userid and will retrieve  id in case of ok and this id can by  user as input for the get  method , and then for DB testing I will connect and execute select statement due the same id  -and extract the username  and compare it to the added username and print the results . 

3.	Combined testing – for Web interface, REST API and Database testing
I created the module combined_testing.py I defined 4 methods for testing this module the post which will accept username and userid and return userid , the userid will be input for the get statement , and for mysql I will  user the same username and id and check if the retrieved username is equal to the username as  result from the execution of the select statement . 
Same for frontend testing this method will accept username and id , this id for concatenating it on the  URL and  username for comparing it with username which extracted from the locator value . it will return user verified in case if true else user not found . 

















