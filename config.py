import psycopg2 as pg

conn = pg.connect(host="localhost",port = 5432 , user="postgres", password="123456", dbname="company_db")