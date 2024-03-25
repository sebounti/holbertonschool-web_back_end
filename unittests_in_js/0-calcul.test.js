// test function 0-calcul.js

const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("calculateNumber", function () {
  describe("two Integers", function () {
    it("should return 4", function () {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });
  });

  describe("one float", function () {
    it("should return 5", function () {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
    });
  });

  describe("two float", function () {
    it("should return 5", function () {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });
  });

  describe("two float2", function () {
    it("should return 6", function () {
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
  });

  describe("not integer1", function () {
    it("should throw TypeError if parameters are not numbers", function () {
      assert.throws(() => {
        calculateNumber("a", 3);
      }, TypeError);
    });
  });

  describe("not integer2", function () {
    it("should throw TypeError if parameters are not numbers", function () {
      assert.throws(() => {
        calculateNumber(5, "c");
      }, TypeError);
    });
  });
});
