from django.views import generic
from gamerank.wrapper import Wrapper as W
from igdb.igdbapi_pb2 import GameResult, CoverResult
from requests import post


class HomeView(generic.TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        options = "fields name; limit 10;"
        byte_array = W.wrapper.api_request("games.pb", options)
        games_message = GameResult()
        games_message.ParseFromString(byte_array)
        games = [game.name for game in games_message.games]
        print(games)
        context = {"games": games}
        options = "fields url; limit 10;"
        byte_array = W.wrapper.api_request
        byte_array = W.wrapper.api_request("covers.pb", options)
        games_message = CoverResult()
        games_message.ParseFromString(byte_array)
        covers = [cover.url for cover in games_message.covers]
        context = {"games" : games, "covers": covers}
        return context
