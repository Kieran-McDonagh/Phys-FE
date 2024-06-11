# BattlePhys (**In Development**)

This project has been built using:

Backend technologies:

- [FastAPI](https://fastapi.tiangolo.com/tutorial/)
- [Docker](https://docs.docker.com/get-started/overview/)
- [pytest](https://docs.pytest.org/en/8.2.x/getting-started.html)

Frontend technologies:

- [Bun](https://bun.sh/docs)
- [React Native](https://reactnative.dev/docs/environment-setup)
- [Expo](https://docs.expo.dev/get-started/set-up-your-environment/)
- [Xcode](https://www.freecodecamp.org/news/how-to-download-and-install-xcode/)
- [Android Studio](https://developer.android.com/studio)

## Getting Started

1. Create a `.env` file to store your mongo uri, secret key, algorithm and access token expiration, e.g.:

```
MONGO_URI = "mongodb://mongo:27017/test_database"
SECRET_KEY = "<secret_key>"
ALGORITHM = "<chosen algorithm>"
ACCESS_TOKEN_EXPIRE_MINUTES = <chosen time in minutes>

# to get a secret key, in your terminal run:
openssl rand -hex 32
```

1. To get just the development server running, from the backend root, run: `scripts/run_app.sh`

## Running Backend Tests

To run tests, execute the following command from the backend root: `scripts/run_tests.sh`

## Running the App

To run the Battlephys App with a development server:

1. First run `bun install` to install dependencies.

2. To run the developer server from the frontend, from the frontend root run: `bun run server`

3. Then to run the expo app run `bun start`
