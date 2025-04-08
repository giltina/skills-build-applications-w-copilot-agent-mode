from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='user1@example.com', name='User One', age=20),
            User(email='user2@example.com', name='User Two', age=25),
            User(email='user3@example.com', name='User Three', age=30),
        ]
        for user in users:
            user.save()  # Save individually to populate primary keys

        # Create teams
        team = Team(name='Team Alpha')
        team.save()
        team.members.set(users)  # Associate users with the team

        # Create activities
        activities = [
            Activity(user=users[0], type='Running', duration=30, date=date.today()),
            Activity(user=users[1], type='Cycling', duration=60, date=date.today()),
            Activity(user=users[2], type='Swimming', duration=45, date=date.today()),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(team=team, points=100),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Morning Run', description='A quick morning run', duration=30),
            Workout(name='Evening Swim', description='Relaxing swim in the evening', duration=45),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))