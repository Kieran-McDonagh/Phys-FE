import pytest
import os

# must run from the backend root

def run_integration_tests():
    os.chdir('tests/integration')
    pytest.main()


if __name__ == "__main__":
    run_integration_tests()
