import sqlite3
import random

db = sqlite3.connect("ledger.db")
db.row_factory = sqlite3.Row
print("Database opened successfully")

cursor = db.cursor()

seedaccounts = [
    (1, 585309209, 'SGSavings726', 'Savings', '2018/11/08', 'SGD', 84327.51),
    (1, 791066619, 'AUSavings933', 'Savings', '2018/11/08', 'AUD', 88055.93),
    (1, 321143048, 'AUCurrent433', 'Current', '2018/11/08', 'AUD', 38010.62),
    (1, 347786244, 'SGCurrent166', 'Current', '2018/11/08', 'SGD', 50664.65),
    (1, 680168913, 'AUCurrent374', 'Current', '2018/11/08', 'AUD', 41327.28),
    (1, 136056165, 'AUSavings938', 'Savings', '2018/11/08', 'AUD', 48928.79),
    (1, 453963528, 'SGSavings842', 'Savings', '2018/11/08', 'SGD', 72117.53),
    (1, 334666982, 'AUSavings253', 'Savings', '2018/11/08', 'AUD', 20558.16),
]

for i in range(len(seedaccounts)):
    cursor.execute("INSERT INTO accounts \
    (user_id, account_number, account_name, account_type,balance_date,currency,balance) \
    VALUES (?, ?, ?, ?, ?, ?, ?)", seedaccounts[i])
    for j in range(10):
        cursor.execute("INSERT INTO transactions \
        (account_id, currency, number, transaction_date) \
        VALUES (?, ?, ?, ?)", (seedaccounts[i][1], seedaccounts[i][5], round(random.uniform(5.33, 50000), 2), '2012/12/01'))

db.commit()
db.close()
