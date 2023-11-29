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
