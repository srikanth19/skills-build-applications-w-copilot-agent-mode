from django.test import TestCase
from .models import UserProfile, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        self.assertEqual(str(team), 'Test Team')
    def test_userprofile_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        user = UserProfile.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')
    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        user = UserProfile.objects.create(name='Test User', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, type='run', distance=5.0, duration=30)
        self.assertEqual(activity.type, 'run')
    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        user = UserProfile.objects.create(name='Test User', email='test@example.com', team=team)
        workout = Workout.objects.create(name='Test Workout')
        workout.suggested_for.add(user)
        self.assertEqual(workout.name, 'Test Workout')
    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        user = UserProfile.objects.create(name='Test User', email='test@example.com', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)
