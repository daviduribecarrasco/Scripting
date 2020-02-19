from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
#from account import username,mypass



def likebot():

    print("Enter account username:")
    username = input()

    print("Enter the password:")
    my_pass = input()

    print("Enter account whose post you want to like:")
    acc = input()
    
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")
    assert "Instagram" in driver.title
    sleep(3)

    user= driver.find_element_by_name("username")
    user.clear()
    user.send_keys(username)

    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys(my_pass)

    login= driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
    login.click()

    sleep(3)

    annoyingnotifications = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
    annoyingnotifications.click()

    search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
    search.send_keys(acc)
    search.send_keys(u'\ue007')

    picture = driver.find_element_by_class_name("_9AhHO")
    picture.click()

    like = driver.find_element_by_class_name("wpO6p")
    like.click()


if __name__ == '__main__':
    likebot()
