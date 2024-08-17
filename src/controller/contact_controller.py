from fastapi import APIRouter

from src.model.form_submission_request import FormSubmissionRequest
from src.service.form_service import ContactFormService
from src.utils.validation_utils import ValidationUtils

router = APIRouter()


@router.post("/submit")
def submit_contact_form(self, formRequest: FormSubmissionRequest):
    validation_failed_response = {}
    if (ValidationUtils.is_valid_email(formRequest.email)):
        validation_failed_response["errorMessage"] = "Email is not valid"
        validation_failed_response["status"] = "failed"
        validation_failed_response["statusCode"] = "400"
        return validation_failed_response

    if (ValidationUtils.check_http_header(self.request.headers["requestor"])):
        validation_failed_response["errorMessage"] = "Invalid HTTP header"
        validation_failed_response["status"] = "failed"
        validation_failed_response["statusCode"] = "400"
        return validation_failed_response
    contact_form_service = ContactFormService()
    contact_form_service.save_contact_form(formRequest)
    return {"message": "This is Endpoint 1"}


@router.post("/partner/partnerId/submitForm")
def submit_general_form(self, formRequest: FormSubmissionRequest):
    validation_failed_response = {}
    if (ValidationUtils.field_exists_in_database())

