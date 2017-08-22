import requests, json

url='https://mp3zing.download/api?key=QFopqEX1hjMN&url='
def getlink(link):
	html=requests.get(url+link).text
	response=json.loads(html)
	
	data1=response["lossless"]
	data2=response["link320"]
	data3=response["link128"]

	print 'Link lossless: '+data1

	print '-------------------------------------------------------'
	
	print 'Link 320: '+data2

	print '-------------------------------------------------------'

	print 'Link 128: '+data3

	print '-------------------------------------------------------'
	

	

link=raw_input('Nhap link: ')
getlink(link)




