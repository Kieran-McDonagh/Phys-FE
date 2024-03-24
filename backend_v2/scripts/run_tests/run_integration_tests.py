import pytest
import os

def run_integration_tests():
    os.environ['ENV'] = 'testing'
    os.chdir('tests/integration_tests')
    pytest.main(['-v', '-s'])  


if __name__ == "__main__":
    run_integration_tests()
