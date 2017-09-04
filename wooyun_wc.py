#coding:utf-8
#Author:LSA
#Description:wordcloud for wooyun
#Date:20170904



import urllib
import urllib2
import re
import threading
import Queue


q0 = Queue.Queue()

threads = 20

threadList = []


def gettitle():
	while not q0.empty():

		i = q0.get()
		url = 'http://wy.hxsec.com/bugs.php?page=' + str(i)
		html = urllib.urlopen(url).read()
		reg = re.compile(r'<li  style="width:60%;height:25px;background-color:#FFFFFF;float:left" ><a href=".*?">(.*?)</a>')
		titleList = re.findall(reg,html)
		fwy = open("wooyunBugTitle.txt","a")
		for title in titleList:
			fwy.write(title+'\n')
		fwy.flush()
		fwy.close()
		print 'Page ' + str(i) + ' over!'


def main():
	for page in range(1,2962):
		q0.put(page)
	for thread in range(threads):
		t = threading.Thread(target=gettitle)
		t.start()
		threadList.append(t)
	for th in threadList:
		th.join()

	print '***********************All pages over!**********************'
		



if __name__ == '__main__':
	main()

			