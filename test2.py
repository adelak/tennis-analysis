# coding=utf-8
import psycopg2
import csv
import sqlalchemy
#import pprint
import pandas as pd
import glob

#conn_string = "host='localhost' dbname='db4ds' user='postgres' password='R1a9f9a2'"
#conn = psycopg2.connect(conn_string)
#cursor = conn.cursor()
#?client_encoding=utf8
conn_string='postgresql://postgres:R1a9f9a2@localhost:5432/db4ds'
engine = sqlalchemy.create_engine(conn_string)
filepaths=glob.glob("data/matchchart/*.csv")
for filepath in filepaths:
    #filename = "'"+filepath+"'" #[:filepath.rindex('.')]
    df = pd.read_csv(filepath,sep=',',quoting=csv.QUOTE_NONE,quotechar='"',encoding="latin-1")
    df.columns = [c.lower() for c in df.columns]
    tablename=filepath[filepath.index('g')+2:filepath.rindex('.')]
#   print "'"+filepath+"'"
#   print filename
#   'data/matchchart/charting-w-stats-ShotTypes'
#   'data/matchchart/charting-m-matches.csv'
    df.to_sql(name=tablename, schema='tennis', con=engine, if_exists='replace', index=False)
