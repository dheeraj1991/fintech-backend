import json
from abc import ABC, abstractmethod

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View

from fintech_backend.constants import CONTENT_TYPE
from .custom_responses import HttpResponseWrongContentType, HttpResponseUnprocessable


class CustomClassView(View, ABC):

    required_fields = []

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
            Override dispatch to accpet requests without csrf checks and beofer going to view
            adds a few internal checks
        """
        request_type_check = self.request_type_check(request)
        if request_type_check:
            return request_type_check

        self.request_data = self.extract_data(request)

        required_field_check = self.required_field_check()
        if required_field_check:
            return required_field_check

        null_or_empty_data_check = self.null_or_empty_data_check()
        if null_or_empty_data_check:
            return null_or_empty_data_check

        validation_response = self.validate()
        if validation_response:
            return validation_response

        self.convert()

        return super(CustomClassView, self).dispatch(request, *args, **kwargs)

    def request_type_check(self, request):
        """
            This is to check all the requests come with content-type json
        """
        content_type = request.META.get('CONTENT_TYPE')
        if content_type != CONTENT_TYPE:
            return HttpResponseWrongContentType("Wrong content_type passed")
        return None

    def extract_data(self, request):
        """
            POST request data is extracted for further checks
        """
        if request.method == 'POST':
            return json.loads(request.body)

    def required_field_check(self):
        """
            Check all fields required are passed and extra fileds are not added to the body
        """
        request_data_keys = self.request_data.keys()
        for key in request_data_keys:
            if key not in self.required_fields:
                return HttpResponseUnprocessable("The fields passed are invalid")

        missing_keys = []
        for key in self.required_fields:
            if key not in request_data_keys:
                missing_keys.append(key)

        if missing_keys:
            return HttpResponseUnprocessable("The following keys are required : {}".format(", ".join(missing_keys)))

    def null_or_empty_data_check(self):
        """
            Since all fields are mandatory check for fields which are empty or null
        """
        empty_fields = []
        for key in self.required_fields:
            if not self.request_data[key]:
                empty_fields.append(key)
        if empty_fields:
            return HttpResponseUnprocessable("The following fields are empty or null : {}".format(", ".join(empty_fields)))

    @abstractmethod
    def validate(self):
        pass

    def convert(self):
        pass
