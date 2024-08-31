import os

from src.database.database import Database
from src.utils.service_utils import ServiceUtils

db = Database()

class FormService:
    def __init__(self):
        self.form_sub_table = os.getenv("FORM_SUB_TABLE")

    def save_form(self, formRequest):
        query = f"INSERT INTO fs as {self.form_sub_table} (form_id, form_data) VALUES ({formRequest.form_id}, {formRequest.form_data})"
        response = db.execute_query(query)
        return response

    def get_form(self, formRequest):
        getConditional = ServiceUtils.parse_get_conditional(formRequest.getCondition)
        query = f"SELECT * FROM fs as {self.form_sub_table} WHERE {getConditional};"
        response = db.fetch_query(query)
        return response

    def get_forms(self, formRequest):
        getConditional = ServiceUtils.parse_get_conditional(formRequest.getCondition)
        query = f"SELECT * FROM fs as {self.form_sub_table} WHERE {getConditional};"
        response = db.fetch_query(query)
        return response

    def delete_form(self, formRequest):
        query = f"SELECT * FROM fs as {self.form_sub_table} WHERE fs.form_submission_id={formRequest.form_submission_id};"
        response = db.fetch_query(query)
        return response

    def update_form(self, formRequest):
        query = f"UPDATE fs as {self.form_sub_table} SET {formRequest.updateConditional} WHERE fs.form_submission_id={formRequest.form_submission_id};"
        response = db.execute_query(query)
        return response
