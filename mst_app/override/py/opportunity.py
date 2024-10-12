import frappe
from frappe import _, msgprint, throw
from frappe.utils import today
from mst_app.tasks import create_notification

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def filter_users(doctype, txt, searchfield, start, page_len, filters):
    role = filters.get("role")

    query = f"""
        SELECT parent
        FROM `tabHas Role`
        WHERE role = '{role}'
        AND parenttype = 'User'
        AND parent LIKE '%{txt}%'
        """

    return frappe.db.sql(query)

def new_items_notes(doc,method):
    # Opportunity Items Notes
    if doc.custom_new_items:
        for row in doc.custom_new_items:
            items_note = frappe.db.sql(f""" select * from `tabOpportunity Items Notes` WHERE opportunity_items_description = '{row.name}' """,as_dict=1)

            if not items_note:
                new_doc = frappe.new_doc("Opportunity Items Notes")
                new_doc.opportunity_items_description = row.name
                new_doc.item_name = row.item_name
                new_doc.item_description = row.item_description
                new_doc.share_to = row.share_to
                new_doc.insert(ignore_permissions=True)

                # create_notification(recipients, subject, doctype, docname)
                new_notification = frappe.new_doc("Notification Log")
                new_notification.from_user = frappe.session.user
                new_notification.for_user = row.share_to
                new_notification.type = "Assignment"
                new_notification.document_type = "Opportunity Items Notes"
                new_notification.document_name = new_doc.name
                new_notification.subject = row.item_name
                new_notification.email_content = "Assignment for Opportunity Items Notes" + row.item_name
                new_notification.insert(ignore_permissions=True)