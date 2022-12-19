# sample-project
sample-project


A sample project made for a coding assessment.

Initial prototype made in Flask due to comfort, then rewritten for NodeJS/Express.

To use the Flask backend: navigate to python-backend and type 'flask run' in the terminal

To use Express backend: navigate to node-backend and type 'npm start'

The coding task itself seems fairly simple - I'm not sure if I've misinterpreted it, but it seems to be asking for a backend with just two endpoints that return a list of accounts and transactions.

The local server will have two endpoints: '/accounts/<user_id>' which will return all of the user's accounts in json format, and '/transactions/<account_id>' which will return all of the transactions for a given account, also as a json.
There was only one example user given - I've input the details given for that single user.

Some reflections:
1. This is an obviously insecure api endpoint - the specifications said that logging in/out was outside of scope, so there's no authorisation here.

2. I've made some assumptions in designing the schema - I would assume that that there would be another table to handle user details, which is outside of the scope. In that case, the accounts table should have a foreign key referencing user. User id should also be stored in a session cookie rather than being exposed in the URL bar.

3. I've seeded some random transactions. There is only 1 user at present, with user_id 1. The only response you'll get from the accounts endpoint is from '/accounts/1'. I've limited myself to the data from the assignment, but I can seed more users with random data if required.

4. I'm very new to Node, so I'm not sure about general coding conventions for Express/Node - please forgive me if it looks excessively messy. ExpressJS is almost certainly overkill for a simple project - I certainly don't need the templating engine built in, for instance - in hindsight I could have written it with just Node.
