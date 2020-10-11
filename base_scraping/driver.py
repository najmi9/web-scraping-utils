#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
Created on Tusday Sep 29 10:54:42 2020

@author: Najmi Imad
"""
from selenium import webdriver
from fake_useragent import UserAgent
#from selenium.webdriver.common.proxy import Proxy, ProxyType

def browser(headless = False):
	ua = UserAgent()
	a = ua.random
	user_agent = ua.random
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument(f'user-agent={user_agent}')
	chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "safebrowsing-disable-download-protection", "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection"])
	chrome_options.add_argument('--enable-automation')
	chrome_options.add_argument('--disable-extensions')
	chrome_options.add_argument('--profile-directory=Default')
	chrome_options.add_argument("--incognito")
	chrome_options.add_argument("--disable-plugins-discovery")
	chrome_options.add_argument('--ignore-certificate-errors')
	chrome_options.add_argument('--ignore-ssl-errors')
	chrome_options.headless=headless
	"""
	PROXY = "185.26.33.84:8080"
	prox = Proxy()
	prox.proxy_type = ProxyType.MANUAL
	prox.autodetect = False
	capabilities = webdriver.DesiredCapabilities.CHROME
	prox.http_proxy = PROXY
	prox.ssl_proxy = PROXY
	prox.add_to_capabilities(capabilities)
	

	driver = webdriver.Chrome(executable_path="../chromedriver",
		chrome_options=chrome_options, desired_capabilities = capabilities)
	"""
	driver = webdriver.Chrome(executable_path="../chromedriver", chrome_options=chrome_options)
	driver.delete_all_cookies()
	driver.set_window_size(1600,1000)
	driver.set_window_position(0,0)
	
	return driver
