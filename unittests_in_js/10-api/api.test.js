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

    describe("testing login", () => {
      describe("POST /login", () => {
        it("Responds 200 and correct name sebastien", (done) => {
          const options = {
            url: "http://localhost:7865/login",
            method: "POST",
            json: true,
            body: {
              userName: "sebastien",
            },
          };

          request(options, function (error, response, body) {
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal("Welcome sebastien");
            done();
          });
        });
      });
    });

    describe("testing available payments", () => {
      describe("GET /available_payments", () => {
        it("Responds with 200 and correct JSON object when parsed", (done) => {
          const options = {
            url: "http://localhost:7865/available_payments",
            method: "GET",
          };

          request(options, function (error, response, body) {
            expect(response.statusCode).to.equal(200);
            const bodyParse = JSON.parse(body);

            const bodyReference = {
              payment_methods: {
                credit_cards: true,
                paypal: false,
              },
            };

            expect(bodyParse).to.deep.equal(bodyReference);
            done();
          });
        });
      });
    });
  });
});
