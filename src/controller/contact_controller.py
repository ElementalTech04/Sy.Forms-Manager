from fastapi import APIRouter

from src.model.form_submission_request import FormSubmissionRequest
from src.service.contact_form_service import ContactFormService
from src.utils.validation_utils import ValidationUtils

router = APIRouter()


@router.post("/submit")
def submit_contact_form(self, formRequest: FormSubmissionRequest):
    validation_failed_response = {}
    contact_form_service = ContactFormService()
    contact_form_service.save_contact_form(formRequest)
    return {"message": "This is Endpoint 1"}


@router.post("/partner/partnerId/submitForm")
def submit_partner_form(self, formRequest: FormSubmissionRequest):
    validation_failed_response = {}
    if (ValidationUtils.field_exists_in_database())

