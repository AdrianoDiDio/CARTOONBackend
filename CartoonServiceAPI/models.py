from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator

class Camera(models.Model):
    Name = models.CharField(max_length=256)
    Position = models.PointField(srid=4326)
    IPv4 = models.GenericIPAddressField(protocol='IPv4')
    Port = models.PositiveIntegerField(validators=[MaxValueValidator(65535)])
    StreamName = models.CharField(max_length=512)
    
    def __str__(self):
        return self.Name
    class Meta:
        db_table = "Camera"
        managed = True
