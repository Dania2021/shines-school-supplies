from django.db import models


class Subscriber(models.Model):
    """ Newsletter model """

    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
