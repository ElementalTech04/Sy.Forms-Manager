from src.model.form_submission import FormSubmission
from src.service.form_service import FormService



class ContactFormService(FormService):
    def __init__(self):
        super().__init__()

    def save_form(self, formRequest):
        form_submission = FormSubmission()

        form_submission.form_source_id = formRequest.site_id
        form_submission.form_data = formRequest.form_data
        form_submission.email_notification_id = formRequest.email_notification_id
        form_submission.is_spam = formRequest.is_spam
        form_submission.spam_associations = formRequest.spam_associations

        response = super().save_form(form_submission)
        return response

    def get_form(self, formRequest):
        form_submission = super().get_form_by_id(formRequest.form_id)
        return form_submission

    def get_forms(self, formRequest):
        form_submissions = super().get_all_forms(formRequest.filter_criteria)
        return form_submissions

    def delete_form(self, formRequest):
        success = super().delete_form_by_id(formRequest.form_id)
        return success

    def update_form(self, formRequest):
        form_submission = super().get_form_by_id(formRequest.form_id)
        if form_submission:
            form_submission.form_data = formRequest.form_data
            form_submission.email_notification_id = formRequest.email_notification_id
            form_submission.is_spam = formRequest.is_spam
            form_submission.spam_associations = formRequest.spam_associations
            response = super().update_form(form_submission)
            return response
        else:
            return None
