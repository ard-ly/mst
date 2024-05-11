# Copyright (c) 2024, ARD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _, msgprint, throw

class Assemblies(Document):
	def validate(self):
		self.validate_main_item()
		self.validate_child_items()

	def validate_main_item(self):
		"""Validates, main Item is not a stock item"""
		if frappe.db.get_value("Item", self.new_item_code, "is_stock_item"):
			frappe.throw(_("Parent Item {0} must not be a Stock Item").format(self.new_item_code))

	def validate_child_items(self):
		for item in self.items:
			if frappe.db.exists("Product Bundle", item.item_code):
				frappe.throw(
					_(
						"Row #{0}: Child Item should not be a Product Bundle. Please remove Item {1} and Save"
					).format(item.idx, frappe.bold(item.item_code))
				)
