# Copyright (c) 2025, sowmya and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    
    columns = [
        {'fieldname': 'event_name', 'label': 'Event', 'fieldtype': 'Data', 'width': 200},
        {'fieldname': 'total_team_members', 'label': 'Member', 'fieldtype': 'Int', 'width': 100}
    ]

    data = frappe.db.get_all('Participants', ['event_name', 'total_team_members'])
    
    summary = dict()
    for i in data:
        event_name = i["event_name"]
        total_members = int(i["total_team_members"])
        
        if event_name not in summary:
            summary[event_name] = 0
        summary[event_name] += total_members
        
    data_new = [{"event_name": eve, "total": tot} for eve, tot in summary.items()]
    
    report_summary = [ {"label": i["event_name"], "value":i["total"] }for i in data_new ]
    
    chart = {
		'type': "bar",
		'data': {
			'labels': [f"{row['event_name']}" for row in data_new],
			'datasets':[
				{'values':[row['total'] for row in data_new]}
			]
		}
	}  

    return columns, data, None, chart, report_summary
