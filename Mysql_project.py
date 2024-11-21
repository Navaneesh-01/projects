#-----------------Creating DataBase-------------------#

# import mysql.connector

# db = mysql.connector.connect(host="localhost",user="navaneesh",password="nana@111",port="3307")

# c = db.cursor()

# query = "create database book_store"

# c.execute(query)

# print("Database is created")



#-----------------Creating Table------------------#

import mysql.connector
import datetime as dt

db = mysql.connector.connect(host="localhost",user="navaneesh",password="nana@111",port="3307",database="book_store")

c = db.cursor()

# query = """create table book_details(book_code int primary key auto_increment,
# book_name varchar(20),
# Author_name varchar(20),
# category varchar(20),
# publish_year year,
# book_price int,
# cur_book_count int)auto_increment = 1000"""

# c.execute(query)

# print("Table is created")


#-------------------Inserting Values into Table-------------------#


# a = "yes"

# while a == "yes":
#  query = """insert into book_details(book_name,Author_name,category,publish_year,book_price,cur_book_count)
#  values(%s,%s,%s,%s,%s,%s)"""
 
#  d1 = input("Book_Name :")
#  d2 = input("Author_Name :")
#  d3 = input("category :")
#  d4 = int(input("Book_publish_year :"))
#  d5 = int(input("Book_price :"))
#  d6 = int(input("current_book_count:"))
 
#  val = (d1,d2,d3,d4,d5,d6)
 
#  c.execute(query,val)
 
#  db.commit()
 
#  a = input("Are You Want To Insert Again?").lower()


#----------------create second Table--------------------

# query = """create table sales_details(sale_id int primary key auto_increment,
# book_code int,
# num_of_sold_books int,
# book_price int,
# sale_date date,
# Total_amount int,foreign key(book_code)references book_details (book_code))auto_increment=55"""

# c.execute(query)

# print("Table is created")


#-------------Values inserting in second table--------------#

b = "yes"

while b == "yes":
    
    query = """insert into sales_details(book_code,num_of_sold_books,book_price,sale_date,Total_amount)
    values(%s,%s,%s,%s,%s)"""
    
    d1 = int(input("book_code :"))
    
    query2 = "select book_price,cur_book_count from book_details where book_code=%s"
    
    val2 = (d1,)
    
    c.execute(query2,val2)
    
    data = c.fetchone()
    
    d2 = int(input("num_of_sold_books :"))
    d3 = data[0]
    d4 = dt.datetime.now()
    d5 = d2 * d3
    
    if data[1] >= d2:
        d6 = data[1] - d2
        
    else:
        print("Not enough books....") 
        break  
        
    val = (d1,d2,d3,d4,d5)     
    c.execute(query,val)
    
    
    query3 = """update book_details set cur_book_count = %s where book_code = %s"""
    
    val3 = (d6,d1)
    
    c.execute(query3,val3)
    
    db.commit()
    
    b = input("wamt to continue?").lower()