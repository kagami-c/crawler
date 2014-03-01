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
# the two array initialize in re_processs

# handle the robots.txt content using regular expression
def re_process(robots_txt):
	# robots.txt format
	#
	# User-agent:
	# Disallow:
	# Allow:
	disallow_match = re.compile(r'^Disallow: (.*)$')
	allow_match = re.compile(r'^Allow: (.*)$')

	del_r = re.compile(r'\r')
	lines = robots_txt.split('\n')
	for each in lines:
		# delete \r
		each = del_r.sub('', each)

		#print(each)

		if disallow_match.match(each):
			disallow_array.append(disallow_match.sub(r'\1', each))
			#print('match disallow')

		if allow_match.match(each):
			allow_array.append(allow_match.sub(r'\1', each))
			#print('match allow')

	# return two array of disallow and allow


# the main function
if __name__ == '__main__':

	website = 'http://share.dmhy.org/'
	
	robots_txt = get_robots_txt(website);
	print(robots_txt)

	re_process(robots_txt)

	print(disallow_array)
	print(allow_array)

# this file deal with robots.txt just in an easy way
# and can get two array of disallow and allow 
# which can be used in other file