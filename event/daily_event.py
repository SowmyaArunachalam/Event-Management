from datetime import datetime
from frappe.utils.pdf import get_pdf
from frappe import render_template
from frappe import get_print
import frappe

def daily():

    address = frappe.db.sql(
    """ Select p.name From `tabParticipants` as p where cast( p.date_time as DATE)  = curdate()""",
    as_dict=1)
    
    for value in address:
        user = frappe.get_doc('Participants', value['name'])
        
        mail(user.parti_name, user.year, user.college_name, user.event_name, str(user.date_time.date()), user.receiver_email)
        
        for item in user.team_member_details:
            mail(item.name1, item.year, user.college_name, user.event_name, str(user.date_time.date()), item.email)

def mail(name, year, college, event, date, email):
    html_content = frappe.render_template("templates/certificates.html", {
            "parti_name": name,
            "year": year,
            "college_name": college,
            "event_name": event,
            "date_time": date
            })
    
    pdf_data = get_pdf(html_content)
    
    frappe.sendmail(
        recipients=[email],
        subject="Participation Certificate",
        message="Thank you! for your participation",
        attachments=[{
            'fname': "Certification.pdf",
            'fcontent': pdf_data
                }]
            )
    