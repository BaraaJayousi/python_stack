from django.shortcuts import render, redirect
from django.db.models import Q

from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		
		#Query 1 all baseball leagues
		#"leagues": League.objects.filter(sport='Baseball')

		#Query 2: .all womens' leagues
		#"leagues": League.objects.filter(name__icontains= 'women')

		#Query 3: all leagues where sport is any type of hockey
		# "leagues": League.objects.filter(sport__icontains='hockey')

		# Query 4: all leagues where sport is something OTHER THAN football
		# "leagues": League.objects.exclude(sport__icontains = 'football')

		# Query 5: all leagues that call themselves "conferences"
		# "leagues": League.objects.filter(name__icontains = 'conference')


		# Query 6: .all leagues in the Atlantic region
		# "leagues": League.objects.filter(name__icontains = 'atlantic'),

		# Query 7: all teams based in Dallas
		# "teams": Team.objects.filter(location="Dallas")

		# Query 8: .all teams named the Raptors
		# "teams": Team.objects.filter(team_name="Raptors") ---> Couldn't find a team with that name

		# Query 9: all teams whose location includes "City"
		# "teams": Team.objects.filter(location__icontains="city") ---> Coudn't find a team in such city

		# Query 10: all teams whose names begin with "T"
		# "teams": Team.objects.filter(team_name__startswith="T")

		# Query 11: all teams, ordered alphabetically by location
		# "teams": Team.objects.order_by("location")

		# Query 12: all teams, ordered by team name in reverse alphabetical order
		# "teams": Team.objects.order_by("-team_name")


		# Query 13: .every player with last name "Cooper"
		# "players": Player.objects.filter(last_name="Cooper")

		# Query 14: every player with first name "Joshua"
		# "players": Player.objects.filter(first_name="Joshua")

		# Query 15: every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
		# "players": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")

		# Query 16: all players with first name "Alexander" OR first name "Wyatt"
		# "players": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt"))
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")