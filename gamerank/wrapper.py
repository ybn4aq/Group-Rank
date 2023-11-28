from igdb.wrapper import IGDBWrapper
import requests
import json
from mysite.config import Keys


class Wrapper:
    keys = Keys()
    access_token = keys.twitch_access_token
    client_id = keys.twitch_client_id
    r = requests.post(
        "https://id.twitch.tv/oauth2/token?client_id="
        + client_id
        + "&client_secret="
        + access_token
        + "&grant_type=client_credentials"
    )
    access_token = json.loads(r._content)["access_token"]
    wrapper = IGDBWrapper(client_id, access_token)
