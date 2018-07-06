from django.db import models
from accounts.models import User
from ckeditor_uploader.fields import RichTextUploadingField 

# Create your models here.
class Suggestion(models.Model):
    suggestion_choices = ((True, 'Feature'), (False, 'Bug Fix'))
    
    suggestion_type = models.BooleanField(blank=False, default=False, choices=suggestion_choices)
    user = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    title = models.CharField(max_length=200, blank=False)
    details = RichTextUploadingField()
    date_time = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return "{0}: {1}".format(self.user, self.title)
    
    