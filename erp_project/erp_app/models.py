from django.contrib.postgres.fields import JSONField
from django.db import models
from django.contrib.auth.models import User, Group
import secrets
from django import forms
from django.utils import timezone

STATUS_CHOICES = [
    ('Sent', 'Sent'),
    ('Received', 'Received'),

]
ADDRESSEE_CHOICES = [
    ('ceo', 'CEO'),
    ('cto', 'CTO'),
    ('pm', 'Project Manager'),

]

PROGRESS_CHOICES = [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Done', 'Done'),

]
RECIPIENT_CHOICES = [
    ('ceo', 'CEO'),
    ('cto', 'CTO'),
    ('pm', 'Project Manager'),
    ('','')

]


def generate_tracking_code():
    while True:
        code = secrets.SystemRandom().randrange(100000, 999999)
        if not Letter.objects.filter(tracking_code=code).exists():
            return code


class Letter(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reci_get=models.CharField(max_length=15,null=True)
    recipient = models.CharField(max_length=50, choices=RECIPIENT_CHOICES)
    title = models.CharField(max_length=40, default='Title')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tracking_code = models.IntegerField(unique=True, default=generate_tracking_code)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Sent')
    is_read = models.BooleanField(default=False)
    opened_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='opened_letters')
    messages = models.TextField(default='There is no messages.')
    additional_text = models.TextField(blank=True, null=True)
    referred_to_group = models.CharField(max_length=50, blank=True, null=True)
    progress = models.CharField(max_length=20, choices=PROGRESS_CHOICES, default='pending')
    actions_history = models.JSONField(default=list)


    def add_reference(self, referred_to_group, additional_text):
        letter_details = LetterDetails.objects.create(
            letter=self,
            referred_to_group=referred_to_group,
            additional_text=additional_text
        )
        letter_details.save()

    def __str__(self):
        return f"Letter from {self.user.username}  - for {self.recipient}   -   {self.tracking_code}"


class LetterDetails(models.Model):
    letter = models.ForeignKey(Letter, on_delete=models.CASCADE)
    referred_to_group = models.CharField(max_length=50, blank=True, null=True)
    additional_text = models.TextField(blank=True, null=True)
    is_done = forms.BooleanField(label='Done', required=False)
