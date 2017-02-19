from __future__ import unicode_literals
from django.db import models

class UserProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.OneToOneField(AUTH_USER_MODEL)
    blocked = models.IntegerField(default=0)
    email_verified
    username
    gender
    location
    address
    timezone
    preferred_currency
    father
    mother
    spouse
    birth = models.DateTimeField()
    death = models.DateTimeField()

    @property
    def full_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email

    @property
    def username(self):
        return self.user.email

    @property
    def age(self):
        return calculate_age(self.birth)

    def is_adult(self):
        return False;

    def aadhar(self):
        try:
            aadhar = UserAadhar.objects.get(user_profile=self).aadhar
            return aadhar

    def primary_phone_number(self):
        try:
            phone_number = UserPhoneNumber.objects.get(user_profile=self, primary=True).phone_number
            return phone_number
        except UserPhoneNumber.DoesNotExist:
            return ''

    def primary_phone_calling_code(self):
        try:
            return UserPhoneNumber.objects.get(user_profile=self, primary=True).calling_code
        except UserPhoneNumber.DoesNotExist:
            return ''

    def primary_phone_verified(self):
        try:
            verified = UserPhoneNumber.objects.get(user_profile=self, primary=True).verified
            return verified
        except UserPhoneNumber.DoesNotExist:
            return False

    def primary_language(self):
        try:
            language = UserLanguage.objects.get(user_profile=self, primary=True).language
            return language
        except UserLanguage.DoesNotExist:
            return ''

class UserAadhar(models.Model):
    class Meta:
        get_latest_by = "created"
        ordering = ['-created']
        unique_together = ('user_profile', 'aadhar')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    user_profile = models.ForeignKey(UserProfile)
    aadhar = models.CharField(max_length=100, default=None)

class UserPan(models.Model):
    class Meta:
        get_latest_by = "created"
        ordering = ['-created']
        unique_together = ('user_profile', 'pan')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    user_profile = models.ForeignKey(UserProfile)
    pan = models.CharField(max_length=100, default=None)

class UserPhoneNumber(models.Model):
    class Meta:
        get_latest_by = "created"
        ordering = ['-created']
        unique_together = ('user_profile', 'phone_number',)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    uuid = UUIDField(auto=True, primary_key=True)
    user_profile = models.ForeignKey(UserProfile)
    phone_number = models.CharField(max_length=100)
    calling_code = models.CharField(max_length=10, default="91")
    verified = models.BooleanField(default=False)
    verification_uid = models.CharField(max_length=10, blank=True, null=True)
    primary = models.BooleanField(default=False)
    last_verified_at = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return unicode("(%s)%s"%(self.calling_code, self.phone_number))

class UserLanguage(models.Model):
    language = models.ForeignKey(Language)
    user_profile = models.ForeignKey(UserProfile)
    primary = models.BooleanField(default=False)
