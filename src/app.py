#Librerias

import sqlite3
import pandas as pd

#CCONECTAMOS EL DB

con = sqlite3.connect("exercise.db")

#CREAMOS EL CURSOR

c = con.cursor()

#CREAMOS LAS TABLAS

#c.execute('''DROP TABLE publishers''')

#c.execute('''CREATE TABLE publishers(
#                id_publisher INT NOT NULL,
#                name VARCHAR(255) NOT NULL,
#                PRIMARY KEY(id_publisher)
#);''')

#c.execute('''CREATE TABLE authors(
#                id_author INT NOT NULL,
#                first_name VARCHAR(100) NOT NULL,
#                middle_name VARCHAR(100) NULL,
#                last_name VARCHAR(100) NULL,
#               PRIMARY KEY(id_author)
#);''')

#c.execute('''CREATE TABLE books(
#                id_book INT NOT NULL,
#                title VARCHAR(255) NOT NULL,
#                total_pages INT NULL,
#                rating DECIMAL(4, 2) NULL,
#                isbn VARCHAR(13) NULL,
#                published_date DATE,
#                id_publisher INT NULL,
#                PRIMARY KEY(id_book),
#                CONSTRAINT fk_publisher FOREIGN KEY(id_publisher) REFERENCES publishers(id_publisher)
#);''')

#c.execute('''CREATE TABLE book_authors(
#                id_book INT NOT NULL,
#                id_author INT NOT NULL,
#                PRIMARY KEY(id_book, id_author),
#                CONSTRAINT fk_book FOREIGN KEY(id_book) REFERENCES books(id_book) ON DELETE CASCADE,
#                CONSTRAINT fk_author FOREIGN KEY(id_author) REFERENCES authors(id_author) ON DELETE CASCADE
#);''')

#INSERTAMOS LOS DATOS

data_publisher = [(1, "O Reilly Media"),(2, "A Book Apart"), (3, "A K PETERS"), (4, "Academi Press"), (5, "Addison Wesley"), (6, "Albert&Sweigart"),(7, "Alfred A. Knopf")]
#c.executemany("INSERT INTO publishers(id_publisher, name) VALUES (?, ?);", data_publisher)

data_author = [(1, "Merritt","", "Eric"), (2, "Linda","", "Mui"), (3, "Alecos","", "Papadatos"), (4, "Anthony", "", "Molinaro"), (5, "David", "", "Cronin"), (6, "Richard", "", "Blum"), (7, "Yuval", "Noah", "Harari"), (8, "Paul", "", "Albitz")] 
#c.executemany("INSERT INTO authors(id_author, first_name, middle_name, last_name) VALUES (?,?,?,?);", data_author)

data_books = [(1, "Lean Software Development: An Agile Toolkit", 240, 4.17, "9780320000000", "2003-05-18", 5), (2, "Facing the Intelligence Explosion", 91, 3.87, "", "2013-02-01", 7), (3, "Scala in Action", 419, 3.74, "9781940000000", "2013-04-10", 1), (4, "Patterns of Software: Tales from the Software Community", 256, 3.84, "9780200000000", "1996-08-15", 1), (5, "Anatomy Of LISP", 446, 4.43, "9780070000000", "1978-01-01", 3), (6, "Computing machinery and intelligence", 24, 4.17, "", "2009-03-22", 4), (7, "XML: Visual QuickStart Guide", 269, 3.66, "9780320000000", "2009-01-01", 5), (8, "SQL Cookbook", 595, 3.95, "9780600000000", "2005-12-01", 7), (9, "The Apollo Guidance Computer: Architecture And Operation (Springer Praxis Books / Space Exploration)", 439, 4.29, "9781440000000", "2010-07-01", 6), (10, "Minds and Computers: An Introduction to the Philosophy of Artificial Intelligence", 222, 3.54, "9780750000000", "2007-02-13", 7) ]
#c.executemany("INSERT INTO books(id_book, title, total_pages, rating, isbn, published_date, id_publisher) VALUES (?,?,?,?,?,?,?);", data_books)

data_bookauthors = [(1, 1), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 4), (10, 1)]
#c.executemany("INSERT INTO book_authors(id_book, id_author) VALUES (?,?);", data_bookauthors)

con.commit() #No olvidarse del Commit o no va a actualizar en la vida

#IMPRIMIMOS UNA TABLA COMO UN DF

publisher_df = pd.read_sql_query("SELECT * FROM publishers;", con, index_col="id_publisher")

print (publisher_df)