from sqlite3 import *
mydb = connect("C:/Users/USER/Desktop/hancom/python/deep/db/mydb.db")
csr = mydb.cursor()
# csr.execute("CREATE TABLE test(fruit VARCAHR(20), num INT, price INT)")

#csr.execute("INSERT INTO test(fruit, num, price) VALUES('Apple', 10, 1000)")
csr.execute("INSERT INTO test(fruit, num, price) VALUES('Banana', 5, 5000)")
csr.execute('SELECT * FROM test')

row = csr.fetchone()
print(row)

mydb.commit()
mydb.close()