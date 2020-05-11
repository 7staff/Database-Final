#import mysql connector and pygal
import mysql.connector
import pygal

#connect to your datbase
mydb = mysql.connector.connect(
  host="localhost",
  user="stevencoll",
  passwd="!St3v3n19",
  database="classicmodels"
)

#The cursor will execute  queries on your MySql Datbase
mycursor = mydb.cursor()

#Create sql query. The backslash \  is a line continuation character and will allow the query to execute as one string
sql_query = '''SELECT e.firstName, e.lastName, COUNT(c.salesRepEmployeeNumber) AS "NumCustomers"
 FROM employees e, customers c
 WHERE e.employeeNumber = c.salesRepEmployeeNumber
 GROUP BY c.salesRepEmployeeNumber
 ORDER BY COUNT(c.salesRepEmployeeNumber) DESC;'''

#Execute the query
mycursor.execute(sql_query)

#Get the query result
query_result = mycursor.fetchall()

#Store results in lists
#Each record will be returned in the form of a tuple so we will need to access each tuple item
employee_names = []
number_of_customers = []

for record in query_result:
    employee_names.append(record[0] + " " + record[1]) #The first 2 items in the tuple are first and last names
    number_of_customers.append(record[2]) #the third item is the number of customers

#Export the data in a chart to an SVG file
bar_chart = pygal.Bar(x_label_rotation=45)
bar_chart.title = "Customers per Employee"
bar_chart.x_labels = map(str, employee_names) #set x axis labels to the employee names
bar_chart.add('Number of Customers', number_of_customers) # add number of customers
bar_chart.render_to_file('images/mod13_q1.svg') #render the chart to an SVG file

#If program is successful print this
print("Program executed successfully")

### Write your queries and create your charts below


mycursor = mydb.cursor()


sql_query = '''SELECT
  orderNumber,
  priceEach
FROM
  orderdetails
ORDER BY
  priceEach DESC
LIMIT
  10;
'''

mycursor.execute(sql_query)

query_result = mycursor.fetchall()


order_number = []
price_each = []

for record in query_result:
    order_number.append(record[0]) 
    price_each.append(record[1]) 


bar_chart = pygal.Bar(x_label_rotation=45)
bar_chart.title = "question 4"
bar_chart.x_labels = map(str, price_each) 
bar_chart.add('Top 10 expensive orders', order_number) 
bar_chart.render_to_file('images/mod13_q4.svg') 


print("Program executed successfully")

### Write your queries and create your charts below
mycursor = mydb.cursor()


sql_query = '''SELECT
  products.productName,
  COUNT(products.productName),
  products.productCode,
  orderdetails.quantityOrdered
FROM
  products
  INNER JOIN orderdetails ON products.productCode = orderdetails.productCode
GROUP BY
  products.productName, products.productCode, orderdetails.quantityordered
ORDER BY
  COUNT(products.productName)
LIMIT 10;
;
'''

mycursor.execute(sql_query)

query_result = mycursor.fetchall()


product_name = []
product_code = []

quantity = []

for record in query_result:
    product_name.append(record[3]) 
    product_code.append(record[0]) 
    quantity.append(record[3]) 


bar_chart = pygal.Bar(x_label_rotation=45)
bar_chart.title = "question 2"
bar_chart.x_labels = map(str, product_name) 
bar_chart.add('productName', quantity) 
bar_chart.render_to_file('images/mod13_q2.svg') 


print("Program executed successfully")

### Write your queries and create your charts below
sql_query = '''SELECT
  products.productCode, products.productName, orderdetails.priceEach
FROM
products
INNER JOIN orderdetails
ON products.productCode=orderdetails.productCode
ORDER BY orderdetails.priceEach
LIMIT
  10;
'''
ord_ = '''SELECT
*
FROM
orderdetails;
'''
mycursor.execute(sql_query)

query_result = mycursor.fetchall()


product_name = []
product_code = []


for record in query_result:
    product_name.append(record[1]) 
    product_code.append(record[0])

mycursor.execute(ord_)
query = mycursor.fetchall()
price = []

for record in query:
    price.append(record[3])

bar_chart = pygal.Bar(x_label_rotation=45)
bar_chart.title = "question 3"
bar_chart.x_labels = map(str, product_name) 
bar_chart.add('Top 10 highest dollar value', price) 
bar_chart.render_to_file('images/mod13_q3.svg') 


print("Program executed successfully")

### Write your queries and create your charts below
sql_query = '''SELECT c.customerName, c.customerNumber, COUNT(o.orderNumber) as "NumOrders"
 FROM customers c, orders o
 WHERE c.customerNumber = o.customerNumber
 GROUP BY c.customerNumber
 ORDER BY COUNT(o.orderNumber);'''

