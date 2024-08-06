# Copyright (c) 2024, ARD and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestTicket(FrappeTestCase):
	@frappe.whitelist()
	def create_issue():
		return "test"
