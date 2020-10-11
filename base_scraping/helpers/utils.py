import time
import random
import requests # to get image from the web
import shutil # to save it locally
import os


def url(url):
	from env import api_key
	url_with_proxy = "http://api.scraperapi.com?api_key={}&url={}&render=true".format(api_key, url)
	return url_with_proxy


def delay(min=1, max=10):
	time.sleep(random.randint(min, max))

def download(src, folder=os.getcwd()):
	r = requests.get(src, stream = True, allow_redirects=True)
	filename = src.split("/")[-1]
	path = '{}/{}'.format(folder, filename)
	if r.status_code == 200:
		r.raw.decode_content = True
		with open(path,'wb') as f:
			shutil.copyfileobj(r.raw, f)
		print('Image sucessfully Downloaded: ',filename)
	else:
		print('Image Couldn\'t be retreived')

def is_downloadable(src):
    """
    Does the src contain a downloadable resource
    """
    h = requests.head(src, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True