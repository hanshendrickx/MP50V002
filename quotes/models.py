from django.db import models


class Quote(models.Model): 
    subject = models.CharField(max_length=200) 
    author = models.CharField(max_length=200)
    quote = models.CharField(max_length=272, default='Medicine is a science and an art.') 
    reference = models.URLField(max_length=200, blank=False, help_text="Create google search like https://www.google.com/search?q= and add author and subject to find the quote and its context.")
    year = models.IntegerField()

def __str__(self): 
    return self.subject
