from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.team, 'Marvel')

    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', members=['A', 'B'])
        self.assertEqual(team.name, 'Test Team')
        self.assertIn('A', team.members)

    def test_activity_creation(self):
        activity = Activity.objects.create(user='Test User', activity='Running', duration=30)
        self.assertEqual(activity.activity, 'Running')

    def test_leaderboard_creation(self):
        lb = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(lb.points, 100)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.assertEqual(workout.name, 'Test Workout')
