"""
Python API for the playlist service.
"""

import requests

KEY_AUTH = 'Authorization'
KEY_OWNER_ID = 'OwnerId'
KEY_M_IDS = 'MusicIds'


class Playlist():
    """Python API for the playlist service.
    """
    def __init__(self, url, auth):
        self._url = url
        self._auth = auth

    # TODO: Fix params once figured out (Array or single ID)
    # Also, will have to figure out how to delete music from playlist
    def update(self, p_id, uid, m_ids):
        r = requests.put(
            self._url + p_id,
            json={
                KEY_OWNER_ID: uid,
                KEY_M_IDS: m_ids,
                },
            headers={KEY_AUTH: self._auth}
        )
        return r.status_code

    def create(self, uid, m_ids):
        r = requests.post(
            self._url,
            json={
                KEY_OWNER_ID: uid,
                KEY_M_IDS: m_ids,
            },
            headers={KEY_AUTH: self._auth}
        )
        return r.status_code, r.json()['playlist_id']

    def delete(self, p_id):
        r = requests.delete(
            self._url + p_id,
            headers={KEY_AUTH: self._auth}
        )
        return r.status_code

    def get(self, p_id):
        r = requests.get(
            self._url + p_id,
            headers={KEY_AUTH: self._auth}
        )
        if r.status_code != 200:
            return r.status_code, None
        item = r.json()['Items'][0]
        return r.status_code, item['MusicIds']

    def getAll(self):
        r = requests.get(
            self._url,
            headers={KEY_AUTH: self._auth}
        )
        items = r.json()
        if 'Count' not in items:
            return r.status_code, 0
        return r.status_code, items['Count']
