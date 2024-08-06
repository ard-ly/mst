// Copyright (c) 2024, ARD and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ticket", {
    onload(frm) {
        console.log("after_load");
        
        // Call the server-side method to get effective agents
        // frappe.call({
        //     method: "mst_app.ticket_form.get_effective_agent",
        //     args: {},
        //     callback: r => {
        //         if (!r.exc && r.message) {
        //             console.log(r.message);
                    
        //             // Check if r.message is a list
        //             var effectiveAgentList = r.message;

        //             // Set the query for the 'effective_agent' field
        //             frm.set_df_property("effective_agent", "options", effectiveAgentList);
        //         }
        //     }
        // });
    },

    validate(frm){},

});

