from fastapi import APIRouter, Request

from src.constants import *
from src.model.form_submission_request import FormSubmissionRequest
from src.service.contact_form_service import ContactFormService
from src.utils.validation_utils import ValidationUtils

router = APIRouter()


# Global variables
email_invalid_message = "Email is not valid"
spam_check_failed_message = "Nice try, but you are not allowed to submit this form"


@router.post("/submit")
def submit_contact_form(request: Request, form_request: FormSubmissionRequest):
    validation_failed_response = {}
    if (ValidationUtils.is_valid_email(form_request.email)):
        validation_failed_response["errorMessage"] = email_invalid_message
        validation_failed_response["status"] = FormSubmissionStatus.FAILED
        validation_failed_response["statusCode"] = HTTPStatusCodes.BAD_REQUEST
        return validation_failed_response

    if(ValidationUtils.check_spam_on_db(request.headers.get('User-Agent'), request.client.host)):
        validation_failed_response["errorMessage"] = spam_check_failed_message
        validation_failed_response["status"] = FormSubmissionStatus.FAILED
        validation_failed_response["statusCode"] = HTTPStatusCodes.FORBIDDEN
        return validation_failed_response

    form_service = ContactFormService()
    save_response = {}

    try:
        save_response = form_service.save_form(form_request)
    except Exception as e:
        print(e)
        validation_failed_response["errorMessage"] = e
        validation_failed_response["status"] = FormSubmissionStatus.FAILED
        validation_failed_response["statusCode"] = HTTPStatusCodes.INTERNAL_SERVER_ERROR
        return validation_failed_response

    response = {"data", save_response, "statusCode", HTTPStatusCodes.CREATED, "status", FormSubmissionStatus.SUCCESS}

    return response
