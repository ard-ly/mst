import frappe
from frappe import _, msgprint, throw
from frappe.utils import today
from mst_app.tasks import create_notification


@frappe.whitelist()
def send_notification(doc,method):
    users=[]
    if doc.event_participants:
        for row in doc.event_participants:
            if row.reference_doctype == 'Opportunity':
                opp_doc = frappe.get_doc('Opportunity', row.reference_docname)
                if opp_doc.opportunity_from == 'Customer':
                    customer_doc = frappe.get_doc('Customer', opp_doc.party_name)
                    if customer_doc.account_manager:
                        users.append(customer_doc.account_manager)
    
    # create_notification(users, doc.subject, "Event", doc.name)
    for user in users :
        email_cont = 'Assignment for Event ' + doc.name
        new_doc = frappe.new_doc("Notification Log")
        new_doc.from_user = frappe.session.user
        new_doc.for_user = user
        new_doc.type = "Assignment"
        new_doc.document_type = "Event"
        new_doc.document_name = doc.name
        new_doc.subject = doc.subject
        new_doc.email_content = email_cont
        new_doc.insert(ignore_permissions=True)

        frappe.sendmail(
            recipients=[user],
            message=str("New Event was assigned to you: \n"+doc.subject),
            header=_('New Event'),
            )


@frappe.whitelist()
def move_event(doc,method):
    if doc.status != 'Open':
        if doc.event_participants:
            for row in doc.event_participants:
                if row.reference_doctype == 'Opportunity':
                    tasks_and_events = frappe.db.sql(f""" select * from `tabOpportunity Events` WHERE parent = '{row.reference_docname}' AND event = '{doc.name}' """,as_dict=1)
                    print(tasks_and_events)
                    if tasks_and_events: 
                        frappe.db.sql(f""" UPDATE `tabOpportunity Events` SET status='{doc.status}' WHERE parent = '{row.reference_docname}' AND event = '{doc.name}' AND parentfield = 'custom_tasks_and_events' AND parenttype = 'Opportunity' """)
                        frappe.db.commit()
                        
                    else:
                        new_doc = frappe.new_doc("Opportunity Events")
                        new_doc.parent = row.reference_docname
                        new_doc.parentfield = 'custom_tasks_and_events'
                        new_doc.parenttype = 'Opportunity'
                        new_doc.event = doc.name
                        new_doc.subject = doc.subject
                        new_doc.status = doc.status
                        new_doc.insert(ignore_permissions=True)

                   

