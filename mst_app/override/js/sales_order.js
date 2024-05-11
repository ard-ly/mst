frappe.ui.form.on("Sales Order", {
    refresh: function(frm) {  

        // Create Budget Load Doctype.
        //before submit.
        if (frm.doc.docstatus == 0 && !frm.is_new()) {
            frm.add_custom_button(
            __("Service Level Agreement"),
            function () {
                frappe.model.open_mapped_doc({
                method: "mst_app.api.map_sal_from_so",
                frm: frm,
                });
            },
            __("Create")
            );
        }

	},

});