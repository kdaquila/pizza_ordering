from django.db import models


class Pizza(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField(null=True)
    stop_time = models.DateTimeField(null=True)

    class Meta:
        db_table = "pizza"
        app_label = "pizza"

    def __str__(self):
        return self.name
