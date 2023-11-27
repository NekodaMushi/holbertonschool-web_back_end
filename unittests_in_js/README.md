# How to Use Mocha to Write a Test Suite

Mocha is a powerful and flexible JavaScript test framework that runs on Node.js and in the browser, making asynchronous testing simple and fun. Mocha tests run serially, allowing for flexible and accurate reporting, while mapping uncaught exceptions to the correct test cases.

## How to Use Mocha

### Installation

First, install Mocha globally or as a development dependency in your project:

```bash
npm install --global mocha
# OR
npm install --save-dev mocha
```

### Writing Tests

Create a new test file (e.g., `test.js`). Mocha tests are composed of `describe` blocks that define test suites and `it` blocks that define test cases:

```javascript
const assert = require("assert");

describe("Array", function () {
  describe("#indexOf()", function () {
    it("should return -1 when the value is not present", function () {
      assert.equal([1, 2, 3].indexOf(4), -1);
    });
  });
});
```

### Running Tests

Run your tests using the Mocha command:

```bash
mocha test.js
```

## Assertion Libraries

### Node.js Assertions

Node.js has a built-in `assert` module that can be used with Mocha:

```javascript
const assert = require("assert");
assert.strictEqual(1, 1);
```

### Chai Assertion Library

Chai is a BDD/TDD assertion library for node and the browser. It can be paired with any JavaScript testing framework. It has several interfaces that allow the developer to choose the most comfortable.

To use Chai:

1. Install Chai:
   ```bash
   npm install --save-dev chai
   ```
2. Use in tests:
   ```javascript
   const expect = require("chai").expect;
   expect(true).to.be.true;
   ```

## Presenting Long Test Suites

For large test suites, consider:

- Grouping related tests using `describe` blocks.
- Using `context` blocks to define different states or conditions in your tests.
- Keeping tests focused and concise.
- Utilizing `before`, `beforeEach`, `after`, `afterEach` hooks to set up and tear down test environments.

## Spies and Stubs

### Spies

Spies are functions that record how and when they are called. This is useful for verifying that functions have been called, and with the correct parameters.

Example using `sinon`:

```javascript
const sinon = require("sinon");
let spy = sinon.spy();
someFunction(spy);
assert(spy.calledOnce);
```

### Stubs

Stubs are like spies, but they can also replace the target function's behavior. Use stubs to control a method's behavior to test different parts of your application in isolation.

Example using `sinon`:

```javascript
const sinon = require("sinon");
let stub = sinon.stub().returns("fake data");
someAsyncFunction(stub);
```

## Hooks

Mocha provides hooks (`before`, `beforeEach`, `after`, `afterEach`) for setting up conditions that your tests need to run under. These are useful for setup and teardown operations.

Example:

```javascript
describe("Array", function () {
  beforeEach(function () {
    // code
  });

  // ...tests...
});
```

## Async Testing

Mocha naturally handles asynchronous code. Use `done` callback in test cases to handle async operations:

```javascript
it("should return data", function (done) {
  asyncFunction().then((data) => {
    assert.equal(data, expectedData);
    done();
  });
});
```

## Integration Tests with a Node Server

Integration tests involve testing multiple components together. To write integration tests for a Node server:

1. Set up a testing environment (e.g., a test database).
2. Use a library like `supertest` to make HTTP requests to your server.
3. Write tests that assert the response from your server endpoints.

Example using `supertest`:

```javascript
const request = require("supertest");
const app = require("../app");

describe("GET /users", function () {
  it("responds with json", function (done) {
    request(app).get("/users").expect("Content-Type", /json/).expect(200, done);
  });
});
```
