import sqlite3

connect = sqlite3.connect('books.sqlite') #creating the database

cursor = connect.cursor() # creating a cursor Object to be able to execute sql statements on the database

# creating the table variable
sql_query = """ CREATE TABLE books (
    id integer PRIMARY KEY,
    author text NOT NULL,
    language text NOT NULL,
    title text NOT NULL
)"""