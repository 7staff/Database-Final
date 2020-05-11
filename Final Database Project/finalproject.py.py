#import mysql connector and pygal
import mysql.connector
import pymongo
import pygal
import json
import datetime
from datetime import datetime
from decimal import *
##################### SETUP  DATABASE CONNECTIONS ###############

#connect to your mysql datbase
mydb = mysql.connector.connect(
  host="localhost",
  user="stevencoll",
  passwd="!St3v3n19",
  database="classicmodels"
)

#connect to the mongo database
mongo_client = pymongo.MongoClient(host = "mongodb://localhost:27017/",
serverSelectionTimeoutMS = 3000,
username="mongosrc4gb",
password='!St3v3n19')

#Select mongo datacbase and collections
mongo_db = mongo_client["finalproject"]
employee_collection = mongo_db["employees"]

#The cursor will execute queries on your MySql Datbase
mycursor = mydb.cursor()

################# QUERIES TO POPULATE EMPLOYEE COLLECTION  ####################

#sql query generates a list of managers. People who have other employees report to them
sql_query = '''select employeeNumber, firstName, lastName
from employees
where employeeNumber IN (select reportsTo from employees);'''

#Execute the query
mycursor.execute(sql_query)

#Get the query result
query_result = mycursor.fetchall()

#Create managers dictionary
managers = {}

'''query_result is a list of tuples. The loop below converts the list of tuples into
a dictionary where the dictionary key is the employeeNumber and the value is the 
first and last name'''
for result in query_result:
    managers[result[0]] = result[1] + " " + result[2]

#Select all data from the employees and offices tables
sql_query = '''SELECT *
FROM employees e, offices o
WHERE e.officeCode = o.officeCode;'''

#Execute the query
mycursor.execute(sql_query)

#Get the query results
query_result = mycursor.fetchall()

#################### WRITE DOCUMENTS TO INSERT INTO EMPLOYEE COLLECTIONS ################

#list to store employee documents
employees = []
#loop through tuples in query_result. Write data to json format to store in our json file
for record in query_result:
    office_document = {
    "officeCode": record[8],
    "city": record[9],
    "phone": record[10],
    "addressLine1": record[11],
    "addressLine2": record[12],
    "state": record[13],
    "country" : record[14],
    "postalCode": record[15],
    "territory": record[16]
    }
    
    '''for employees who don't report to anyone, set the reportsTo value to N/A
    for other employees with a manager get the manager name from the managers dictionary
    using the the employeeNumber as the dictionary key'''
    if record[6] == None:
        manager = "N/A"
    else:
        manager = managers[int(record[6])]

    employee_document = {
    "_id": record[0],
    "lastName": record[1],
    "firstName": record[2],
    "extension": record[3],
    "email": record[4],
    "reportsTo": manager,
    "jobTitle": record[7],
    "office": office_document
    }
    employees.append(employee_document)

#insert employee documents into the employees collection in the mongo database
employee_collection.drop()
employee_collection.insert_many(employees)

#write to mongo formated data to a json file
json_file = open("employees.json", "w") #open the file
json_file.write("[\n") #write the opening bracket forthe list
counter = 1 #use counter to determine id the last document is being written

#loop through the list of employee documents
for employee_doc in employees:
    json_file.write(json.dumps(employee_doc)) #convert a python dictionary to a json object
    #write a comma after the document if it is not the last in the list
    if counter != len(employees):
        json_file.write(",\n")
        counter += 1
    else: #don't write a comma after the document if it is the last in the list
        json_file.write("\n")

json_file.write("]\n")
json_file.close()

print("\nScript executed successfully")
########################################





###################################




#Select mongo datacbase and collections
mongo_db = mongo_client["finalproject"]
products_collection = mongo_db["products"]

#The cursor will execute queries on your MySql Datbase
mycursor = mydb.cursor()

################# QUERIES TO POPULATE EMPLOYEE COLLECTION  ####################

#Select all data from the employees and offices tables
sql_query = '''SELECT *
FROM products a, productlines l
WHERE a.productline = l.productline;'''

#Execute the query
mycursor.execute(sql_query)

#Get the query results
query_result = mycursor.fetchall()

#################### WRITE DOCUMENTS TO INSERT INTO EMPLOYEE COLLECTIONS ################

