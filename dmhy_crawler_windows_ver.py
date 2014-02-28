import urllib.request, urllib.error, urllib.parse
import time
import re
import codecs

def get_page(webaddr):
	headers = {  
		'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
	}
	req = urllib.request.Request(url=webaddr, headers=headers)
	response = urllib.request.urlopen(req)
	page = response.read().decode("utf-8")

	return page

def get_tbody(page):
	delete_newline = re.compile(r"\n")
	delte_return = re.compile(r"\r")
	match_tbody = re.compile(r".*<tbody>(.*)</tbody>.*")

	line1 = delete_newline.sub(r' ', page)
	line2 = delte_return.sub(r' ', line1)
	tbody = match_tbody.sub(r'\1', line2)
	
	return tbody

def get_tr_s(tbody):
	array = tbody.split(r'</tr>')
	array.pop()
	#for x in array:
	#	print '!!!\n' + x + '\n'
	return array

def get_title(tr_s):
	tag = re.compile(r'.*<td class="title">(.*?)</td>.*')
	title_array = []
	for each in tr_s:
		title_array.append(tag.sub(r'\1', each))

	#for x in title_array:
	#	print '!!!' + x + '\n'
	return title_array

def get_href(title_array):
	get_a = re.compile(r'.*(<a href.*?</a>).*?$')
	add_addr = re.compile(r'href="')
	ref_array = []
	for each in title_array:
		temp = get_a.sub(r'\1', each)
		ref_array.append(add_addr.sub(r'href="http://share.dmhy.org', temp))

	#for x in ref_array:
	#	print x + '\n'
	return ref_array

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

	start = 1
	increment = 1
	#end = 142
	end = 1 # just for test
	
	base = 'http://share.dmhy.org/topics/list/page/'

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
	print('Program ends.')

#my = FirstParser()
#my.feed(page)
#print my.getresult()
#
#for name, value in attrs:
#	if name == 'href':
#		print value
#
# http://share.dmhy.org/topics/list/page/1
# webaddr format!

# the next thing to do is to parse the robots.txt file