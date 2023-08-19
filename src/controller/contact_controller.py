from fastapi import FastAPI

from src.model.form_submission_request import FormSubmissionRequest

router = FastAPI()


@router.post("/submit")
def submit_contact_form(self, formRequest: FormSubmissionRequest):
    return {"message": "This is Endpoint 1"}
