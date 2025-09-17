from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.


def validate_pdf(file):
    if not file.name.endswith('.pdf'):
        raise ValidationError("Only PDF files are allowed.")
    return file


class Resume(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    resume_file = models.FileField(upload_to='resumes/', validators=[validate_pdf])


