// Copyright (c) 2025, sowmya and contributors
// For license information, please see license.txt

frappe.ui.form.on("Events_List", {
    'validate': function(frm) {
    if (frm.doc.datetime ==frappe.datetime.get_today()) {
        frappe.throw('You cannot select today');
    }
    else if(frm.doc.datetime < frappe.datetime.now_datetime()) {
        frappe.throw('You can not select past date.');
    }
}
});
