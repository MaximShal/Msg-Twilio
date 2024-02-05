from django.db import models
from uuid import uuid4
from django.utils import timezone


class Order(models.Model):
    slug = models.UUIDField(default=uuid4, editable=False, unique=True)
    start_timestamp = models.PositiveIntegerField()
    end_timestamp = models.PositiveIntegerField()
    user_email = models.EmailField()
    user_name = models.CharField(max_length=255)
    cell_id = models.IntegerField()
    reminded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"Rental {self.pk} - {self.user_name}"

    def start_datetime(self):
        return timezone.datetime.fromtimestamp(self.start_timestamp).strftime('%d.%m.%y %H:%M')

    def end_datetime(self):
        return timezone.datetime.fromtimestamp(self.end_timestamp).strftime('%d.%m.%y %H:%M')
