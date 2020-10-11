#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
Created on Tusday Sep 29 10:54:42 2020

@author: Najmi Imad
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import speech_recognition as sr
import requests
import pydub
from base_scraping.helpers.delay import delay

def solve_captch_v2(driver):
	wait = WebDriverWait(driver, 10)
	wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
	wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

	#switch to recaptcha audio control frame
	driver.switch_to.default_content()
	xpath= "/html/body/div[2]/div[4]"
	frames=driver.find_element_by_xpath(xpath).find_elements_by_tag_name("iframe")
	driver.switch_to.frame(frames[0])

	driver.find_element_by_id("recaptcha-audio-button").click()
	delay(1, 2)
	#switch to recaptcha audio challenge frame
	driver.switch_to.default_content()
	frames= driver.find_elements_by_tag_name("iframe")
	driver.switch_to.frame(frames[-1])
	delay(2, 5)

	src = driver.find_element_by_id('audio-source').get_attribute('src')

	r = requests.get(src, allow_redirects=True)

	with open('audio.mp3', 'wb') as f:
		f.write(r.content)
	sound = pydub.AudioSegment.from_mp3("audio.mp3")
	sound.export("audio.wav", format="wav")
	sample_audio = sr.AudioFile("audio.wav")
	r= sr.Recognizer()

	with sample_audio as source:
    	audio = r.record(source)

	#translate audio to text with google voice recognition
	key=r.recognize_google(audio)

	print("[INFO] Recaptcha Passcode: %s"%key)

	driver.find_element_by_css_selector("input#audio-response").send_keys(key)
	delay(3, 4)
	driver.find_element_by_css_selector('button#recaptcha-verify-button').click()
	driver.switch_to.default_content()

