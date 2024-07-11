# Copyright (c) 2024, ARD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SupplierPartner(Document):

	@frappe.whitelist()
	def create_contact(self):
		self.save()
		tasks_and_events = frappe.db.sql(f""" select * from `tabContact` WHERE custom_supplier_partner = '{self.name}' """,as_dict=1)
		
		if not tasks_and_events:
			new_doc = frappe.new_doc("Contact")
			new_doc.custom_supplier_partner = self.name
			new_doc.first_name = self.full_name
			
			if self.designation:
				new_doc.designation = self.designation
			if self.gender:
				new_doc.gender = self.gender
			
			new_doc.append("links", {'link_doctype': "Supplier",
									 'link_name': self.supplier,
							})
			new_doc.is_primary_contact = 1 
			new_doc.insert(ignore_permissions=True)

			return new_doc.name
