# Unittests and Integration Tests

## Overview
This project focuses on implementing unit tests and integration tests for Python code. Unit tests validate individual units or components of the code, typically functions, while integration tests assess the interaction between various parts of the code, testing code paths end-to-end.

## Project Details
- **Start Date**: May 23, 2024, 6:00 AM
- **End Date**: May 28, 2024, 6:00 AM
- **Checker Release**: May 24, 2024, 12:00 PM
- **Auto Review Launch**: Deadline

## Testing Concepts
- **Unit Testing**: Involves testing individual functions to ensure they return expected results for different inputs, including standard inputs and corner cases. Mocking is common, especially for calls to external functions, particularly those involving network or database operations.
  
  - **Objective**: To determine if the function behaves as expected under the assumption that external dependencies function correctly.
  
- **Integration Testing**: Focuses on testing code paths end-to-end, often involving low-level functions that interact with external systems such as HTTP requests, file I/O, or databases. Mocking is limited to these external interactions.
  
  - **Objective**: To test interactions between different parts of the codebase.

## Execution
Tests can be executed using the following command:
```bash
$ python -m unittest path/to/test_file.py
```

## Resources
Refer to the following resources for further learning:
- [unittest Documentation](https://docs.python.org/3/library/unittest.html) - Python's unit testing framework
- [unittest.mock Documentation](https://docs.python.org/3/library/unittest.mock.html) - Python's mock object library
- [How to mock a readonly property with mock?](https://stackoverflow.com/questions/8658043/how-to-mock-a-readonly-property-with-mock) - Stack Overflow discussion
- [Parameterized Testing](https://pypi.org/project/parameterized/) - Python package for parameterized testing
- [Memoization](https://en.wikipedia.org/wiki/Memoization) - Wikipedia article on memoization technique

## Learning Objectives
Upon completion of this project, you should be able to:
- Explain the difference between unit and integration tests.
- Understand common testing patterns such as mocking, parametrizations, and fixtures.

## Requirements
Ensure the following requirements are met:
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should follow the `pycodestyle` style (version 2.5).
- All files must be executable.
- All modules, classes, and functions should be documented.
- Documentation should provide clear explanations of the purpose of the module, class, or method.

## Required Files
Ensure the presence of the following files:
- `utils.py`
- `client.py`
- `fixtures.py
sebsibe solomon`
