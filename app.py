from selenium import webdriver
import info


browser = webdriver.Chrome()
browser.get("https://github.com")
signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()
username = browser.find_element_by_id("login_field")
username.send_keys(info.username)
password = browser.find_element_by_id("password")
password.send_keys(info.password)
password.submit()