#list to store employee documents
products = []
#loop through tuples in query_result. Write data to json format to store in our json file
for record in query_result:
    productLine_document = {
    "line": record[9],
    "textDescription": record[10],
    "htmlDescription": record[11],
    "image": record[12],
    
    }
    

    products_document = {
    "_id": record[0],
    "productName": record[1],
    "productScale": record[2],
    "productVendor": record[3],
    "productDescription": record[4],
    "quantityInStock": record[5],
    "buyPrice": record[6],
    "MSRP": record[7],
    "productLine": productLine_document
    }
    products.append(products_document)

#insert employee documents into the employees collection in the mongo database
products_collection.drop()
products_collection.insert_many(products)

#write to mongo formated data to a json file
json_file = open("products.json", "w") #open the file
json_file.write("[\n") #write the opening bracket forthe list
counter = 1 #use counter to determine id the last document is being written

#loop through the list of employee documents
for products_doc in products:
    json_file.write(json.dumps(products_doc)) #convert a python dictionary to a json object
    #write a comma after the document if it is not the last in the list
    if counter != len(products):
        json_file.write(",\n")
        counter += 1
    else: #don't write a comma after the document if it is the last in the list
        json_file.write("\n")

json_file.write("]\n")
json_file.close()

print("\nScript executed successfully")

######################################################











#Select mongo datacbase and collections
mongo_db = mongo_client["finalproject"]
employee_collection = mongo_db["orders"]

#The cursor will execute queries on your MySql Datbase
mycursor = mydb.cursor()

################# QUERIES TO POPULATE EMPLOYEE COLLECTION  ####################

#sql query generates a list of managers. People who have other employees report to them
sql_query = '''select customerNumber, contactFirstName, contactLastName
from customers;'''

#Execute the query
mycursor.execute(sql_query)

#Get the query result
query_result = mycursor.fetchall()

#Create managers dictionary
customerName = {}

'''query_result is a list of tuples. The loop below converts the list of tuples into
a dictionary where the dictionary key is the employeeNumber and the value is the 
first and last name'''
for result in query_result:
    customerName[result[0]] = result[3] + " " + result[2]




#sql query generates a list of managers. People who have other employees report to them
sql_query = '''select productName
from products;'''

#Execute the query
mycursor.execute(sql_query)

#Get the query result
query_result = mycursor.fetchall()

#Create managers dictionary
productName = {}

'''query_result is a list of tuples. The loop below converts the list of tuples into
a dictionary where the dictionary key is the employeeNumber and the value is the 
first and last name'''
for result in query_result:
    productName[result[1]]

#sql query generates a list of managers. People who have other employees report to them

#sql query generates a list of managers. People who have other employees report to them
sql_query = '''select employeeNumber, lastName, firstName
from employee;'''

#Execute the query
mycursor.execute(sql_query)

#Get the query result
query_result = mycursor.fetchall()

#Create managers dictionary
employeeName = {}

'''query_result is a list of tuples. The loop below converts the list of tuples into
a dictionary where the dictionary key is the employeeNumber and the value is the 
first and last name'''
for result in query_result:
    customerName[result[0]] = result[1] + " " + result[2]



#Select all data from the employees and offices tables
sql_query = '''SELECT *
FROM orders a, orderdetails b
WHERE a.orderNumber. = b.orderNumber;'''

#Execute the query
mycursor.execute(sql_query)

#Get the query results
query_result = mycursor.fetchall()

#################### WRITE DOCUMENTS TO INSERT INTO EMPLOYEE COLLECTIONS ################

#list to store employee documents
orders = []
#loop through tuples in query_result. Write data to json format to store in our json file
for record in query_result:
    orderdetails_document = {
    "productName": productName,
    "quantityOrdered": record[9],
    "priceEach": record[10],
    }
    
  

    orders_document = {
    "_id": record[0],
    "orderDate": record[1],
    "requiredDate": record[2],
    "shippedDate": record[3],
    "status": record[4],
    "comments": record[5],
    "customerName": customerName,
    "employeeName": employeeName,
    "orderDetails": orderdetails_document
    }
    orders.append(orders_document)

#insert employee documents into the employees collection in the mongo database
orders_collection.drop()
orders_collection.insert_many(employees)

#write to mongo formated data to a json file
json_file = open("orders.json", "w") #open the file
json_file.write("[\n") #write the opening bracket forthe list
counter = 1 #use counter to determine id the last document is being written

#loop through the list of employee documents
for orders_doc in employees:
    json_file.write(json.dumps(orders_doc)) #convert a python dictionary to a json object
    #write a comma after the document if it is not the last in the list
    if counter != len(orders):
        json_file.write(",\n")
        counter += 1
    else: #don't write a comma after the document if it is the last in the list
        json_file.write("\n")

json_file.write("]\n")
json_file.close()

print("\nScript executed successfully")
