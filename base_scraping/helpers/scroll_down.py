def scroll(driver, css_selector, timeout):
	element = "document.querySelector('{}')".format(css_selector)
	scroll_pause_time = timeout
	last_height = driver.execute_script("return {}.scrollHeight".format(element))
	i = 0
	while True:
		driver.execute_script("{}.scrollTo(0, {}.scrollHeight);".format(element, element))
		sleep(scroll_pause_time)
		new_height = driver.execute_script("return {}.scrollHeight".format(element))
		print("-------Scrolling : {}----------".format(i))
		if new_height == last_height:
			break
		last_height = new_height
		i = i + 1
