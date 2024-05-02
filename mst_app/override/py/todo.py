import frappe
from frappe.model.document import Document
from frappe import _, msgprint, throw
from mst_app.tasks import create_notification


# doc_events on validate.
@frappe.whitelist()
def send_email_and_notification(doc, method):
    pass
    if doc.reference_type == "Lead":
        if doc.allocated_to:
            # msgprint(str(doc.allocated_to))
            subject = str("New task was assigned to you: \n"+doc.description+"\n Due To: "+doc.date)
            doctype = doc.reference_type
            docname = doc.reference_name
            recipients = [doc.allocated_to]
            create_notification(recipients, subject, doctype, docname)
            
            frappe.sendmail(
            recipients=[doc.allocated_to],
            message=str("New task was assigned to you: \n"+doc.description+"\n Due To: "+doc.date+"\n Doctype: "+doc.reference_name),
            header=_('New Task'),
            # attachments=[{"file_url": "/app/lead/{doc.reference_name}"}],
            # subject="New Task",
            )
