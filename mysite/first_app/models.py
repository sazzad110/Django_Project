from django.db import models

# Create your models here.
class Muscian(models.Model):
    # id = models.AutoField(Primary_key=True) # hidden auto create hobe
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=38)
    instrument = models.CharField(max_length=48)

    def __str__(self):
        return self.first_name

class Album(models.Model):
    artist = models.ForeignKey(Muscian,on_delete=models.CASCADE)        # foreign key
    name = models.CharField(max_length=49)
    release_date = models.DateField()
    nums_stars = models.IntegerField()
