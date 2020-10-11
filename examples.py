

from base_scraping.helpers.utils import url

url = url("https://mbasic.facebook.com/login/")

username = ""
password = ""
username_xpath='//*[@id="m_login_email"]'
password_xpath = '//*[@id="login_form"]/ul/li[2]/section/input'
submit_xpath = '//*[@id="login_form"]/ul/li[3]/input'
driver = browser()

login(driver, url, username, password, username_xpath, password_xpath, submit_xpath)

