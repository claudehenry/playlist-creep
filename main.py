import requests

# test

def PLC:

    def get_auth():
        # todo switch to AuthCode flow with refresh to allow for update
        audata = {
            "client_id": "3347ef90343c41678fbf8b8879d8299d",
            "responce_type": "token",
            "redirect_uri": "http://35.181.67.120/playlist-creep",
        }
        auth_request = requests.get("https://accounts.spotify.com/authorize",params=audata)
        return auth_request.text

    def do():
        if not auth:
            return get_auth()
        return "success"

# playlist_id = "40dItKjpTvV8jb4U1J0ykm"
# url = "https://api.spotify.com/v1/playlists/{}/tracks".format(playlist_id)
# print(url)
# pl_request = requests.get(url)
# print(pl_request.text)
