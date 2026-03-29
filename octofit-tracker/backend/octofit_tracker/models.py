from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=50)
    distance = models.FloatField()
    duration = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    suggested_for = models.ManyToManyField(UserProfile, related_name='workouts')

class Leaderboard(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='leaderboard_entries')
    points = models.IntegerField()
