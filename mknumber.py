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

def writeData(dataStr,nowtime):
	
	FileW = open(str(nowtime)+'_data'+'.dic','a')

	FileW.write(dataStr+ '\n')
	FileW.close()

def mkData(dataLines,dataFormat,limitNumber,linestr,nowtime):
	if ':' in linestr:
	    lineL=linestr.split(":")
	if dataFormat=='NameNumS' or dataFormat=='NameNumL':
		if dataFormat=='NameNumS':
			numList=['123','321','111','666','888']
		else:
			numList=['123','321','111','666','888','1234','12345','1111','11111','4321','666666','888888','112233','123123']
		try:
			count=0
			for datastr in dataLines:
				for num in numList:
					if limitNumber!=0 and count<limitNumber:
					
						data=datastr.replace('\n','')+num.replace('\n','')
						if len(data)<int(lineL[1]) and len(data)>int(lineL[0]):
							writeData(data,nowtime)
					elif limitNumber==0:
					
						data=datastr.replace('\n','')+num.replace('\n','')
						if len(data)<int(lineL[1]) and len(data)>int(lineL[0]):
							writeData(data,nowtime)
					count=count+1
					data=''
					
		except Exception as e:
			print(e)
			print('报错。。1')
	 


if __name__ == '__main__':

	print('''
		****************************************************
		*          ecshop getshell(user.php-rce)           *
		*				      Coded by Lroot *
		****************************************************
		''')
	
	parser = optparse.OptionParser('python %prog ' +'-h (manual)',version='%prog v1.0')
	parser.add_option('-i', dest='InputFile', type='string', help='输入元数据文件')

	parser.add_option('-f', dest='FormatData', type ='string', help='数据格式')
	parser.add_option('-m', dest='Max',  default=0,type ='int', help='最多输出xx条数据')
	parser.add_option('-l', dest='Lines', type ='string', help='输出数据最小长度和最大长度')
	
	
	
	(options, args) = parser.parse_args()
	
	
	InputFile = options.InputFile
	FormatData = options.FormatData
	Max = options.Max
	Lines = options.Lines
	

	if InputFile!='' and FormatData!='':
		
		InputData = open(InputFile, mode='r', buffering=-1, encoding=None)
		print(Max)
		nowtime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
		print('数据文件：'+str(nowtime)+'_data'+'.dic')
		mkData(InputData,FormatData,Max,Lines,nowtime)


			
		

