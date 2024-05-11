// Copyright (c) 2024, ARD and contributors
// For license information, please see license.txt

frappe.ui.form.on('Assemblies', {
	refresh: function(frm) {

		frm.toggle_enable("new_item_code", frm.is_new());
		frm.set_query("new_item_code", () => {
			return {
				query: "erpnext.selling.doctype.product_bundle.product_bundle.get_new_item_code",
			};
		});

	}
});
