#!/usr/bin/env python3
''' news report analysis
    author: Lai Man Tang(Nancy) 
    email: cloudtang030@gmail.com
'''

from newsdb import popular_articles, popular_authors, request_error
import datetime



def main():
	op = open('newsreport' +'.txt', 'w')
	op.write( '\nNew Report -- '+ str(datetime.datetime.now()))
	op.write( '\n\nthe most popular three articles of all time\n\n')
	result = popular_articles()
	count = 1
	for text in result:
		s = str(count) + ': ' +text[0] + '---' + str(text[1]) + " views\n"
		op.write(s)
		count +=1
	
	op.write( '\n\nthe most popular article authors of all time\n\n')
	result = popular_authors()
	count = 1
	for text in result:
		s = str(count) + ': ' +text[0] + '---' + str(text[1]) + " views\n"
		op.write(s)
		count +=1
	
	op.write( '\n\nthe day that has more than 1% of requests lead to errors\n')
	result = request_error()
	count = 1
	for text in result:
		p2 = float(text[2])
		p1 = p2/float(text[1])*100
		if p1 > 1:
			s = str(count) + ': ' + str(text[0]) + '---'  + " "+str(p1)+"%\n\n"
			op.write(s)
			count +=1
	
	op.close()
	
	
	
if __name__ == '__main__':
	main()
