# Copyright (c) 2024, ARD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class OpportunityItemsNotes(Document):
	def on_submit(self):
		self.update_new_items_row()

	def update_new_items_row(self):
		items_note = frappe.db.sql(f""" UPDATE `tabOpportunity Items Description` SET notes = '{self.notes}' WHERE name = '{self.opportunity_items_description}'  """,as_dict=1)
		frappe.db.commit()
	
