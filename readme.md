# BattlePhys (**In Development**)

## Backend

To get the project running on your machine, follow these steps:

1. Create a `.env.development` file to store your mongo uri, secret key, algorithm and access token expiration, e.g.:

```
MONGO_URI='mongodb+srv://<username>:<password>@<cluster>.jsphw8s.mongodb.net/<database>?'
SECRET_KEY = "<secret_key>"
ALGORITHM = "<chosen algorithm>"
ACCESS_TOKEN_EXPIRE_MINUTES = <chosen time in minutes>

# to get a secret key, in your terminal run:
openssl rand -hex 32
```

2. To get the dev server running, from the backend root, run `bash run_development.sh`

## Running Tests

To run tests, execute the following command from the backend root:

`scripts/run_tests.sh`

## Frontend

1. First run `npm i` to install dependencies.

2. To run the dev server from the frontend, from the frontend root run `npm run server-start`

3. Then to run the expo app run `npm start`
