from django.db import models

class Car(models.Model):
    marke               = models.CharField(max_length=100)
    modell              = models.CharField(max_length=100)
    baujahr             = models.PositiveIntegerField()
    farbe               = models.CharField(max_length=50)
    kilometer           = models.PositiveIntegerField()
    unfallhistorie      = models.CharField(max_length=5, choices=[('keine','Keine'),('ja','Ja')])
    preis               = models.PositiveIntegerField()
    kraftstoffart       = models.CharField(max_length=10, choices=[('benzin','Benzin'),('diesel','Diesel')])
    getriebe            = models.CharField(max_length=10, choices=[('manuell','Manuell'),('automatik','Automatik')])
    au_hu               = models.DateField()
    leistung            = models.PositiveIntegerField()
    gewicht             = models.PositiveIntegerField()
    hubraum             = models.FloatField()
    vin                 = models.CharField(max_length=50, unique=True)
    ausstattung         = models.JSONField(default=list)
    extras              = models.JSONField(default=list)
    sonstigeMerkmale    = models.TextField(blank=True)

    def __str__(self):
        return f"{self.marke} {self.modell}"

class CarImage(models.Model):
    car   = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/%Y/%m/%d/')

    def __str__(self):
        return f"Image for {self.car} – {self.image.name}"
