from django.urls import path
from blood_group_view import Blood_Group_DropdownAPIView, Blood_Group_APIview

urlpatterns = [
        path('', Blood_Group_DropdownAPIView.as_view(), name='blood_group_list'), #drop down
        path('all/', Blood_Group_APIview.as_view(), name='blood_group_detail'), #get
        path('create/', Blood_Group_APIview.as_view(), name='blood_group_create'), #single post

    ]