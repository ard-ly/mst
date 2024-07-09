frappe.ui.form.on("Event", {
    
    refresh: function(frm) {   
      frm.set_query('reference_doctype', "event_participants", function() {
        return {
          "filters": {
            "name": ["in", [ "Customer", "Employee", "Sales Partner", "Supplier Partner"]]
          }
        };
      });
    },
});


frappe.ui.form.on("Event Participants", {
	
  // reference_docname: function (frm, cdt, cdn) {
  //   let row = locals[cdt][cdn];
  //     if (row.reference_doctype == 'Supplier Partner'){
  //       var d = new frappe.ui.Dialog({
  //         title: __("New Supplier Partner"),
  //         fields: [
  //               {
  //                 label: __("Supplier"),
  //                 fieldname: "supplier",
  //                 fieldtype: "Link",
  //                 options: "Supplier",
  //                 reqd: 1,
  //               },
  //               {
  //                 label: __("Full Name"),
  //                 fieldname: "full_name",
  //                 fieldtype: "Data",
  //                 reqd: 1,
  //               },
  //               {
  //                 label: __("Designation"),
  //                 fieldname: "designation",
  //                 fieldtype: "Data",
  //                 reqd: 0,
  //               },
  //               {
  //                 label: __("Gender"),
  //                 fieldname: "gender",
  //                 fieldtype: "Link",
  //                 options: "Gender",
  //                 reqd: 0,
  //               },
  //             ],
  //         primary_action: function () {
  //             var data = d.get_values();
  //             let supplier =  data.supplier;
  //             let full_name =  data.full_name;
  //             let designation =  data.designation;
  //             let gender =  data.gender;

  //         //       frappe.call({
  //         //         method: "",
  //         //         args: {
  //         //           supplier: supplier,
  //         //           full_name: full_name,
  //         //           designation: designation,
  //         //           gender: gender,
  //         //         },
  //         //         callback: function (r) {
  //         //           if (!r.exc) {
  //         //             // row.reference_docname = r.message ;
  //         //             d.hide();
  //         //           }
  //         //         },
  //         //       });
  //             },
  //           });
  //           d.show();
  //       }
  //   },
});