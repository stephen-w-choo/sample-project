# sample-project
sample-project


A sample project made for a coding assessment.

To use: type 'flask run' in the terminal

The local server will have two endpoints: '/accounts/<user_id>' which will return all of the user's accounts in json format, and '/transactions/<account_id>' which will return all of the transactions for a given account.

Some reflections:
1. This is an obviously insecure api endpoint - the specifications said that logging in/out was outside of scope, so there's no authorisation here.

2. I've made some assumptions in designing the schema - I would assume that that there would be another table to handle user details, which is outside of the scope. In that case, the accounts table should have a foreign key referencing user. User id should also be stored in a session cookie rather than being exposed in the URL bar.

3. I've seeded some random transactions. There is only 1 user at present, with user_id 1. The only response you'll get from the accounts endpoint is from '/accounts/1'.


