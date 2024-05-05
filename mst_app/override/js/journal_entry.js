frappe.ui.form.on("Journal Entry", {
    // refresh: function(frm) {  
	// },
});

// Journal Entry Account Table.
frappe.ui.form.on("Journal Entry Account", {
    account(frm, cdt, cdn) {  
        // cdt = Journal Entry Account, cdn = new-journal-entry-account-1
        let row = locals[cdt][cdn];
        if (frm.doc.custom_cost_center){
            row.cost_center = frm.doc.custom_cost_center;
        }

        if (frm.doc.custom_project){
            row.project = frm.doc.custom_project;
        }
        

	},
});