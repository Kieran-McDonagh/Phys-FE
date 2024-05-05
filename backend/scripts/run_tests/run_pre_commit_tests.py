# import pytest
# import os


# def run_tests():
#     os.environ["ENV"] = "testing"
#     os.chdir("backend/tests/")
#     pytest.main(["-v", "-s", "--capture=no"])


# if __name__ == "__main__":
#     run_tests()

import subprocess
import os


def run_tests():
    os.environ["ENV"] = "testing"
    os.chdir("backend/tests")
    
    # Run pytest as a subprocess and capture its output
    process = subprocess.Popen(["pytest", "-v", "-s"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Read and print output line by line
    while True:
        output = process.stdout.readline().decode().strip()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output)
    
    # Check if there is any error output
    error_output = process.stderr.read().decode().strip()
    if error_output:
        print(error_output)

    # Wait for the process to finish
    process.wait()


if __name__ == "__main__":
    run_tests()

