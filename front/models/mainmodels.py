from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    owner = models.OneToOneField(User,
                                 on_delete=models.CASCADE,
                                 related_name="card"
                                 )
    balance = models.CharField(max_length=255)

class Index(models.Model):
    name = models.CharField(max_length=255)
    tax = models.CharField(max_length=255)

class IndexCoins(models.Model):
    index = models.ForeignKey(Index,
                              on_delete=models.CASCADE,
                              related_name='coin_indexes',
                              )
    coin = models.CharField(max_length=255)

class IndexOwner(models.Model):
    index = models.ForeignKey(Index,
                              on_delete=models.CASCADE,
                              related_name='owner_indexes',
                              )
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='index_owners',
                              )



