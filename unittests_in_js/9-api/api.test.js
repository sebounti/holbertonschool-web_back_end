const request = require("request");
const { expect } = require("chai");
const baseUrl = "http://localhost:7865";

describe("Cart Endpoint", () => {
  it("should return status code 200 and correct body when :id is a number", (done) => {
    const id = 10;
    request(`${baseUrl}/cart/${id}`, (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).equal(`Payment methods for cart 10`);
      done();
    });
  });

  it("should return status code 404 when :id is not a number", (done) => {
    const cartId = "notanumber";
    request(`${baseUrl}/cart/${cartId}`, (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done(); // Nécessaire pour les tests asynchrones
    });
  });

  describe("testing integration", () => {
    describe("GET", () => {
      it("Code: 200 | Body: Welcome to the payment system", (done) => {
        const options = {
          url: "http://localhost:7865",
          method: "GET",
        };

        request(options, function (error, response, body) {
          expect(response.statusCode).to.equal(200);
          expect(body).to.equal("Welcome to the payment system");
          done();
        });
      });
    });
  });
});
