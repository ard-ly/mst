// Copyright (c) 2024, ARD and contributors
// For license information, please see license.txt

frappe.ui.form.on("Supplier Partner", {
	// refresh(frm) {

	// },

    after_save(frm) {
        frappe.call({
            doc: frm.doc,
            method: "create_contact",
            args: {},
            callback: r => {
                if (!r.exc && r.message){
                    console.log(r.message);
                    frm.refresh();						
                }
            }
        })
    },
});
