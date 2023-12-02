const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("calculateNumber", function () {
  it("should round a and b and return the sum of it", function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3.7), 6);
  });
  it("should return 4 when passed 1 and 3.4", function () {
    assert.strictEqual(calculateNumber(1, 3.4), 4);
  });
  it("should return 2 when passed -1.4 and 3", function () {
    assert.strictEqual(calculateNumber(-1.4, 3), 2);
  });
  it("should return -2 when passed 1 and -3.4", function () {
    assert.strictEqual(calculateNumber(1, -3.4), -2);
  });
});
