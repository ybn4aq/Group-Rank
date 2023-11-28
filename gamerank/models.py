from django.db import models


class Game(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=200)
    # ranked_by = models.ForeignKey()
    average_ranking = models.FloatField(default=0.0)
    rank = models.IntegerField(default=0)
    cover_url = models.CharField(max_length=200)
