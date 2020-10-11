from base_scraping.driver import browser
from base_scraping.helpers.utils import delay as dl
from selenium.webdriver.common.keys import Keys
import csv

keyword = input('What is your keyword ! \t')


driver = browser(True)
url = "https://www.google.com/"
driver.get(url)
dl(1, 3)

q = driver.find_element_by_css_selector("input[name='q']")

q.send_keys(keyword)

q.send_keys(Keys.ENTER)

dl(6, 10)

elmnts = driver.find_elements_by_css_selector('.DKV0Md span')
websites = driver.find_elements_by_css_selector('.tjvcx span')

with open('data.csv', 'w') as f:
	csv_file = csv.writer(f)
	csv_file.writerow(['id', 'site', 'title'])

for (i, elmnt) in enumerate(elmnts):
	print(websites[i].text)
	websites[i].screenshot()
	with open('data.csv', 'a') as f:
		csv_file = csv.writer(f)
		csv_file.writerow([i, websites[i].text, elmnt.text])

print("done")