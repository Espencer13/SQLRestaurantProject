import sqlite3 
import matplotlib.pyplot as plt


conn = sqlite3.connect('FastFoodResturant.db')

c = conn.cursor()

#Based on a hypothetical resturant called "McDongles", not entirely sure about how the data 
# in the table would varry from a real resturant, but if its not realistic then they hired a bad manager

mains = [
  ("Hamburger", 2.50, 0.75, 0.06  ),
  ("Cheeseburger", 3.00, 0.80, 0.15 ),
  ("Double Cheesburger", 3.75, 1.00, 0.13 ),
  ("Deluxe Cheeseburger", 4.50, 1.25, 0.20  ),
  ("Deluxe Double Cheeseburger", 5.25, 1.45, 0.17 ),
  ("Chicken Burger", 3.50, 0.75, 0.13),
  ("Deluxe Chicken Burger", 4.50, 1.25, 0.11 ),
  ("Chicken Wrap", 4.50, 1.25, 0.05)
  ]

beverages = [
  ("Small Fountain Pop", 1.00, 0.08, 0.09),
  ("Meduim Fountain Pop", 1.25, 0.10, 0.18),
  ("Large Fountain Pop", 1.45, 0.13, 0.24),
  ("Milkshake", 3.75, 0.95, 0.07),
  ("Chocolate Milk Carton", 1.50, 0.20, 0.04),
  ("Small Coffee", 1.50, 0.06, 0.06),
  ("Meduim Coffee", 1.75, 0.10, 0.09),
  ("Large Coffee", 1.95, 0.14, 0.15),
  ("Cup of Water", 0.00, 0.05, 0.04),
  ("Bottle of Water", 1.25, 0.45, 0.05)
  ]
  
sides = [
  ("Small Fries", 1.25, 0.35, 0.14  ),
  ("Medium Fries", 1.50, 0.38, 0.23  ),
  ("Large Fries", 1.65, 0.40, 0.36  ),
  ("Poutine", 3.00, 0.60, 0.12 ),
  ("Onion Rings", 2.25, 0.40, 0.15 )
  ]

employees = [
  ("Donald McRonald", 13, 15, "Cheeseburger"),
  ("Sir Burger", 25, 22, "Hamburger"),
  ("Wendy Daveson", 18, 15, "Grapes"),
  ("Tony Tiger", 28, 23, "Cereal"),
  ("Cpt. Horatio Crunch", 21, 15, "Cereal"),
  ("Colonel Saunders", 19, 15, "Chicken Burger"),
  ("Papa John", 19, 15, "Pizza"),
  ("Queen Dairy", 17, 15, "Ice Cream"),
  
  ]
  
employeesTasks = [
  ("Donald McRonald", "Fryer"),
  ("Sir Burger", "Manager"),
  ("Wendy Daveson", "Grill"),
  ("Tony Tiger", "General Manager"),
  ("Cpt. Horatio Crunch", "Drive Thru"),
  ("Colonel Saunders", "Fryer"),
  ("Papa John", "Grill"),
  ("Queen Dairy", "Cashier")
  
  ]
  
c.execute("""CREATE TABLE IF NOT EXISTS mains (
        item text,
        salePrice real,
        costToMake real,
        percentage real
    )""")               
               
c.executemany("INSERT INTO mains VALUES (?,?,?,?)", mains)

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS beverages (
        item text,
        salePrice real,
        costToMake real,
        percentage real
    )""")               
               
c.executemany("INSERT INTO beverages VALUES (?,?,?,?)", beverages)

conn.commit()


c.execute("""CREATE TABLE IF NOT EXISTS sides (
        item text,
        salePrice real,
        costToMake real,
        percentage real
    )""")               
               
c.executemany("INSERT INTO sides VALUES (?,?,?,?)", sides)

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS employees (
        employeeName text,
        ordersPerShift integer,
        wage integer,
        favouriteItem text
    )""")               
               
c.executemany("INSERT INTO employees VALUES (?,?,?,?)", employees)

conn.commit()

c.execute("""CREATE TABLE IF NOT EXISTS employeesTasks (
        employeeName text,
        task text
    )""")               
               
c.executemany("INSERT INTO employeesTasks VALUES (?,?)", employeesTasks)

conn.commit()

print("Mains:")
c.execute("SELECT * FROM mains")
main = c.fetchall()
for i in main:
  print(i[0], " | ", i[1], " | ", i[2], " | ", i[3])
print("\n")
  
print("Beverages:")
c.execute("SELECT * FROM beverages")
beverage = c.fetchall()
for i in beverage:
  print(i[0], " | ", i[1], " | ", i[2], " | ", i[3])
print("\n")
  
print("Sides:")
c.execute("SELECT * FROM sides")
side = c.fetchall()
for i in side:
  print(i[0], " | ", i[1], " | ", i[2], " | ", i[3])
print("\n")

print("Employees:")
c.execute("SELECT * FROM employees")
employee = c.fetchall()
for i in employee:
  print(i[0], " | ", i[1], " | ", i[2], " | ", i[3])
print("\n")

print("Employees Tasks: ")
c.execute("SELECT * FROM employeesTasks")
employee = c.fetchall()
for i in employee:
  print(i[0], " | ", i[1])
print("\n")




# Q1 What is the highest price item on each section of the menu?
print("Question 1")

c.execute("""
SELECT item
FROM mains
WHERE salePrice = (SELECT max(salePrice) FROM mains);
 """)

print("\n")

print("Highest Price Main:")
res1 = c.fetchall()
for row in res1:
    r1 = row[0]
    print(r1)
    
c.execute("""
SELECT salePrice
FROM mains
WHERE salePrice = (SELECT max(salePrice) FROM mains);
 """)    
    
