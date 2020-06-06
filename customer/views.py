from utils.custom_class_view import CustomClassView
from django.http import JsonResponse
from .models import Customer
from fintech_backend.constants import DATE_INPUT_FORMAT
from utils.custom_responses import HttpResponseUnprocessable
from datetime import datetime
# Create your views here.


class CustomerView(CustomClassView):

    required_fields = ["first_name", "last_name", "dob"]

    def post(self, request, *args, **kwargs):
        Customer.objects.create(**self.request_data)
        return JsonResponse({"mssage": "User successfully created"})

    def validate(self):
        """
            Validations for the fields
        """

        first_name = self.request_data['first_name']
        last_name = self.request_data['last_name']
        dob = self.request_data['dob']

        if not first_name[0].isalpha():
            return HttpResponseUnprocessable("The field first_name has to start with an alphabet")
        if not last_name[0].isalpha():
            return HttpResponseUnprocessable("The field last_name has to start with an alphabet")
        try:
            datetime.strptime(dob, DATE_INPUT_FORMAT)
        except ValueError:
            return HttpResponseUnprocessable("The field dob should be of the format dd-mm-yyyy")

    def convert(self):
        """
            Convert required fields to thier respective format
        """
        self.request_data['dob'] = datetime.strptime(self.request_data['dob'], DATE_INPUT_FORMAT)
