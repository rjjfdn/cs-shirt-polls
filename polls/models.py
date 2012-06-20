from django.db import models

class Student(models.Model):
    id_number = models.IntegerField()
    last_name = models.TextField()
    first_name = models.TextField()
    middle_initial = models.TextField()
    year = models.IntegerField()
    gender = models.TextField()
    course = models.TextField()
    section = models.TextField()
    voted = models.IntegerField()

    def __unicode__(self):
        return str(self.id_number)

class Choice(models.Model):
    choice_number = models.IntegerField()
    votes = models.IntegerField()

    def __unicode__(self):
        return str(self.choice_number)
