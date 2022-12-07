import sqlite3
from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

@app.route("/accounts", methods=["GET", "POST"])
def accounts():
    # assume there has been some kind of authentication and authorisation and user variable is stored in a session
    if request.method == "GET":
        db = sqlite3.connect("ledger.db")
        db.row_factory = sqlite3.Row
        cursor = db.cursor()

        # assume that the user variable has been obtained from a session instance once the user is logged in
        user = 1 # for the purpose of this exercise we'll assume a user_id of 0 as that's what I've seeded the database with
        cursor.execute("SELECT * FROM accounts WHERE user_id = ?", (user, ))
        result = {
            "accounts": [dict(row) for row in cursor.fetchall()]
            }

        return result

@app.route("/transactions/<account_id>", methods=["GET", "POST"])
def transactions(account_id):
    # assume there has been some kind of authentication/authorisation
    if request.method == "GET":
        db = sqlite3.connect("ledger.db")
        db.row_factory = sqlite3.Row
        cursor = db.cursor()

        cursor.execute("SELECT * FROM transactions WHERE account_id = ?", (account_id, ))

        result = {
            "transactions": [dict(row) for row in cursor.fetchall()]
            }
        db.close()

        return result
