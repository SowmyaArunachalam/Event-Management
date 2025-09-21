# Copyright (c) 2025, sowmya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Participants(Document):
	def validate(self):
		# count
		if self.type=="Solo":
			self.total_team_members = 1
		else:
			self.total_team_members = len(self.team_member_details)+1

		all_values = frappe.db.get_list(
			"Participants",
			filters={"event_name": self.event_name, "name": ["!=", self.name]},
			fields=["total_team_members"]
			)

		event_list = frappe.db.get_value(
			"Events_List",
			{"name": self.event_name},
			"capacity_of_participants"
		)

		count = event_list
		for value in all_values:
			count -= int(value["total_team_members"])

		if count <= 0:
			frappe.throw(f"Registrations for {self.event_name} event gets full.")
		if count - self.total_team_members <0:
			frappe.throw(f"Only {count} participants can register for the {self.event_name} event.")

		# validate phonenumber
		self.validate_phonenumber(self.phone_number)
			
		# unique participation
		self.unique_participant(self.date_time.date(), self.receiver_email, self.name)
		if self.type =="Group":
			for item in self.team_member_details:
				self.validate_phonenumber(item.phone_number)
					
				self.unique_participant(self.date_time.date(), item.email, self.name)

	
	def on_submit(self):
		
		msg_temp ="""<h2>Confirmation of your participation</h2> 
			<p> Hi {{parti_name}}! 
			The participation for the event-{{event_name}} has been confirmed.</p>"""

		frappe.sendmail(
			recipients=[self.receiver_email],
			subject="Confirmaiton of Your Participation",
			message=frappe.render_template(msg_temp,{
				"parti_name":self.parti_name,
				"event_name": self.event_name
			})
		)

	def unique_participant(self, date, email, name):
		print(date, email, name)
		address = frappe.db.sql(	
					""" Select p.name, p.event_name  From `tabParticipants` as p 
						 left join `tabTeam Details` as t 
						on p.name=t.parent 
						where cast( p.date_time as DATE) = %s and (p.receiver_email =%s or t.email=%s) and p.name != %s """,
					(date, email, email, name), as_dict=1, debug=1)
		print(address)

		if(address):
			frappe.throw("user has already registered for same event today.")

	def validate_phonenumber(self, phone_number):
		if not (phone_number.isdigit() and len(phone_number)==10):
			frappe.throw("Phone Number must be digit or must equals 10 digit.")
