from rest_framework import serializers
from .models import UserProfile, Team, Activity, Workout, Leaderboard
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return ObjectId(data)

class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    class Meta:
        model = Team
        fields = ['id', 'name', 'description']

class UserProfileSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    team = TeamSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'team']

class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'type', 'distance', 'duration']

class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    suggested_for = UserProfileSerializer(many=True, read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'suggested_for']

class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdField(source='_id', read_only=True)
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'points']
