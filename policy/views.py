from utils.custom_class_view import CustomClassView
from django.http import JsonResponse
from .models import Policy
from utils.custom_responses import HttpResponseUnprocessable
# Create your views here.


class PolicyView(CustomClassView):

    required_fields = ["type", "premium", "cover"]

    def post(self, request, *args, **kwargs):
        Policy.objects.create(**self.request_data)
        return JsonResponse({"message": "Policy successfully created"})

    def validate(self):
        """
            Validations for the fields
        """

        premium = self.request_data['premium']
        cover = self.request_data['cover']

        if not isinstance(premium, int):
            return HttpResponseUnprocessable("The field premium should be integer")
        if not isinstance(cover, int):
            return HttpResponseUnprocessable("The field cover should be integer")

    def convert(self):
        """
            Convert required fields to thier respective format
        """
        self.request_data['premium_type'] = self.request_data['type']
        del self.request_data['type']
