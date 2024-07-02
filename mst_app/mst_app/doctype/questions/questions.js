// Copyright (c) 2024, ARD and contributors
// For license information, please see license.txt

frappe.ui.form.on("Questions", {
    setup: function(frm) {
		// filter on employee.
		frm.set_query("category", function() {
			return {
				filters: {
					"enable": 1
				}
			};
		});
	},
});
