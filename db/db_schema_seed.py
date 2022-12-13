import sqlite3

db = sqlite3.connect("ledger.db")
print("Database opened successfully")

# Note - in a situation with a login there would be a separate table containing user details, like username, id, email, etc.
# As the scope of this project does not include logins I have created a user_id column in accounts that is NOT a foreign key
# However, if a users table existed, the user_id would reference the user table as a foreign key.

db.execute("CREATE TABLE accounts (\
id INTEGER PRIMARY KEY AUTOINCREMENT, \
account_number INT, \
user_id INT, \
account_name VARCHAR(20), \
account_type VARCHAR(20), \
balance_date DATE, \
currency VARCHAR(10), \
balance DECIMAL(10, 2))")

db.execute("CREATE TABLE transactions (\
transaction_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
account_id INT, \
currency VARCHAR(10), \
number INT, \
transaction_date TINYTEXT, \
FOREIGN KEY (account_id) REFERENCES accounts(account_number))")

print("Table created successfully")

db.close()
