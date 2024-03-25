const assert = require("assert");
const calculateNumber = require("./1-calcul.js");

describe("calculateNumber", function () {
  describe("test1 SUM", function () {
    it("should return 6", function () {
      assert.equal(calculateNumber("SUM", 1.4, 4.5), 6);
    });
  });

  describe("test SUBTRACT", function () {
    it("should return -4", function () {
      assert.equal(calculateNumber("SUBTRACT", 1.4, 4.5), -4);
    });
  });

  describe("test DIVIDE", function () {
    it("should return 0.2", function () {
      assert.equal(calculateNumber("DIVIDE", 1.4, 4.5), 0.2);
    });
  });

  describe("test DIVIDE2", function () {
    it("should return error", function () {
      assert.equal(calculateNumber("DIVIDE", 1.4, 0), "Error");
    });
  });
}); // Add closing parenthesis here
