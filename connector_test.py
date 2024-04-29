import mysql.connector

connection = mysql.connector.connect(
    user = 'root',
    database = 'bank',
    password = 'Nori@1724264159'
)

cursor = connection.cursor()
testQuery = ("SELECT * FROM bank_users")
cursor.execute(testQuery)

for row in cursor:
    print(row)

cursor.close()
connection.close()
