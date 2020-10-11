from base_scraping.driver import browser
from base_scraping.helpers.utils import delay as dl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def login(driver, url, username, password, username_xpath, password_xpath, submit_xpath):
	driver.get(url)
	dl(5,10)
	wait = WebDriverWait(driver, 10)
	actions = ActionChains(driver)
	
	input = wait.until(EC.presence_of_element_located((By.XPATH, username_xpath)))
	actions.move_to_element(input).perform()
	input.send_keys(username)
	
	input = wait.until(EC.presence_of_element_located((By.XPATH, password_xpath)))
	actions.move_to_element(input).perform()
	input.send_keys(password)

	btn = wait.until(EC.element_to_be_clickable((By.XPATH, submit_xpath)))
	actions.move_to_element(btn).click().perform()

