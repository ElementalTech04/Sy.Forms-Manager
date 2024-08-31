
from src.database.database import Database
from src.utils.service_utils import ServiceUtils

db = Database()

class FormService:
    def __init__(self):
        pass

    def save_form(self, formRequest):
        query = f"INSERT INTO form_submissions (form_id, form_data) VALUES ({formRequest.form_id}, {formRequest.form_data})"
        response = db.execute_query(query)
        return response

    def get_form(self, formRequest):
        getConditional = ServiceUtils.parse_get_conditional(formRequest.getCondition)
        query = f"SELECT * FROM fs as form_submissions WHERE {getConditional};"
        response = db.fetch_query(query)
        return response

    def get_forms(self, formRequest):
        getConditional = ServiceUtils.parse_get_conditional(formRequest.getCondition)
        query = f"SELECT * FROM fs as form_submissions WHERE {getConditional};"
        response = db.fetch_query(query)
        return response

    def delete_form(self, formRequest):
        query = f"SELECT * FROM fs as form_submissions WHERE fs.form_submission_id={formRequest.form_submission_id};"
        response = db.fetch_query(query)
        return response

    def update_form(self, formRequest):
        query = f"UPDATE fs as form_submissions SET {formRequest.updateConditional} WHERE fs.form_submission_id={formRequest.form_submission_id};"
        response = db.execute_query(query)
        return response
