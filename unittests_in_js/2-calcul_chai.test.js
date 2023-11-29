const expect = require("chai").expect;
const calculateNumber = require("./1-calcul");

describe("calculateNumber", function () {
  describe("SUM", function () {
    it("should return the sum of two rounded numbers", function () {
      expect(calculateNumber("SUM", 1.4, 4.5)).to.equal(6);
    });
  });

  describe("SUBTRACT", function () {
    it("should round the first argument", function () {
      expect(calculateNumber("SUBTRACT", 1.0, 0)).to.equal(1);
      expect(calculateNumber("SUBTRACT", 1.3, 0)).to.equal(1);
      expect(calculateNumber("SUBTRACT", 1.7, 0)).to.equal(2);
    });

    it("should round the second argument", function () {
      expect(calculateNumber("SUBTRACT", 0, 1.0)).to.equal(-1);
      expect(calculateNumber("SUBTRACT", 0, 1.3)).to.equal(-1);
      expect(calculateNumber("SUBTRACT", 0, 1.7)).to.equal(-2);
    });

    it("should return the right number", function () {
      expect(calculateNumber("SUBTRACT", 1.3, 0)).to.equal(1);
      expect(calculateNumber("SUBTRACT", 0, 1.2)).to.equal(-1);
      expect(calculateNumber("SUBTRACT", 1.3, 1.3)).to.equal(0);
      expect(calculateNumber("SUBTRACT", 1.7, 1.2)).to.equal(1);
      expect(calculateNumber("SUBTRACT", 1.3, 1.8)).to.equal(-1);
      expect(calculateNumber("SUBTRACT", 1.6, 1.8)).to.equal(0);
    });
  });

  describe("DIVIDE", function () {
    it("should return the division of two rounded numbers", function () {
      expect(calculateNumber("DIVIDE", 1.4, 4.5)).to.equal(0.2);
    });

    it("should return 'Error' when dividing by 0", function () {
      expect(calculateNumber("DIVIDE", 1.4, 0)).to.equal("Error");
    });
  });
});
