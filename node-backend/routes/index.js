const express = require('express');
const router = express.Router();
const sqlite3 = require('sqlite3').verbose()

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'DB' });
});

router.get('/accounts/:user_id', function(req, res, next) {
  const user_id = req.params.user_id

  let db = new sqlite3.Database('../db/ledger.db', (err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Connected to the database.');
  });

  let query = "SELECT * FROM accounts WHERE user_id = ?"
  let accounts = {"accounts": []}
  db.all(query, [user_id], (err, rows) => {
    if (err) {
      throw err;
    }
    rows.forEach((row) => {
      accounts.accounts.push(row)
    });

    res.send(accounts)
  });
});

router.get('/transactions/:account_id', function(req, res, next) {
  const account_id = req.params.account_id

  let db = new sqlite3.Database('../db/ledger.db', (err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Connected to the database.');
  });

  let query = "SELECT * FROM transactions WHERE account_id = ?"
  let transactions = {"account": account_id, "transactions": []}

  db.all(query, [account_id], (err, rows) => {
    if (err) {
      throw err;
    }
    rows.forEach((row) => {
      transactions.transactions.push(row)
    });

    res.send(transactions)
  });
});


module.exports = router;
