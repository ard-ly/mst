frappe.ui.form.on("Stock Entry", {
    // refresh: function(frm) {  
	// },
});

// Journal Entry Account Table.
frappe.ui.form.on("Stock Entry Detail", {
    item_code(frm, cdt, cdn) {  
        // cdt = Stock Entry Detail, cdn = new-stock-entry-detail-1
        let row = locals[cdt][cdn];

        if (frm.doc.custom_cost_center){
            row.cost_center = frm.doc.custom_cost_center;
            // frm.refresh_field("cost_center");
        }

        if (frm.doc.custom_project){
            row.project = frm.doc.custom_project;
            // frm.refresh_field("project");
        }
        

	},
});