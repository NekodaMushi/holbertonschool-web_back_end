const chai = require("chai");
const chaiHttp = require("chai-http");
const expect = chai.expect;
const app = require("./api");

chai.use(chaiHttp);

describe("Index page", function () {
  it("should have the correct status code", function (done) {
    chai
      .request(app)
      .get("/")
      .end((err, res) => {
        expect(res).to.have.status(200);
        done();
      });
  });

  it("should have the correct result", function (done) {
    chai
      .request(app)
      .get("/")
      .end((err, res) => {
        expect(res.text).to.equal("Welcome to the payment system");
        done();
      });
  });
});

describe("Cart page", function () {
  it("should return the correct content for a numeric id", function (done) {
    chai
      .request(app)
      .get("/cart/12")
      .end((err, res) => {
        expect(res).to.have.status(200);
        expect(res.text).to.equal("Payment methods for cart 12");
        done();
      });
  });

  it("should return 404 for a non-numeric id", function (done) {
    chai
      .request(app)
      .get("/cart/hello")
      .end((err, res) => {
        expect(res).to.have.status(404);
        done();
      });
  });
});
