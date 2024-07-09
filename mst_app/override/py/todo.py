import frappe
from frappe.model.document import Document
from frappe import _, msgprint, throw
from mst_app.tasks import create_notification


# doc_events on validate.
@frappe.whitelist()
def send_email_and_notification(doc, method):
    if doc.reference_type == "Lead":
        if doc.allocated_to:
            subject = str("New task was assigned to you: \n"+doc.description+"\n Due To: "+doc.date)
            doctype = doc.reference_type
            docname = doc.reference_name
            recipients = [doc.allocated_to]
            create_notification(recipients, subject, doctype, docname)
            
            frappe.sendmail(
            recipients=[doc.allocated_to],
            message=str("New task was assigned to you: \n"+doc.description+"\n Due To: "+doc.date+"\n Doctype: "+doc.reference_name),
            header=_('New Task'),
            )
        else:
            msgprint(_("Please Allocate Task To The User."))


@frappe.whitelist()
def move_task(doc,method):
    if doc.status != 'Open': 
        if doc.reference_type == 'Opportunity':
            # reference_name
            tasks_and_events = frappe.db.sql(f""" select * from `tabOpportunity Tasks` WHERE parent = '{doc.reference_name}' AND task = '{doc.name}' """,as_dict=1)
            print(tasks_and_events)
            if tasks_and_events: 
                frappe.db.sql(f""" UPDATE `tabOpportunity Tasks` SET status='{doc.status}' WHERE parent = '{doc.reference_name}' AND task = '{doc.name}' AND parentfield = 'custom_tasks' AND parenttype = 'Opportunity' """)
                frappe.db.commit()
                        
            else:
                new_doc = frappe.new_doc("Opportunity Tasks")
                new_doc.parent = doc.reference_name
                new_doc.parentfield = 'custom_tasks'
                new_doc.parenttype = 'Opportunity'
                new_doc.task = doc.name
                new_doc.description = doc.description
                new_doc.status = doc.status
                new_doc.insert(ignore_permissions=True)