#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import csv

#con = None
#tb_name='Products2'
#s = "CREATE TABLE %tb_name(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)"
#try:
#    con = psycopg2.connect("host='ec2-54-204-18-53.compute-1.amazonaws.com' dbname='d76ovoqurvj86c' user='etuzviajytaszz' password='2f9b837145b2cdde0aac43fc36f728dc44e869e36b53acffede3e41aec489999'")
#    cur = con.cursor()
#    cur.execute("CREATE TABLE Products2(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)")
#    for i in range(1, 10):
#        cur.execute("INSERT INTO "+ tb_name+ " VALUES("+str(i)+",'Milk',5)")
#    cur.execute("INSERT INTO Products2 VALUES(2,'Sugar',7)")
#    cur.execute("INSERT INTO Products2 VALUES(3,'Coffee',3)")
#    cur.execute("INSERT INTO Products2 VALUES(4,'Bread',5)")
#    cur.execute("INSERT INTO Products2 VALUES(5,'Oranges',3)")
#    con.commit()
#except psycopg2.DatabaseError as e:
#    if con:
#        con.rollback()
#
#    print ('Error %s' % e)
#    sys.exit(1)
#
#finally:
#    if con:
#        con.close()



#with open('books.csv', newline='') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
#    for row in spamreader:
#        print(', '.join(row))
with open('books.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    con = None
#    tb_name='test'
#    s = "CREATE TABLE %tb_name(Id INTEGER PRIMARY KEY, Name VARCHAR(20), Price INT)"
    try:
        con = psycopg2.connect("host='ec2-54-204-18-53.compute-1.amazonaws.com' dbname='d76ovoqurvj86c' user='etuzviajytaszz' password='2f9b837145b2cdde0aac43fc36f728dc44e869e36b53acffede3e41aec489999'")
        cur = con.cursor()
        cur.execute("CREATE TABLE books(Id INTEGER PRIMARY KEY, ISBN VARCHAR(10), Title VARCHAR(30), Author VARCHAR(30), Year INTEGER)")
        i=0
        for row in reader:
            i=i+1
            cur.execute("INSERT INTO books VALUES("+str(i)+",'"+row['isbn']+"','"+row['title'].replace("'", "''")+"','"+row['author'].replace("'", "''")+"',"+row['year']+")")
            print(row['isbn'], row['title'], row['author'], row['year'])

        con.commit()
    except psycopg2.DatabaseError as e:
        if con:
            con.rollback()

        print ('Error %s' % e)
        sys.exit(1)

    finally:
        if con:
            con.close()
