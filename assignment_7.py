import psycopg2

def create_table():

    connect = psycopg2.connect(dbname = "postgres", user = "postgres", password = "Kunal@2007", host = "localhost", port = "5433")

    cursor = connect.cursor()
    

    cursor.execute('''create table students(Name Text, URN varchar, Age int);''')
    
    
    print("Table Created Successfully")
    connect.commit()
    connect.close()

create_table()

def insert_records():

    connect = psycopg2.connect(dbname = "postgres", user = "postgres", password = "Kunal@2007", host = "localhost", port = "5433")
    cursor = connect.cursor()

    cursor.execute('''insert into students(Name, URN, Age) values('John Doe',200,20);''')

    print("Data added successfully.")
    connect.commit()
    connect.close()

insert_records()

def extract_records():
    connect = psycopg2.connect(dbname = "postgres",user = "postgres", password = "Kunal@2007", host = "localhost", port = "5433" )
    cursor = connect.cursor()
    cursor.execute('''select * from students;''')
    show = cursor.fetchone()
    print(show[0])
    print(show[1])
    print(show[2])

    print("Data extracted  successfully.")
    connect.commit()
    connect.close()

extract_records()

def user_input():

    connect = psycopg2.connect(dbname = "postgres", user = "postgres", password = "Kunal@2007", host = "localhost", port = "5433")
    cursor = connect.cursor()
    name = input("Enter the name: ")
    urn = input("Enter the URN: ")
    age = input("Enter the age: ")

    query = ('''insert into students(Name, URN, Age) values(%s,%s,%s);''')
    cursor.execute(query, (name, urn, age))

    print("UserData added successfully.")
    connect.commit()
    connect.close()

user_input()


def delete_records():
    connect = psycopg2.connect(dbname = "postgres", user = "postgres", password = "Kunal@2007", host = "localhost", port = "5433")      
    cursor = connect.cursor()
    
    cursor.execute('''TRUNCATE TABLE students;''')
    cursor.execute('''DROP TABLE students;''')

    print("Data deleted successfully.")
    connect.commit()    
    connect.close()

delete_records()