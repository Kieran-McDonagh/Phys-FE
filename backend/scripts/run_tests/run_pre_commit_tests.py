import pytest
import os


def run_tests():
    os.environ["ENV"] = "testing"
    os.chdir("backend/tests/")
    pytest.main(["-v", "-s", "--capture=yes"])


if __name__ == "__main__":
    run_tests()
