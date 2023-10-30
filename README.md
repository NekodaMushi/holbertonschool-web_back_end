# Back-end Project Overview

Welcome! This is my comprehensive Back-end project, encompassing a range of functionalities. Below is a detailed overview of each module and its key features.

## Table of Contents

- [Basic Authentication](#basic-authentication)
- [Session Authentication](#session-authentication)
- [Unit Tests and Integration Tests](#unit-tests-and-integration-tests)
- [Caching](#caching)
- [Pagination](#pagination)
- [Personal Data](#personal-data)
- [Python Variable Annotations](#python-variable-annotations)
- [Python Async Functions](#python-async-functions)
- [User Authentication Service](#user-authentication-service)

### Basic Authentication

#### Topics Covered:

- **What Authentication Means**: The process of verifying the identity of a user or a system.
- **What Base64 Is**: A binary-to-text encoding scheme that converts binary data into a printable ASCII string format.
- **How to Encode a String in Base64**: Utilizing Python’s base64 module to encode strings.
- **What Basic Authentication Means**: A straightforward authentication scheme built into the HTTP protocol.
- **How to Send the Authorization Header**: Utilizing the Authorization header field in HTTP requests.

### Session Authentication

#### Topics Covered:

- **What Authentication Means**: The process of verifying an individual's or system’s identity.
- **What Session Authentication Means**: An authentication process that utilizes sessions to keep users logged in.
- **What Cookies Are**: Small pieces of data stored on the client-side to keep track of user interactions.
- **How to Send Cookies**: Via the 'Set-Cookie' HTTP response header.
- **How to Parse Cookies**: By examining the 'Cookie' HTTP request header.

### Unit Tests and Integration Tests

#### Topics Covered:

- **unittest — Unit Testing Framework**: Python’s built-in library for unit testing.
- **unittest.mock — Mock Object Library**: A library for creating mock objects in Python tests.
- **How to Mock a Readonly Property with Mock?**: Utilizing the @property decorator and the patch() method.
- **Parameterized**: A library for parameterized testing in Python.
- **Memoization**: The technique of caching the result of costly function calls.

### Caching


![3-data-loading-patterns-improve-frontend-performance](https://github.com/NekodaMushi/holbertonschool-web_back_end/assets/98282927/80600646-ab5e-47d9-8156-cd2b8338d30f)


#### Topics Covered:

- **What a Caching System Is**: A system that temporarily stores copies of data to enhance performance.
- **What FIFO Means**: First-In-First-Out, a method to organize and manipulate a queue of data.
- **What LIFO Means**: Last-In-First-Out, a method to organize and manipulate a stack of data.
- **What LRU Means**: Least Recently Used, a strategy for cache eviction.
- **What MRU Means**: Most Recently Used, another strategy for cache eviction.
- **What LFU Means**: Least Frequently Used, another cache eviction strategy.
- **What the Purpose of a Caching System Is**: To speed up data retrieval operations.
- **What Limits a Caching System Has**: Factors like memory size, eviction policies, and invalidation strategies.

### Pagination

#### Topics Covered:

- **How to Paginate a Dataset with Simple Page and Page_Size Parameters**: By using SQL queries’ limit and offset or equivalent methods in NoSQL databases.
- **How to Paginate a Dataset with Hypermedia Metadata**: Through Link headers or additional metadata.
- **How to Paginate in a Deletion-Resilient Manner**: By employing a stable cursor for data traversal.

### Personal Data

#### Topics Covered:

- **What Is PII, Non-PII, and Personal Data?**: Definitions and differences between Personally Identifiable Information and non-PII.
- **Logging Documentation**: Guidelines for securely logging data.
- **bcrypt Package**: A Python library to securely hash passwords.
- **Logging to Files, Setting Levels, and Formatting**: Utilizing Python’s logging library for diverse logging needs.

### Python Variable Annotations

#### Topics Covered:

- **Type Annotations in Python 3**: Syntax for annotating variables with their types.
- **How You Can Use Type Annotations**: For specifying function signatures and variable types.
- **Duck Typing**: A programming paradigm that allows for more flexible and dynamic typing.
- **How to Validate Your Code with Mypy**: A static type checker for Python.

### Python Async Functions

#### Topics Covered:

- **async and await Syntax**: Modern syntax for writing asynchronous programs in Python.
- **How to Execute an Async Program with asyncio**: A Python library for writing single-threaded concurrent code.
- **How to Run Concurrent Coroutines**: Using asyncio.gather or asyncio.run for concurrent execution.
- **How to Create asyncio Tasks**: With the asyncio.create_task() method.
- **How to Use the Random Module**: Python’s built-in pseudo-random number generator.

### User Authentication Service

#### Topics Covered:

- **How to Declare API Routes in a Flask App**: Using the Flask route decorators.
- **How to Get and Set Cookies**: Through Flask’s request and response objects.
- **How to Retrieve Request Form Data**: Using Flask’s request.form attribute.
- **How to Return Various HTTP Status Codes**: Through Flask’s make_response function.
