from django.contrib import admin

from registerrequest.models import PeopleRequest, RequestDetail


class PeopleRequestAdmin(admin.ModelAdmin):
    list_display = (
        'request_type',
        'name',
        'address',
        'pin_code',
        'city',
        'phone_number',
        'request_status',
    )

class RequestDetailAdmin(admin.ModelAdmin):
    list_display = (
        'no_of_people',
        'food_grocery_type',
        'food_grocery_type_detail',
        'medicine_request_detail',
        'feeling_sick',
    )

admin.site.register(PeopleRequest, PeopleRequestAdmin)
admin.site.register(RequestDetail, RequestDetailAdmin)
