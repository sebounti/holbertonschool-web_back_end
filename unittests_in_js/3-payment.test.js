const sinon = require("sinon");
const expect = require("chai").expect;
const sendPaymentRequestToApi = require("./3-payment");
const Utils = require("./utils");

describe("Spies", function () {
  it("has the same match", function () {
    const spyUtils = sinon.spy(Utils, "calculateNumber");
    const spyConsole = sinon.spy(console, "log");

    sendPaymentRequestToApi(100, 20);

    expect(spyUtils.calledOnceWithExactly("SUM", 100, 20)).to.be.true;

    spyUtils.restore();
  });
});
