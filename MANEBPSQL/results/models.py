# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Exams(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    firstname = models.CharField(max_length=20, blank=False, null=False)
    lastname = models.CharField(max_length=20, blank=False, null=False)
    sex = models.CharField(max_length=6, blank=False, null=False)
    agriculture = models.IntegerField()
    biology = models.IntegerField()
    chichewa = models.IntegerField()
    english = models.IntegerField()
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    geography = models.IntegerField()
    computerstudies = models.IntegerField()
    french = models.IntegerField()

    class Meta:
        db_table = 'exams'
