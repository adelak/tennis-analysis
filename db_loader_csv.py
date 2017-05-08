# coding=utf-8
import psycopg2
import csv
import sqlalchemy
#import pprint
import pandas as pd
import glob

def analyzeCSV(p_filepath):
    l_csv=open(p_filepath, 'rb')
    l_text=csv.reader(l_csv, delimiter=',')
    l_max_columns=0
    for row in l_text:
        if l_max_columns<len(row):
            l_max_columns=len(row)
    for i_row in range(0,len(l_text)):
        while len(l_text[i_row])<l_max_columns:
            l_text[i_row].extend('')

def fixCSV(p_filepath):
    l_data=''

#conn_string = "host='localhost' dbname='db4ds' user='postgres' password='R1a9f9a2'"
#conn = psycopg2.connect(conn_string)
#cursor = conn.cursor()
#?client_encoding=utf8
conn_string='postgresql://postgres:R1a9f9a2@localhost:5432/db4ds'
engine = sqlalchemy.create_engine(conn_string)
filepaths=glob.glob("data/matchchart/*.csv")
for filepath in filepaths:
    analyzeCSV(filepath)
    break
#    filename = "'"+filepath+"'" #[:filepath.rindex('.')]
#    tablename=filepath[filepath.index('g')+2:filepath.rindex('.')].replace('-','_').lower()
#    print tablename+' upload'
#    df = pd.read_csv(filepath,sep=',',encoding="latin-1") #latin-1 ,quoting=csv.QUOTE_NONE,quotechar='"'
#    df.columns = [c.lower() for c in df.columns]
#    if tablename=='m_stats_keypointsreturn':
#        'm_stats_shotdiroutcomes'
#        print df
#   print "'"+filepath+"'"ы
#   print filename
#   'data/matchchart/charting-w-stats-ShotTypes'
#   'data/matchchart/charting-m-matches.csv'
#    df.to_sql(name=tablename, schema='tennis', con=engine, if_exists='replace', index=False)
#    print tablename+' upload
