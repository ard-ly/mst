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

def issue_reminder():
    users = []
    user_docs =frappe.db.get_list('User', pluck='name')
    for user in user_docs:
        doc = frappe.get_doc('User', user)
        roles = [d.role for d in doc.roles]
        if 'supervisor' in roles:
            users.append(user)
    
    issues = frappe.db.sql("""select name from `tabIssue` where status = 'Open' """, as_dict=1 ,pluck='name')
    
    if users:
        if issues:
            for issue in issues:
                create_notification(users, "Open issue", "Issue", issue)