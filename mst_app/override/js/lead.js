frappe.ui.form.on("Lead", {

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
});


frappe.ui.form.on("Lead Qualification", {
	qualification: function (frm, cdt, cdn) {
		let row = locals[cdt][cdn];
		frappe.call({
			method: "mst_app.override.py.lead.get_qualification_value",
			args: {
				qualification: row.qualification,
			},
			callback: r => {
				if (!r.exc && r.message){
					console.log(r.message);
					// cur_frm.set_df_property("child_table_field_name","options",["A","B","C","D"],"current_form_name","field_name_of_chils_table","name_of_child_table_row")
					frm.set_df_property("custom_lead_qualification",  'options', r.message, frm.docname, 'value',row.name );
				}
			}
		});
	},

});