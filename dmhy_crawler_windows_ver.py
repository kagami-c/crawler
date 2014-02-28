import urllib.request, urllib.error, urllib.parse
import time
import re
import codecs


# this method is the most time-comsuming part
def get_page(webaddr):
	headers = {  
		'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
	}
	req = urllib.request.Request(url=webaddr, headers=headers)
	response = urllib.request.urlopen(req)
	# read method is the slowest part
	page = response.read().decode("utf-8")	
	return page


# get_tbody regular expression
delete_newline = re.compile(r"\n")
delte_return = re.compile(r"\r")
match_tbody = re.compile(r".*<tbody>(.*)</tbody>.*")
# get_tbody function
def get_tbody(page):
	line1 = delete_newline.sub(r' ', page)
	line2 = delte_return.sub(r' ', line1)
	tbody = match_tbody.sub(r'\1', line2)	
	return tbody


def get_tr_s(tbody):
	array = tbody.split(r'</tr>')
	array.pop()
	return array


# get_title regular expression
tag = re.compile(r'.*<td class="title">(.*?)</td>.*')
# get_title function
def get_title(tr_s):
	title_array = []
	for each in tr_s:
		title_array.append(tag.sub(r'\1', each))
	return title_array


# get_href regular expression
get_a = re.compile(r'.*(<a href.*?</a>).*?$')
add_addr = re.compile(r'href="')
# get_href function
def get_href(title_array):
	ref_array = []
	for each in title_array:
		temp = get_a.sub(r'\1', each)
		ref_array.append(add_addr.sub(r'href="http://share.dmhy.org', temp))
	return ref_array


# the main proc
if __name__ == '__main__':
		
	htmlfile = codecs.open('htmlfile.html', 'w', 'utf-8')
	htmlfile.write('''<!DOCTYPE html>
<html>
<head>
	<title>htmlfile</title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
''')

	# the start and end page number
	start = 1
	increment = 1
	end = 23
	#end = 1 # just for test
	
	# the base address
	base = 'http://share.dmhy.org/topics/list/sort_id/2/page/'

	# content of share.dmhy.org/robots.txt below
	#
	# User-agent: *
	# Disallow: /topics/down/
	# Disallow: /index.php/topics/down/
	# Allow: /

	while(start <= end):
		
		webaddr = base + str(start)
		print('visiting: ' + webaddr)
		
		page = get_page(webaddr)
		tbody = get_tbody(page)
		tr_s = get_tr_s(tbody)
		title_array = get_title(tr_s)
		ref_array = get_href(title_array)

		for s in ref_array:
			htmlfile.write(s + '<br />\n\r')

		time.sleep(0.1)
		start += increment

	htmlfile.write('</body>\n</html>')
	htmlfile.close()
	print('Program ends.')

# the next thing to do is to parse the robots.txt file