// Copyright (c) 2025, sowmya and contributors
// For license information, please see license.txt

frappe.ui.form.on("Participants", {
    setup: function(frm){
        frm.set_query("event_name", function(){
            return{
                filters: {
                    "datetime" : [">", frappe.datetime.now_datetime()]
                }
            };
        });
    },
    refresh: function(frm) {
        
        if (frm.is_new()) {
            user_name = frappe.session.user_fullname
            frm.set_value('parti_name', user_name);
            frm.set_value('receiver_email', frappe.session.user_email);
        }
        
    }
        
        
    
    

});
  

