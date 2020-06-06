from http import HTTPStatus
from django.http import HttpResponse


class HttpResponseWrongContentType(HttpResponse):
    status_code = HTTPStatus.UNSUPPORTED_MEDIA_TYPE


class HttpResponseUnprocessable(HttpResponse):
    status_code = HTTPStatus.UNPROCESSABLE_ENTITY
