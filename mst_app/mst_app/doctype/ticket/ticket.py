# Copyright (c) 2024, ARD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.desk.form import assign_to


class Ticket(Document):

	def validate(self):
		self.create_customer_and_issue()

	def create_customer_and_issue(self):
		if self.docstatus == 0:
			if self.existing_customer == 0:
				# create new customer.
				new_customer = frappe.new_doc("Customer")
				new_customer.custom_created_by_ticket = 1
				new_customer.customer_name = self.customer_name
				new_customer.mobile_no = self.phone
				new_customer.email_id = self.email
				new_customer.insert(ignore_permissions=True)

			new_issue = frappe.new_doc("Issue")
			new_issue.subject = self.issue
			new_issue.customer = self.customer_name
			new_issue.priority = self.priority
			# new_issue.issue_type = self.topic
			if self.issue_summary:
				new_issue.description = self.issue_summary
			new_issue.custom_ticket = self.name
			new_issue.insert(ignore_permissions=True)
			
			assign_to_users = []
			user_docs =frappe.db.get_list('User', pluck='name')
			for user in user_docs:
				doc = frappe.get_doc('User', user)
				roles = [d.role for d in doc.roles]
				if 'supervisor' in roles:
					assign_to_users.append(user)

			if assign_to_users:
				assign_to.add(
					{
						"assign_to": assign_to_users,
						"doctype": 'Issue',
						"name": new_issue.name,
					}
					)
				
	


	
