from selenium import webdriver
from selenium.webdriver.common.keys import Keys

debug = False

def fbLogin():
    if(debug == True):
        user = "YourTestEmail"
        passWord = "YourTestPassWord"
    else:
        user = input("what is your userName?")
        passWord = input("what is your passwWord")
    driver = webdriver.Chrome()
    driver.get("https://facebook.com")
    assert "Facebook" in driver.title
    elem = driver.find_element_by_id("email")
    elem.clear()
    elem.send_keys(user)
    elem = driver.find_element_by_id("pass")
    elem.clear()
    elem.send_keys(passWord)
    elem.send_keys(Keys.RETURN)
    

def getPosts():
    elem = driver.find_element_by_id("p")
    print(elem)



fbLogin()
getPosts()
