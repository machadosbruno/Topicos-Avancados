from django.db import models

class Reservation(models.Model):
    court_name = models.CharField(max_length=100)
    player_name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    duration_minutes = models.IntegerField()
    def __str__(self):
        return f"Reserva para {self.player_name} na {self.court_name} na data {self.reservation_date}"