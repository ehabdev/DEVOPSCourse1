from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Windows:
driver = webdriver.Chrome(executable_path="C:\\Users\\idavos\\Desktop\\Devopscourse\\chromedriver.exe")
driver.implicitly_wait(3)
driver.get("https://translate.google.com/?hl=iw&eotf=0&sl=hr&tl=iw")
print(driver.current_url)
print(driver.title)
#print(driver.page_source)

#driver.find_element_by_class_name("er8xn").send_keys("hello")
sendkey=driver.find_element(by=By.CLASS_NAME,value="er8xn")
sendkey.send_keys("hello")
driver.implicitly_wait(5)
sendkey.clear()
if sendkey.is_enabled():
    print ("value is Verified")

sendkey.send_keys(Keys.ENTER)


mylist=driver.find_elements_by_class_name("er8xn")
print(len(mylist))

#driver.quit()

