"""
# Lecture 5 - Unit Tests

# Unit tests are a way to test individual units of code to ensure they are working as expected. 

# The assert keyword is used to test if a condition is True. If the condition is False, an AssertionError is raised. For example;
# assert 1 + 1 == 2
# assert 1 + 1 == 3 # This will raise an AssertionError

# Pytest:
Pytest is a testing framework for Python. It allows us to write test functions that can be run to check if our code is working correctly. For example;
# def test_addition():
#     assert 1 + 1 == 2
#     assert 1 + 1 == 3 # This will fail the test
#     assert 2 + 2 == 4
and so on...

To run the tests, we can use the command line to navigate to the directory where our test file is located and run the command "pytest". This will run all the test functions in the file and report any failures.

"""