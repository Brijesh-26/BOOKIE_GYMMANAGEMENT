from django.db import models

class Gym(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

    def get_short_address(self):
        return self.address[:50]

    @property
    def full_address(self):
        return f"{self.name} - {self.address}"

class Trainer(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    gym = models.OneToOneField(Gym, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def trainer_info(self):
        return f"{self.name} - {self.specialization} - Works at {self.gym.name}"


class Client(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def is_adult(self):
        return self.age >= 18

    def get_age_group(self):
        if self.age < 18:
            return "Child"
        elif 18 <= self.age < 30:
            return "Young Adult"
        elif 30 <= self.age < 50:
            return "Adult"
        else:
            return "Senior"
        
        
        
class WorkoutSession(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.client.name} - {self.trainer.name} - {self.date}"

    @property
    def total_duration(self):
        hours, remainder = divmod(self.duration, 60)
        return f"{hours} hours and {remainder} minutes"
