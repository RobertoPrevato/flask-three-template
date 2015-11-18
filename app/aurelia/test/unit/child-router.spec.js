import {ChildRouter} from "../../src/scripts/areas/public/dashboard/child-router";

class RouterStub {
  configure(handler) {
    handler(this);
  }
  map(routes) {
    this.routes = routes;
  }
}

describe("the Child Router module", () => {
  var sut
    , mockedRouter;

  beforeEach(() => {
    mockedRouter = new RouterStub();
    sut = new ChildRouter();
    sut.configureRouter(mockedRouter, mockedRouter);
  });

  it("contains a router property", () => {
    expect(sut.router).toBeDefined();
  });

  it("configures the heading", () => {
    expect(sut.heading).toEqual("Child Router");
  });

  it("should have a welcome route", () => {
    expect(sut.router.routes).toContain({ route: ["","welcome"], name: "welcome",  moduleId: "welcome", nav: true, title:"Welcome" });
  });

  it("should have a users route", () => {
     expect(sut.router.routes).toContain({ route: "example-form", name: "example-form", moduleId: "areas/public/dashboard/example-form", nav: true, title:"Example form" });
  });

  it("should have a child router route", () => {
    expect(sut.router.routes).toContain({ route: "child-router", name: "child-router", moduleId: "child-router", nav: true, title:"Child Router" });
  });
});
