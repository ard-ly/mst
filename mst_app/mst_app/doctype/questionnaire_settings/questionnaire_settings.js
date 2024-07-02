// Copyright (c) 2024, ARD and contributors
// For license information, please see license.txt

frappe.ui.form.on("Questionnaire Settings", {
	refresh(frm) {},
});

frappe.ui.form.on("Questionnaire Settings Table", {
    question: function (frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        frappe.call({
            doc: frm.doc,
            method: "get_category",
            args: {
                question: row.question,
            },
            callback: r => {
                if (!r.exc && r.message){
                    console.log(r.message);
                    row.category = r.message;	
                    frm.refresh();						
                }
            }
        })
    },

    weight: function (frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        console.log(row.parentfield);
        
        frappe.call({
            doc: frm.doc,
            method: "calculate_weight",
            args: {
                type: row.parentfield,
            },
            callback: r => {
                if (!r.exc && r.message){
                    console.log(r.message);
                    
                    if (row.parentfield == 'technical_questionnaire_table'){
                        frm.doc.technical_total_weight = r.message;
                        frm.refresh();		
                    }
                    else if (row.parentfield == 'hardware_questionnaire_table'){
                        frm.doc.hardware_total_weight = r.message;
                        frm.refresh();		
                    }
                    else if (row.parentfield == 'software_questionnaire_table'){
                        frm.doc.software_total_weight = r.message;
                        frm.refresh();		
                    }			
                }
            }
        })    
    },

    technical_questionnaire_table_remove:function (frm, cdt, cdn) {
        frappe.call({
            doc: frm.doc,
            method: "calculate_weight",
            args: {
                type: "technical_questionnaire_table",
            },
            callback: r => {
                if (!r.exc && r.message){
                    console.log(r.message);
                    frm.doc.technical_total_weight = r.message;
                    frm.refresh();		
                    }
                else{
                    frm.doc.technical_total_weight = 0;
                    frm.refresh();
                }				 
            }
        })    

    },

    hardware_questionnaire_table_remove:function (frm, cdt, cdn) {
        frappe.call({
            doc: frm.doc,
            method: "calculate_weight",
            args: {
                type: "hardware_questionnaire_table",
            },
            callback: r => {
                if (!r.exc && r.message){
                    console.log(r.message);
                    frm.doc.hardware_total_weight = r.message;
                    frm.refresh();		
                }
                else{
                        frm.doc.hardware_total_weight = 0;
                        frm.refresh();
                }				 
            }
        })    

    },

    software_questionnaire_table_remove:function (frm, cdt, cdn) {
        frappe.call({
            doc: frm.doc,
            method: "calculate_weight",
            args: {
                type: "software_questionnaire_table",
            },
            callback: r => {
                if (!r.exc && r.message){
                    console.log(r.message);
                    frm.doc.software_total_weight = r.message;
                    frm.refresh();		
                }
                else{
                    frm.doc.software_total_weight = 0;
                    frm.refresh();
            }					 
            }
        })    

    },

  });