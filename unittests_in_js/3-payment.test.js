const sinon = require("sinon");
var { expect } = require("chai");

const sendPaymentRequestToApi = require("./3-payment");
const Utils = require("./utils");

describe("Spies", function () {
  it("has the same match", () => {
    const spyUtils = sinon.spy(Utils, "calculateNumber");
    const spyConcole = sinon.spy(console, "log");

    sendPaymentRequestToApi(100, 20);

    expect(spyUtils.calledOnceWithExactly("SUM", 100, 200)).to.be.true;
    expect(spyConcole.calledOnceWithExactly("the total is; 120")).to.be.true;

    spyUtils.restore();
    spyConcole.restore();
  });
});
