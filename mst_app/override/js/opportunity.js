frappe.ui.form.on("Opportunity", {

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
		else if (frm.doc.source == "Customer's Vendor"){
			frm.set_value("custom_document_type", "Supplier");

		}
		else{
			frm.doc.custom_document_type = "";
			frm.refresh_field("custom_document_type");	
		}
	},

    onload_post_render: function(frm) {   
		frm.set_query("share_to", "custom_new_items", function () {
			return {
			  query: "mst_app.override.py.opportunity.filter_users",
			  filters: {
				role: "Pre Sales",
			  },
			};
		  });
      },
}); 

frappe.ui.form.on("Opportunity Items Description", {

});

