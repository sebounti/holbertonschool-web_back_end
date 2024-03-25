const chai = require("chai");
const expect = chai.expect;
const calculateNumber = require("./2-calcul_chai.js");

describe("calculateNumber", function () {
  describe("test1 SUM", function () {
    it("should return 6", function () {
      expect(calculateNumber("SUM", 1.4, 4.5)).to.equal(6);
    });
  });

  describe("test SUBTRACT", function () {
    it("should return -4", function () {
      expect(calculateNumber("SUBTRACT", 1.4, 4.5)).to.equal(-4);
    });
  });

  describe("test DIVIDE", function () {
    it("should return 0.2", function () {
      expect(calculateNumber("DIVIDE", 1.4, 4.5)).to.equal(0.2);
    });
  });

  describe("test DIVIDE2", function () {
    it("should return error", function () {
      expect(calculateNumber("DIVIDE", 1.4, 0)).to.equal("Error");
    });
  });
}); // Add closing parenthesis here
