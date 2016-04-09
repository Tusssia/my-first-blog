from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #słowko klucz, oznacza obiekt, w ktorym jestem
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #metoda str - jak zrobimy print Post to ona sie wykona
        return self.title #tu zwraca i się kończy funkcja
