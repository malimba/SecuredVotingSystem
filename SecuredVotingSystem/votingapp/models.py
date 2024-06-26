from django.db import models

# Create your models here.
class VoteNominee(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='static/nomineephotos')
    position = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name