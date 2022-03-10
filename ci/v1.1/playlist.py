"""
Python API for the playlist service.
"""

import requests

KEY_AUTH = 'Authorization'
KEY_M_IDS = 'MusicIds'


class Playlist():
    """Python API for the playlist service.
    """
    def __init__(self, url, auth):
        self._url = url
        self._auth = auth

    # TODO: Fix params once figured out (Array or single ID)
    # Also, will have to figure out how to delete music from playlist
    def update(self, p_id, m_ids):
        r = requests.put(
            self._url + p_id,
            json={
                KEY_M_IDS: m_ids,
                },
            headers={KEY_AUTH: self._auth}
        )
        return r.status_code

    def create(self, m_ids):
        r = requests.post(
            self._url,
            json={
                KEY_M_IDS: m_ids,
                },
            headers={KEY_AUTH: self._auth}
        )
        return r.status_code, r.json()['playlist_id']

    def delete(self, p_id):
        r = requests.delete(
            self._url,
            headers={KEY_AUTH: self._auth}
        )
        return r.status_code

    def get(self, p_id):
        r = requests.get(
            self._url + p_id,
            headers={KEY_AUTH: self._auth}
        )
        return r.status_code, r.json()['Playlist']  # TODO: Temporary Key