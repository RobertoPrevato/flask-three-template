//
//  Base model for administrative panels
//
R("admin-panel", ["app", "model"], function (app, Model) {

  // NB: this file defines the base model for all administrative panels
  // therefore, it should contain only common, abstracted functions.
  return Model.extend({

    template: "generic-panel",
    editItemTitle: I.t("voc.EditItem"),
    createItemTitle: I.t("voc.CreateNewItem"),

    handleParams: function (params) {
      if (!params) params = { view: "list" };
      //function to use to handle url changes;
      var self = this;
      if (!self.form) self.set("form", {});
      self.view = params.view;
      switch (params.view)
      {
        case "list":
          //display the list view
          self.subtemplate("tableview");
          break;
        case "details":
          //display the detail view
          self
            .loading(true)
            .formtitle(self.editItemTitle)
            .subtemplate(self.detailView)
            .loadDetails(params.id);
          break;
        case "edit":
          //load both the item data; and the form data;
          var a = self.services.getDetails({
            id: params.id
          }), b = self.services.getFormData ? self.services.getFormData({}) : null;

          self
            .loading(true)
            .formtitle(self.editItemTitle)
            .subtemplate(self.formView);

          $.when(a, b).done(function (aData, bData) {
            //set the object data
            self.data(aData[0]);
            if (b)
              //set the form data
              self.form(bData[0]);

            //now display the view
            self.loading(false);
          }).fail(function () {
            self.error({
              title: I.t("errors.LoadingData"),
              retry: function () {
                self.loading(true).delay(function () {
                  self.handleParams(params);
                }, 300);
              }
            }).loading(false);
          });

          self.loading(true);
          break;
        case "creation":
          //display the creation view
          if (self.services.getFormData) {
            self
              .loading(true)
              .formtitle(self.createItemTitle)
              .subtemplate(self.formView)
              .getFormData();
          } else {
            //no data fetching is required to display the form
            self
              .formtitle(self.createItemTitle)
              .subtemplate(self.formView);
          }
          break;
        default:
          throw "View type `" + params.view + "` is not handled.";
      }
    },

    loadDetails: function (id) {
      var self = this;

      self.services.getDetails({
        id: id
      }).done(function (data) {
        self
          .data(data)
          .loading(false);
      }).fail(function () {
        self.error({
          title: I.t("errors.LoadingData"),
          retry: function () {
            self.loading(true).delay(function () {
              self.loadDetails(id);
            }, 300);
          }
        }).loading(false);
      });
    },

    getFormData: function () {
      var self = this;

      self.services.getFormData({
        context: self
      }).done(function (data) {
        self
          .data(self.getDefaultObject())
          .form(data)
          .loading(false);
      }).fail(function () {
        self.error({
          title: I.t("errors.LoadingData"),
          retry: function () {
            self.loading(true).delay(function () {
              self.getFormData();
            }, 300);
          }
        }).loading(false);
      });
    },

    save: function () {
      //avoid fast clicking problems:
      var self = this, sub = "__submitting__";
      if (self[sub]) return false;
      self[sub] = true;

      //validate the form
      self.validate().done(function () {
        //try to save
        self.services.save({
          data: self.getData()
        }).always(function () {
          self[sub] = false;
        }).done(function (data) {
          //data was saved successfully
          alert("Data was saved successfully");
        }).fail(function () {
          //server side error during saving
          //in this case, display a modal dialog
          app.error();
        });
      }).fail(function () {
        //validation failed
        self[sub] = false;
      });
    },

    cancel: function () {
      location.hash = this.listUrl;
    },

    // returns the default object to use when creating a new item
    getDefaultObject: function () {
      return {};
    },

    getData: function () {
      return this.data();
    }

  });
});