# coding=utf-8
import requests
import urllib
import pandas as pd
import psycopg2
import sys
from bs4 import BeautifulSoup
import pprint
from matplotlib import pyplot as plt
from html5print import HTMLBeautifier
import re

pp = pprint.PrettyPrinter()
f=open('chart.htm', 'r')
htmldata = f.read()
soup = BeautifulSoup(htmldata, "html5lib")
#tags_a=[]
links=[]
for tag_a in soup.findAll('a',attrs={"href" : re.compile("^20")}):
    links.append(tag_a['href'])
#print pp.pprint(tags_a)
l_df=pd.DataFrame(links)
l_df.columns=['link']
valueslist=l_df['link'].str.replace('.html','')
values=valueslist.str.split('-')
tvalues=zip(*values)
l_df['date']=pd.to_datetime(tvalues[0])
l_df['gender']=tvalues[1]
l_df['tournament']=tvalues[2]
l_df['stage']=tvalues[3]
l_df['player1']=tvalues[4]
l_df['player2']=tvalues[5]
#print pp.pprint(zip(*values))
#print l_df
#url='http://tennisabstract.com/charting/'+l_df['link'][1]
#response = requests.get(url)
#l_data = response.content
#soup2 = BeautifulSoup(l_data, "html5lib")
#data=[]
#for tag_span in soup2.findAll('table'):
#    data.append(tag_span)
#print pp.pprint(data)

#Define our connection string
conn_string = "host='localhost' dbname='db4ds' user='postgres' password='R1a9f9a2'"
# print the connection string we will use to connect
# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

	# execute our Query
cursor.execute("SELECT * FROM train.test_tab")

	# retrieve the records from the database
records = cursor.fetchall()

	# print out the records using pretty print
	# note that the NAMES of the columns are not shown, instead just indexes.
	# for most people this isn't very useful so we'll show you how to return
	# columns as a dictionary (hash) in the next example.
pprint.pprint(records)

#print soup.prettify().encode('UTF-8')
