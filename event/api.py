import frappe
from frappe.utils import now

@frappe.whitelist()
def filter_event():
	participant_event = frappe.db.get_list(
		"Participants",
		filters={"receiver_email": frappe.session.user},
		pluck="event_name"
		)

	event_list = frappe.db.get_list(
		"Events_List",
		filters={
			'name1': ["not in", participant_event], 
			'datetime':[">", now()],
			'status': ["!=", "Full"]
			},
		fields=["event_name",'name','description']
		)
	return event_list

