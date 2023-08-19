import json

from pydantic import BaseModel


class FormSubmissionRequest(BaseModel):
    form_submission_id: int
    form_source_id: int
    form_data: json
    from_email: str
    to_email: str

