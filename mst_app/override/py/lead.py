import frappe
from frappe import _, msgprint, throw
from frappe.utils import today

@frappe.whitelist()
def get_qualification_value(qualification):
    values = frappe.db.sql(f""" select value from `tabQualification Table` WHERE qualification='{qualification}' AND parenttype='Lead Qualification Matrix' """,as_dict=1, pluck="value")
    print(values)
    return values

@frappe.whitelist()
def get_qualification_marks(doc,method):
    mark = 0 
    if doc.custom_lead_qualification:
        for row in doc.custom_lead_qualification:
            qualification_and_value_mark = frappe.db.sql(f""" select mark from `tabQualification Table` WHERE qualification='{row.qualification}' AND value='{row.value}' AND parenttype='Lead Qualification Matrix' """,as_dict=1, pluck="mark")
            if qualification_and_value_mark:
                mark += qualification_and_value_mark[0]
                print(mark)
        
        qualification_mark = frappe.db.get_value("Lead Qualification Matrix","Lead Qualification Matrix", "qualification_mark")
        
        if int(mark) >= int(qualification_mark):
            doc.qualification_status = 'Qualified'
            # doc.qualified_on = today()
        else:
            doc.qualification_status = 'Unqualified'
            # doc.qualified_on = today()
