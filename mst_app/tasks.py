import frappe
from datetime import datetime, timedelta
from frappe.utils import today


def create_notification(recipients: list, subject: str, doctype:str = "", docname:str = ""):
    for user in recipients:
        # send notification
        notification = frappe.new_doc("Notification Log")
        notification.subject = subject
        notification.for_user = user
        notification.type = "Alert"
        if doctype:
            notification.document_type = doctype
        if docname:
            notification.document_name = docname
        notification.insert(ignore_permissions=True)
        frappe.db.commit()