

frappe.listview_settings['Participants'] = {
    onload: function(listview){
        console.log("Participants list loaded");

        listview.page.add_inner_button(__('Check Available Events'), function() {
            
            frappe.xcall("event.api.filter_event",{})
                .then(r =>{
                    console.log(r)
                    let list_events =[]
                    let c=0;
                    r.forEach(ev => {
                        console.log(ev.name1)

                        list_events.push({
                        label: ev.name,
                        fieldname: "event",
                        fieldtype:'Button',
                        description: ev.description,
                        click: ()=>{
                            console.log("Clicked valuee...")
                            frappe.route_options = { "event_name": ev.name, "parti_name": frappe.session.user_fullname, "receiver_email": frappe.session.user_email};
                            frappe.set_route("Form", "Participants", "new")
                        }
                    })
                    });

                    let d = new frappe.ui.Dialog({
                    title: 'Available Events',
                    fields: list_events,
                    });

                    d.show();  

                })

            // frappe.call({
            //     method: "event.api.filter_event",
            //     args:{},
            //     callback: function(r){
            //         let list_events =[]
            //         let c=0;
            //         r.forEach(ev => {
            //             console.log(ev.name1)

            //             list_events.push({
            //             label: ev.name,
            //             fieldname: "event",
            //             fieldtype:'Button',
            //             description: ev.description,
            //             click: ()=>{
            //                 console.log("Clicked valuee...")
            //                 frappe.route_options = { "event_name": ev.name, "parti_name": frappe.session.user_fullname, "receiver_email": frappe.session.user_email};
            //                 frappe.set_route("Form", "Participants", "new")
            //             }
            //         })
            //         });

            //         let d = new frappe.ui.Dialog({
            //         title: 'Available Events',
            //         fields: list_events,
            //         });

            //         d.show();  
            //     }
                
                    

            //     })
            
            
                
        });
    }
};
