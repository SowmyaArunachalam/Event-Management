# Copyright (c) 2025, sowmya and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	
    columns = [
        {'fieldname': 'participant', 'label': 'Participants', 'fieldtype': 'Data', 'width': 200},
        {'fieldname': 'phone_number', 'label': 'Phone Number', 'fieldtype': 'Data', 'width': 200},
        {'fieldname': 'year', 'label': 'Year', 'fieldtype': 'Data', 'width': 200},
        {'fieldname': 'email', 'label': 'Email', 'fieldtype': 'Email', 'width': 250}
    ]

    Event= {
		filters.get("event_name")
	}
    
    new = frappe.db.sql(
        """ Select p.name, p.type, p.parti_name, p.phone_number as pno, p.year as yr, p.receiver_email as email
        From `tabParticipants` as p where p.event_name = %s 
         """,
        (Event),
        as_dict=1,
        )
    summary = dict()
    for val in new:
        if val['type'] == "Group":
            address = frappe.db.sql(
                """ Select p.name, p.parti_name, p.phone_number as pno, p.year as yr, p.receiver_email as email,
                t.name1, t.phone_number, t.year, t.email as mail From `tabParticipants` as p 
                join `tabTeam Details` as t 
                on  p.name = t.parent where p.event_name = %s 
                """,
                (Event),
                as_dict=1,
                )

            for i in address:
                if i['name'] not in summary:
                    summary[i['name']] = [{"participant":i['parti_name'], "phone_number": i['pno'],"year": i["yr"], "email": i["email"]},
                                        {"participant":i['name1'], "phone_number": i['phone_number'],"year": i["year"], "email": i["mail"]}]
                else:
                    summary[i['name']].append({"participant":i['name1'], "phone_number": i['phone_number'],"year": i["year"], "email": i["mail"]})
            [{"event_name": eve, "total": tot} for eve, tot in summary.items()]
        else:
            summary[val['name']] = [{"participant":val['parti_name'], "phone_number": val['pno'],"year": val["yr"], "email": val["email"]}]
            
    
    data=[]
    for i, j in summary.items():
        for  k in j:
            data.append(k)

    return columns, data

