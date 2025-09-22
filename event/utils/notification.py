import frappe

def remainder():
    notification = frappe.new_doc("Notification")
    notification.subject = "Remainder Mail for the event"
    notification.message = """
    <h2>A Quick Remainder!!!!</h2>

    <p>The {{doc.event_name}} event get started Tomorrow!! </p>

    """
    notification.send_alert_on = "Days Before"
    notification.days_in_advance =1
    notification.document_type = "Participants"
    notification.append("recipients",{
        "receiver_by_document_field": "receiver_email"
    })