# Copyright (c) 2024, ARD and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class QuestionnaireSettings(Document):
	
	@frappe.whitelist()
	def get_category(self,question):
		catagory = ''
		cato_list = frappe.db.sql(f""" SELECT questions_category FROM `tabMulti Questions Category` WHERE parenttype= 'Questions' AND parent='{question}' """,as_dict=1)
		for row in cato_list:
			catagory += row.questions_category + ", "
		return catagory
	
	@frappe.whitelist()
	def calculate_weight(self,type):
		new_weight = 0.0
		if type == "technical_questionnaire_table":
			for row in self.technical_questionnaire_table:
				new_weight += row.weight
		
		elif type == "hardware_questionnaire_table":
			for row in self.hardware_questionnaire_table:
				new_weight += row.weight
		
		elif type == "software_questionnaire_table":
			for row in self.software_questionnaire_table:
				new_weight += row.weight

		return new_weight