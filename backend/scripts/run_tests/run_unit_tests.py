import pytest
import os


def run_unit_tests():
    os.environ["ENV"] = "testing"
    os.chdir("tests/unit_tests")
    pytest.main(["-v", "-s"])


if __name__ == "__main__":
    run_unit_tests()
