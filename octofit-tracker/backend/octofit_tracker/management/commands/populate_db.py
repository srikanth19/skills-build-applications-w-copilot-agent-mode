from django.core.management.base import BaseCommand
from django.conf import settings

from django.db import connections
from pymongo import ASCENDING

from django.contrib.auth.models import User

import random

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        db = connections['default'].cursor().db_conn
        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Teams
        teams = [
            {"name": "Team Marvel", "description": "Marvel superheroes"},
            {"name": "Team DC", "description": "DC superheroes"}
        ]
        team_ids = db.teams.insert_many(teams).inserted_ids

        # Users
        users = [
            {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": team_ids[0]},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": team_ids[0]},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": team_ids[1]},
            {"name": "Batman", "email": "batman@dc.com", "team": team_ids[1]},
        ]
        user_ids = db.users.insert_many(users).inserted_ids
        db.users.create_index([("email", ASCENDING)], unique=True)

        # Activities
        activities = [
            {"user": user_ids[0], "type": "run", "distance": 5, "duration": 30},
            {"user": user_ids[1], "type": "cycle", "distance": 20, "duration": 60},
            {"user": user_ids[2], "type": "swim", "distance": 2, "duration": 40},
            {"user": user_ids[3], "type": "run", "distance": 10, "duration": 50},
        ]
        db.activities.insert_many(activities)

        # Workouts
        workouts = [
            {"name": "Morning Cardio", "suggested_for": [user_ids[0], user_ids[2]]},
            {"name": "Strength Training", "suggested_for": [user_ids[1], user_ids[3]]},
        ]
        db.workouts.insert_many(workouts)

        # Leaderboard
        leaderboard = [
            {"user": user_ids[0], "points": 100},
            {"user": user_ids[1], "points": 90},
            {"user": user_ids[2], "points": 110},
            {"user": user_ids[3], "points": 95},
        ]
        db.leaderboard.insert_many(leaderboard)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