#Execute the query
mycursor.execute(sql_query)

#Get the query result
query_result = mycursor.fetchall()

#Store results in lists
#Each record will be returned in the form of a tuple so we will need to access each tuple item
employee_names = []
number_of_orders = []

for record in query_result:
    employee_names.append(record[0]) #The first 2 items in the tuple are first and last names
    number_of_orders.append(record[2]) #the third item is the number of customers

#Export the data in a chart to an SVG file
bar_chart = pygal.HorizontalBar(x_label_rotation=45)
bar_chart.title = "q5"
bar_chart.x_labels = map(str, employee_names) #set x axis labels to the employee names
bar_chart.add('Number of Orders', number_of_orders) # add number of customers
bar_chart.render_to_file('images/mod13_q5.svg') #render the chart to an SVG file

#If program is successful print this
print("Program executed successfully")

### Write your queries and create your charts below

sql_query = '''SELECT amount, YEAR(paymentDate)
 FROM payments
 ORDER BY YEAR(paymentDate);
 '''

#Execute the query
mycursor.execute(sql_query)

#Get the query result
query_result = mycursor.fetchall()

#Store results in lists
#Each record will be returned in the form of a tuple so we will need to access each tuple item
amount = []
year = []

for record in query_result:
    amount.append(record[0]) #The first 2 items in the tuple are first and last names
    year.append(record[1]) #the third item is the number of customers

#Export the data in a chart to an SVG file
bar_chart = pygal.Pie()
bar_chart.title = "q6"
bar_chart.add("Amount", amount) # add number of customers
bar_chart.x_labels = map(int, year)
bar_chart.render_to_file('images/mod13_q6.svg') #render the chart to an SVG file

#If program is successful print this
print("Program executed successfully")

### Write your queries and create your charts below

#The cursor will execute  queries on your MySql Datbase
mycursor = mydb.cursor()


sql_query = '''SELECT COUNT(checkNumber)
 FROM payments
 WHERE YEAR(paymentDate) = 2004
 GROUP BY MONTH(paymentDate);'''

#Execute the query
mycursor.execute(sql_query)

#Get the query result
query_result = mycursor.fetchall()

#Store results in lists
#Each record will be returned in the form of a tuple so we will need to access each tuple item
check= []
year = []
month = []

for record in query_result:
    check.append(record[0]) 
    year.append(record[0]) 
    month.append(record[0])
#Export the data in a chart to an SVG file
bar_chart = pygal.Bar(x_label_rotation=45)
bar_chart.title = "Question 7"
bar_chart.x_labels = map(str, range(1,13)) #set x axis labels to the employee names
bar_chart.add('Number of Payments', check) # add number of customers
bar_chart.render_to_file('images/mod13_q7.svg') #render the chart to an SVG file

#If program is successful print this
print("Program executed successfully")

mycursor = mydb.cursor()


sql_query = '''SELECT COUNT(checkNumber)
 FROM payments
 WHERE YEAR(paymentDate) = 2004 and MONTH(paymentDate) = 12
 GROUP BY DAY(paymentDate);'''

#Execute the query
mycursor.execute(sql_query)

#Get the query result
query_result = mycursor.fetchall()

#Store results in lists
#Each record will be returned in the form of a tuple so we will need to access each tuple item
check= []
year = []
month = []
day =[]

for record in query_result:
    check.append(record[0]) 
    year.append(record[0]) 
    month.append(record[0])
    day.append(record[0])

#Export the data in a chart to an SVG file
bar_chart = pygal.Line(x_label_rotation=45)
bar_chart.title = "Question 8"
bar_chart.x_labels = map(str, range(1, 32)) #set x axis labels to the employee names
bar_chart.add('Number of Payments', check) # add number of customers
bar_chart.render_to_file('images/mod13_q8.svg') #render the chart to an SVG file

#If program is successful print this
print("Program executed successfully")

### Write your queries and create your charts below

#The cursor will execute  queries on your MySql Datbase
mycursor = mydb.cursor()


sql_query = '''SELECT c.customerName, c.customerNumber, COUNT(p.customerNumber)
  FROM customers c, payments p
 WHERE c.customerNumber = p.customerNumber
  GROUP BY c.customerNumber DESC
  ORDER BY customerName
 LIMIT 10;'''

#Execute the query
mycursor.execute(sql_query)

#Get the query result
query_result = mycursor.fetchall()

#Store results in lists
#Each record will be returned in the form of a tuple so we will need to access each tuple item
name= []
number = []


for record in query_result:
    name.append(record[1]) 
    number.append(record[0]) 


