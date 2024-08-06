import frappe

from frappe import _, msgprint, throw
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def map_sal_from_so(source, target=None):
    def set_missing_values(source, target):
        target.document_type = "Sales Partner"
        target.entity_type = "Customer"
        target.entity = source.customer
        target.custom_sales_order = source.name
        target.run_method("set_missing_values")
        target.run_method("calculate_taxes_and_totals")

    doc = get_mapped_doc(
        "Sales Order",
        source,
        {
            "Sales Order": {
                "doctype": "Service Level Agreement",
            },
        },
        target,
        set_missing_values,
    )
    return doc