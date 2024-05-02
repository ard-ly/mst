frappe.ui.form.on("Lead", {
    // refresh: function(frm) {

	// },

    source(frm) {
		if (frm.doc.source == "Campaign"){
			frm.set_value("custom_document_type", "Campaign");
		}
		else if (frm.doc.source == "Existing Customer"){
			frm.set_value("custom_document_type", "Customer");
		}
		else if (frm.doc.source == "Supplier Reference"){
			frm.set_value("custom_document_type", "Supplier");
		}
		else{
			frm.set_query("custom_document_type", function() {
				return {
					"filters": {
						"issingle": 0 ,
						"istable": 0 
					}
				};
			});	
		}
	},
});