# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Art(models.Model):
    owner = models.ForeignKey('User', models.DO_NOTHING, db_column='owner')
    price = models.IntegerField()
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    thumb = models.TextField()
    time = models.DateTimeField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'art'


class User(models.Model):
    uid = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'user'
