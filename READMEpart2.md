Project Second Part

Python code changes:

•	rest_app.py module : I added the stop_server method which will take action in stopping the server after completing running all the CI pipeline .

•	web_app.py: same as rest_app.py module .

•	backend_testing.py : I added some methods to convert the flow fully automated . method for verifying the userid is not exist on the DB ,then in other method I will generate username by concatenating userid+’user’ .and both values will be input for the pots request ,and the userid will be input for the get request as well . 

•	frontend _testing.py: I added another method to execute select statement on the DB and retrieve exist userid , this userid will be input for the get request which will retrieve the username related to the userid using the Selenium   .

•	combined_testing.py : I merged  between these automated flows to get  the combined testing .

•	clean_environemnt.py : it  will call each method on the web and rest server in order to stop the servers runs .

also for extra4 : 
I added new method page_not_found using render_template using very simple html file to return page not found . 


Jenkins pipeline configurations:

•	I added my Jenkinsfile which include the all the pipeline stages and following all the requirements  ,and run this  build many times to verify it stability and output 
•	Also for the Extra 1,and 3 I added two files  Jenkinswithpost for Extra 1 , ParameterizedJenkinesfile for Extra 3 .