res1p = c.fetchall()
for row in res1p:
    r1price = row[0]
    print('$', r1price)    
    
print("\n")

c.execute("""
SELECT item
FROM sides
WHERE salePrice = (SELECT max(salePrice) FROM sides);
 """)

print("Highest Price Side:")
res2 = c.fetchall()
for row in res2:
    r2 = row[0]
    print(r2)
    
c.execute("""
SELECT salePrice
FROM sides
WHERE salePrice = (SELECT max(salePrice) FROM sides);
 """)    
    
res2p = c.fetchall()
for row in res2p:
    r2price = row[0]
    print('$', r2price)    
    
c.execute("""
SELECT item
FROM beverages
WHERE salePrice = (SELECT max(salePrice) FROM beverages);
 """)

print("\n")

print("Highest Price Beverage:")
res3 = c.fetchall()
for row in res3:
    r3 = row[0]
    print(r3)
    
c.execute("""
SELECT salePrice
FROM beverages
WHERE salePrice = (SELECT max(salePrice) FROM beverages);
 """)    
    
res3p = c.fetchall()
for row in res3p:
    r3price = row[0]
    print('$', r3price)    
    
print("\n")

data = {r1:r1price, r2:r2price, r3:r3price}

items = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (5, 5))

plt.bar(items, values, color = 'orange',
        width = 0.5)
 
plt.xlabel("Most expensive item on each menu sections")
plt.ylabel("Cost of an Item ($)")
plt.title("Q1 Most expensive items on each section of the menu")
plt.show()


# Q2 What is the average cost to make an item on each section of the menu?
c.execute("""
SELECT item, round(avg(costToMake), 3)
FROM mains
""")

print("Question 2")
print("\n")
print("Average Cost to Make a Main:")
res = c.fetchall()
for row in res:
    print("$",row[1])
    
x = round(float(row[1]),3)
    
print("\n")
    
c.execute("""
SELECT item, round(avg(costToMake), 3)
FROM sides
""")

print("Average Cost to Make a Side:")
res = c.fetchall()
for row in res:
    print("$",row[1])
    
y = round(float(row[1]),3)    

print("\n")
    
c.execute("""
SELECT item, round(avg(costToMake), 3)
FROM beverages
""")

print("Average Cost to Make a Beverage:")
res = c.fetchall()
for row in res:
    print("$",row[1])
    
z = round(float(row[1]),3)
    
print("\n")

data = {'mains':x, 'sides':y, 'beverages':z}

items = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (5, 5))

plt.bar(items, values, color = 'orange',
        width = 0.5)
 
plt.xlabel("Menu Sections")
plt.ylabel("Average Cost of an Item ($)")
plt.title("Q2 Average cost to make an item on each section of the menu")
plt.show()


# Q3 What employees have a favourite food that is on the menu?

print("Question 3")
print("\n")

c.execute("""
SELECT employeeName FROM employees
INNER JOIN mains ON mains.item = employees.Favouriteitem
""")

print("Employees with a favourite food on the menu: ")

res = c.fetchall()
for row in res:
    print(row[0])
    
print("\n")



# Q4 Do any mains and sides cost the same amount?

print("Question 4")
print("\n")

c.execute("""
SELECT mains.item FROM mains
INNER JOIN sides ON sides.salePrice = mains.salePrice
""")

res1 = c.fetchall()

c.execute("""
SELECT sides.item FROM sides
INNER JOIN mains ON mains.salePrice = sides.salePrice
""")

res2 = c.fetchall()

c.execute("""
SELECT sides.salePrice FROM sides
INNER JOIN mains ON mains.salePrice = sides.salePrice
""")

res3 = c.fetchall()

for row in res1:
    r1 = row[0]
    
for row in res2:
    r2 = row[0]    
    
for row in res3:
    r3 = row[0]   

print("The items that share prices are: ")
print(r1, "&", r2)
    
print("\n")

data = {r1:r3, r2:r3}

items = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (5, 5))

plt.bar(items, values, color = 'orange',
        width = 0.5)
 
plt.xlabel("Items")
plt.ylabel("Cost of an Item ($)")
plt.title("Q4 Do any mains and sides cost the same amount?")
plt.show()

# Q5 Do any items share a likelihood of being ordered with another item?
print("Question 5")

print("\n")

c.execute("""
SELECT mains.item FROM mains
INNER JOIN beverages ON beverages.percentage = mains.percentage
""")

res1 = c.fetchall()

c.execute("""
SELECT beverages.item FROM beverages
INNER JOIN mains ON mains.percentage = beverages.percentage
""")

res2 = c.fetchall()

    
print("The items that share likelihoods of a being ordered are: ")
for row in res1:
    r1 = row[0]
    print(r1)
for row in res2:
    r2 = row[0]
    print(r2)
    
print("\n")

# Bonus Question: If a person ordered a combo (main, side and beverage), what would it most likely be?
# I read the specifictions wrong, but I already wrote this code so I thought I'd keep it in
# Don't have to mark/not expecting marks

c.execute("""
SELECT item
FROM mains
WHERE percentage = (SELECT max(percentage) FROM mains);
 """)

main = c.fetchall()
for row in main:
    main = row[0]
    
    
c.execute("""
SELECT item
FROM sides
WHERE percentage = (SELECT max(percentage) FROM sides);
 """)

side = c.fetchall() 
for row in side:
    side = row[0]
    
    
c.execute("""
SELECT item
FROM beverages
WHERE percentage = (SELECT max(percentage) FROM beverages);
 """)

beverage = c.fetchall()
for row in beverage:
    beverage = row[0]
    

print("Bonus Question: ")
print("The most ordered combo would be: ")
print(main, ',' ,side , ',' , beverage)


