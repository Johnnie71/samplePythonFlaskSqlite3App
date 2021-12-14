import sqlite3

connect = sqlite3.connect('books.sqlite') #creating the database

cursor = connect.cursor() # creating a cursor to be able to execute sql statements on the database