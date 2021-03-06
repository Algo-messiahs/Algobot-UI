import mysql.connector
import environ

env = environ.Env()
environ.Env.read_env()

mydb = mysql.connector.connect(
  host=env("DATABASE_HOST"),
  user=env("DATABASE_USER"),
  password=env("DATABASE_PASSWORD"),
  database=env("DATABASE_NAME")
)


mycursor = mydb.cursor()
# deletes current stock in order for new one to be added in sql database.
sql = "DELETE FROM stocks WHERE id = id"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

# this is where the user inputs stock example apple(AAPL) and get saved to sql
# This is where you would need to add to front end. This
# It is ready and works just need you to add to fron end.
id = input("Enter Stock you want to add to Algobot Algorithm: ")

mycursor = mydb.cursor()

sql = ("INSERT INTO stocks (id) VALUES ('%s')" % (id,))
val = (id)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