#Export the data in a chart to an SVG file
bar_chart = pygal.Bar(x_label_rotation=45)
bar_chart.title = "Question 9"
bar_chart.x_labels = map(str, name) #set x axis labels to the employee names
bar_chart.add('Number of Payments', name) # add number of customers
bar_chart.render_to_file('images/mod13_q9.svg') #render the chart to an SVG file

#If program is successful print this
print("Program executed successfully")

### Write your queries and create your charts below

#The cursor will execute  queries on your MySql Datbase
mycursor = mydb.cursor()


sql_query = '''SELECT COUNT(customerNumber), state
 FROM customers
GROUP BY state;'''

#Execute the query
mycursor.execute(sql_query)

#Get the query result
query_result = mycursor.fetchall()

#Store results in lists
#Each record will be returned in the form of a tuple so we will need to access each tuple item
number= []
state = []


for record in query_result:
    state.append(record[1]) 
    number.append(record[0]) 


#Export the data in a chart to an SVG file
bar_chart = pygal.Pie(x_label_rotation=45)
bar_chart.title = "Question 10"
 #set x axis labels to the employee names
bar_chart.add("State", number) # add number of customers
bar_chart.render_to_file('images/mod13_q10.svg') #render the chart to an SVG file

#If program is successful print this
print("Program executed successfully")

### Write your queries and create your charts below
#The cursor will execute  queries on your MySql Datbase
mycursor = mydb.cursor()


sql_query = '''SELECT employeeNumber, reportsTo, firstName, lastName
 FROM employees
 where reportsTo = employeeNumber
ORDER BY reportsTo
LIMIT 1;'''

#Execute the query
mycursor.execute(sql_query)

#Get the query result
query_result = mycursor.fetchall()

#Store results in lists
#Each record will be returned in the form of a tuple so we will need to access each tuple item
number= []
report = []
name = []


for record in query_result:
    report.append(record[6]) 
    number.append(record[0]) 


#Export the data in a chart to an SVG file
bar_chart = pygal.Bar(x_label_rotation=45)
bar_chart.title = "Question 11"
bar_chart.x_labels = map(str, number) #set x axis labels to the employee names
bar_chart.add('Number of Payments', report) # add number of customers
bar_chart.render_to_file('images/mod13_q11.svg') #render the chart to an SVG file

#If program is successful print this
print("Program executed successfully")


### Write your queries and create your charts below

#The cursor will execute  queries on your MySql Datbase
mycursor = mydb.cursor()


sql_query = '''SELECT COUNT(p.amount), c.country
 FROM payments p,  customers c
 where p.customerNumber = c.customerNumber
GROUP BY c.country;'''

#Execute the query
mycursor.execute(sql_query)

#Get the query result
query_result = mycursor.fetchall()

#Store results in lists
#Each record will be returned in the form of a tuple so we will need to access each tuple item
amount= []
country = []


for record in query_result:
    amount.append(record[0]) 
    country.append(record[1]) 


#Export the data in a chart to an SVG file
bar_chart = pygal.Bar(x_label_rotation=45)
bar_chart.title = "Question 13"
bar_chart.x_labels = map(str, country) #set x axis labels to the employee names
bar_chart.add('Payments', amount) # add number of customers
bar_chart.render_to_file('images/mod13_q13.svg') #render the chart to an SVG file

#If program is successful print this
print("Program executed successfully")

### Write your queries and create your charts below
#The cursor will execute  queries on your MySql Datbase
### Write your queries and create your charts below

#The cursor will execute  queries on your MySql Datbase
mycursor = mydb.cursor()


sql_query = '''SELECT e.firstName, e.lastName, c.customerNumber, p.amount
 FROM employees e,  customers c, payments p
 where p.customerNumber = c.customerNumber
 AND e.employeeNumber = c.salesRepEmployeeNumber;'''

#Execute the query
mycursor.execute(sql_query)

#Get the query result
query_result = mycursor.fetchall()

#Store results in lists
#Each record will be returned in the form of a tuple so we will need to access each tuple item
amount= []
name = []


for record in query_result:
    amount.append(record[3]) 
    name.append(record[0] + record[1]) 


#Export the data in a chart to an SVG file
bar_chart = pygal.Bar(x_label_rotation=45)
bar_chart.title = "Question 14"
bar_chart.x_labels = map(str, name) #set x axis labels to the employee names
bar_chart.add('Employee dollar amount', amount) # add number of customers
bar_chart.render_to_file('images/mod13_q14.svg') #render the chart to an SVG file

#If program is successful print this
print("Program executed successfully")

### Write your queries and create your charts below
