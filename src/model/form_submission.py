from pydantic import BaseModel, json


class FormSubmission(BaseModel):
    form_submission_id: int
    form_source_id: int
    form_data: json
    email_notification_id: int
    is_partner: bool
    partner_id: int
    is_spam: bool
    spam_associations: json
