import frappe

def after_install():
    add_ticket_link_in_top_bar_items()

def add_ticket_link_in_top_bar_items():
    if not frappe.db.exists("Top Bar Item", {"url":"/ticket"}):
        doc = frappe.new_doc("Top Bar Item")
        doc.label = "Ticket"
        doc.url = "/ticket"
        doc.parent = "Website Settings"
        doc.parenttype = "Website Settings"
        doc.parentfield = "top_bar_items"
        doc.idx = 4
        doc.right = 0
        doc.insert()