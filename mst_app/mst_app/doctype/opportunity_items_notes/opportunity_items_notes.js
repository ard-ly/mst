// Copyright (c) 2024, ARD and contributors
// For license information, please see license.txt

frappe.ui.form.on("Opportunity Items Notes", {
	onload(frm) {
        if (frappe.user == frm.doc.share_to){
            frm.set_df_property("notes", "read_only", 0);
        }

	},
});

