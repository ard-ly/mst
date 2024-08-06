import frappe
from frappe import _, msgprint, throw
from frappe.model.mapper import get_mapped_doc
from datetime import datetime

# @frappe.whitelist()
# def get_effective_agent():
#     agents_list = frappe.db.sql("""SELECT user FROM `tabEffective Agent Table`""", as_dict=True)
#     users_list = [agent['user'] for agent in agents_list]
#     return users_list

@frappe.whitelist()
def send_email_to_customer(email,customer_name,topic,issue,start_date,end_date,on_site):
    recipient = email  
    subject = 'New MST Ticket' 
    message = """<p>Dear Mr./Ms.""" + customer_name + """, <br> 
                Thank you for contacting MST Company. We have created a new  ticket regarding the """ + topic + """you reported, specifically concerning a"""+ issue + """.<br>
                Our team will address this issue """+ on_site +""" and expects to have it resolved between""" + start_date+""", and """+ end_date+""".<br>
                If you did not recently contact MST Company or believe this message was sent in error, please notify us immediately by responding to this email.<br>
                Thank you for your attention, and we appreciate your cooperation.<br>
                Sincerely,
                <br> MST Company </p>"""
    frappe.sendmail(
            recipients=[recipient],
            subject=subject,
            message=message,
        )
    frappe.db.commit()
    return "Email Sent Successfly"

@frappe.whitelist()
def check_sla(sla_number):
    sla = frappe.db.sql(f"""select * from `tabService Level Agreement` where name = '{sla_number}' """, as_dict=1)
    if sla:
        for row in sla:
            return row.entity
