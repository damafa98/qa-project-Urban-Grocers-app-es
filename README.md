# Urban Grocers Project

#### Daniela Malagon. Sprint 7

### Project Files:
- configuration.py: Stores the URL and request paths.
- data.py: Contains the required bodies for the requests.
- sender_stand_request.py: Contains functions for creating a new user and a new kit.
- create_kit_name_kit_test.py: Contains all functions and tests for creating a new kit.
- README.md: Contains a brief description of the project.
- .gitignore: Lists the files that should be ignored by git.

---

### Project Description:
- This project involves testing the creation of a new product kit in the Urban Grocers app. Specifically, the "Name" field will be tested according to its requirements for creation. Both positive and negative tests will be performed, expecting each response to match the expected code.

---

### Test Checklist:

**№	Description	ER:**
1.	Allowed number of characters (1): kit_body = { "name": "a"} Response code: 201. The "name" field in the response body matches the "name" field in the request body.
2.	Allowed number of characters (511): kit_body = { "name":"The test value for this check will be shorter than" } Response code: 201. The "name" field in the response body matches the "name" field in the request body.
3.	Number of characters less than allowed (0): kit_body = { "name": "" } Response code: 400.
4.	Number of characters greater than allowed (512): kit_body = { "name":"The test value for this check will be shorter than" } Response code: 400
5.	Special characters are allowed: kit_body = { "name": ""№%@"," } Response code: 201 The "name" field in the response body matches the "name" field in the request body.
6.	Spaces are allowed: kit_body = { "name": " A Aaa " } Response code: 201 The "name" field in the response body matches the "name" field in the request body.
7.	Numbers are allowed: kit_body = { "name": "123" } Response code: 201 The "name" field in the response body matches the "name" field in the request body.
8.	Parameter not passed in the request: kit_body = { } Response code: 400
9.	A different parameter type passed (number): kit_body = { "name": 123 } Response code: 400

---

### Technologies Used:

- Pytest
- Requests

To install these, open the PyCharm terminal and run the following commands:
- pip install pytest
- pip install requests

---

### Instructions 

- Run all project tests via the PyCharm terminal: type pytest create_kit_name_kit_test.py in the terminal.
- Run all tests via the PyCharm interface by clicking the green triangle button at the top.
- Make sure you run them on the correct file; an easy way is to go to the file and select "Current File" before clicking the green triangle.
- Another way to run the tests is by clicking the green arrows next to the tests in the code.
- Some tests will return FAILED as a result; don't worry, this is expected behavior according to the checklist.

