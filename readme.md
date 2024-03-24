# BattlePhys

## Getting Started

To get the project running on your machine, follow these steps:

1. In the root of the project, create a venv with `python3 -m venv venv`

2. Set the PYTHONPATH to point to the project root in the activation script. For example:
   ```bash
   export PYTHONPATH="/path/to/project/BattlePhys/"
   ```
3. Install required dependencies: cd into backend, then `pip install -r requirements.txt`

4. Create a `.env` file to put your mongo uri's in.

## Running Integration Tests

To run integration tests, execute the following command from the root of the backend directory:

```bash
python scripts/run_tests/run_integration_tests.py

```
