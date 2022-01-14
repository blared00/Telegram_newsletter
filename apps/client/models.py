from django.db import models


class Contact(models.Model):
    """Данные пользователей"""
    name = models.CharField(max_length=128)
    email = models.EmailField()

    class Meta:
        verbose_name = "клиента"
        verbose_name_plural = "Контакты клиентов"

    def __str__(self):
        return self.name
