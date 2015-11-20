export class App {
  configureRouter(config, router) {
    config.title = "Flask Aurelia";
    config.map([
      {
        route: ["", "welcome"],
        name: "welcome",
        moduleId: "areas/public/dashboard/welcome",
        nav: true,
        title: "Welcome"
      },
      {
        route: "example-form",
        name: "example-form",
        moduleId: "areas/public/dashboard/example-form",
        nav: true,
        title: "Example Form"
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
