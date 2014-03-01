# This .py file use to handle the robots.txt of a website

import urllib.request
import re


# visit the website and get robots.txt
def get_robots_txt(website):	
	robots_txt_addr = website + 'robots.txt'
	req = urllib.request.Request(url=robots_txt_addr)
	response = urllib.request.urlopen(req)
	txt = response.read().decode("utf-8")	
	#print("Get robots.txt")
	return txt

# disallow array
disallow_array = []
# allow array
allow_array = []

# handle the robots.txt content using regular expression
def re_process(robots_txt):
	# robots.txt format
	#
	# User-agent:
	# Disallow:
	# Allow:
	disallow_match = re.compile(r'^Disallow: (.*)$')
	allow_match = re.compile(r'^Allow: (.*)$')


	# r return two array of disallow and allow


# the main function
if __name__ == '__main__':

	website = 'http://share.dmhy.org/'
	
	robots_txt = get_robots_txt(website);
	print(robots_txt)

