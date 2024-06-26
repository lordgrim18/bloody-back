from django.db import models
from auth_setup.models import User
import uuid

class Role(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='role_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='role_updated_by')

    class Meta:
        ordering = ['name']

class UserRoleLink(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_role_link')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_role_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_role_updated_by')

    class Meta:
        ordering = ['role']

class Blood_Group(models.Model):
    id = models.CharField(max_length=36, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blood_group_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blood_group_updated_by')

    class Meta:
        ordering = ['name']

class District(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='district_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='district_updated_by')

    class Meta:
        ordering = ['name']

class City(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True, blank=False)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='city_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='city_updated_by')

    class Meta:
        ordering = ['district', 'name']

class Organization(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True, blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organization_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organization_updated_by')

    class Meta:
        ordering = ['city', 'name']

class UserOrganizationLink(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_organization_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_organization_updated_by')

    class Meta:
        ordering = ['organization']

class Donor(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=15, unique=True, blank=False)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    date_of_birth = models.DateField(blank=False)
    blood_group = models.ForeignKey(Blood_Group, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donor_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donor_updated_by')

    class Meta:
        ordering = ['blood_group', 'city', 'name']

class Patient(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True, blank=False)
    bystander_name = models.CharField(max_length=255, blank=False)
    bystander_phone_number = models.CharField(max_length=15, blank=False)
    hospital_name = models.CharField(max_length=255, blank=False)
    blood_group = models.ForeignKey(Blood_Group, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_updated_by')

    class Meta:
        ordering = ["updated_at", "blood_group", "city", "name"]

class Request(models.Model):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, blank=False, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='request_updated_by')

    class Meta:
        ordering = ['status', 'created_at']