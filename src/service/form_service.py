from idlelib.query import Query

from src.database.database import Database

db = Database()

class FormService:
    def __init__(self):
        pass

    def save_form(self, formRequest):
        query = Query().from_table("form_submissions").insert(**formRequest)
        response = db.execute_query(query)
        return response

    def get_form(self, formRequest):
        pass

    def get_forms(self, formRequest):
        pass

    def delete_form(self, formRequest):
        pass

    def update_form(self, formRequest):
        pass
