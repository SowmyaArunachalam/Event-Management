// Copyright (c) 2025, sowmya and contributors
// For license information, please see license.txt

frappe.query_reports["List of Participation"] = {
	"filters": [{
		fieldname: "event_name",
    	label: "Event",
    	fieldtype: "Link",
    	options: "Events_List",
    	reqd :0
}]
};
