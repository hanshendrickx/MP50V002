import uuid # new
from django.db import models
from django.urls import reverse


class Quote(models.Model):
    id = models.UUIDField( # new 
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False)
    subject = models.CharField(max_length=200) 
    author = models.CharField(max_length=200)
    quote = models.CharField(max_length=272, default='Medicine is a science and an art.') 
    reference = models.URLField(max_length=200, blank=False, help_text="No spaces, use '+'. Create google search like https://www.google.com/search?q= and add author and subject to find the quote and its context.")
    year = models.IntegerField()

    def __str__(self):
        return self.subject

    def get_absolute_url(self): # new 
        return reverse('quote_detail', args=[str(self.id)])       