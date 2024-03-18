import pytest
import os

# must run from the backend root

os.environ['TEST_ENV'] = 'true'

def run_integration_tests():
    os.chdir('tests/integration')
    pytest.main(['-v', '-s'])  


if __name__ == "__main__":
    run_integration_tests()
