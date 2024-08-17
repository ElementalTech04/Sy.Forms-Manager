from enum import Enum

class HTTPStatusCodes(Enum):
    BAD_REQUEST = '400'
    INTERNAL_SERVER_ERROR = '400'
    FORBIDDEN = '403'
    OK = '200'
    CREATED = '201'
    NO_CONTENT = '204'

class FormSubmissionStatus(Enum):
    SUCCESS = 'success'
    FAILED = 'failed'

class FormType(Enum):
    CONTACT = 'contact'
    GENERAL = 'general'
