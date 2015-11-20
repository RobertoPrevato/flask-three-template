export class ChildRouter {
  heading = "Child Router";

  configureRouter(config, router) {
    config.map([
      {
        route: ["", "welcome"],
        name: "welcome",
        moduleId: "areas/public/dashboard/welcome",
        nav: true, title: "Welcome"
      },
      {
        route: "example-form",
        name: "example-form",
        moduleId: "areas/public/dashboard/example-form",
        nav: true,
        title: "Example form"
      },
      {
        route: "child-router",
        name: "child-router",
        moduleId: "areas/public/dashboard/child-router",
        nav: true,
        title: "Child Router"
      }
    ]);

    this.router = router;
  }
}
