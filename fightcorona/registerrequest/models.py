
import logging
from django.db import models

logger = logging.getLogger(__name__)


request_type_options = (
    ('food_grocery', 'Food / Grocery'),
    ('medicine', 'Medicines'),
    ('feeling_sick', 'Feeling Sick'),
)

request_status_options = (
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('declined', 'Declined'),
)

food_grocery_type_options = (
    ('requestFood', 'Food'),
    ('requestGrocery', 'Grocery'),
    ('requestBoth', 'Both'),
)

class PeopleRequest(models.Model):
    request_type = models.CharField(choices=request_type_options, max_length=250)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    pin_code = models.IntegerField()
    city = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    request_status = models.CharField(choices=request_status_options, max_length=250, default='pending')

class RequestDetail(models.Model):
    request = models.OneToOneField(PeopleRequest, related_name='request_detail', blank=False,
                                   on_delete=models.deletion.CASCADE)
    no_of_people = models.IntegerField()
    food_grocery_type = models.CharField(blank=True, null=True, choices=food_grocery_type_options, max_length=250)
    food_grocery_type_detail = models.CharField(blank=True, null=True, max_length=250)
    medicine_request_detail = models.CharField(blank=True, null=True, max_length=250)
    feeling_sick = models.BooleanField(blank=True, null=True)
