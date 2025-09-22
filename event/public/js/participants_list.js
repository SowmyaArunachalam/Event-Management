

frappe.listview_settings['Participants'] = {
    onload: function(listview){
        console.log("Participants list loaded");

        listview.page.add_inner_button(__('Available events'), function() {
            
            let val = frappe.db.get_list("Events_List", {
                filters:{
                    datetime:[">", frappe.datetime.now_datetime()]
                },
                fields:['name1','name','description'] })
                .then(r =>{

                    let list_events =[]
                    let c=0;
                    r.forEach(ev => {
                        console.log(ev.name1)

                        list_events.push({
                        label: ev.name1,
                        fieldname: "event",
                        fieldtype:'Button',
                        description: ev.description,
                        click: ()=>{
                            console.log("Clicked valuee...")
                            frappe.route_options = { "event_name": ev.name};
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
            
                
        });
    }
};

