"""
Python API for the user service.
"""

# Standard library modules

# Installed packages
import requests


class User():
    """Python API for the music service.

    Handles the details of formatting HTTP requests and decoding
    the results.

    Parameters
    ----------
    TODO: fill this parameters
    """
    def __init__(self, url, auth):
        self._url = url
        self._auth = auth

    def create(self, lname, email, fname):
        r = requests.post(
            self._url,
            json={"objtype": "user",
                  "lname": lname,
                  "email": email,
                  "fname": fname},
            headers={'Authorization': self._auth}
        )
        return r.status_code, r.json()['user_id']

    def read(self, user_id):
        """Read an user info.

        Parameters
        ----------
        TODO: fill this parameters
        """
        r = requests.get(
            self._url + user_id,
            headers={'Authorization': self._auth}
            )
        if r.status_code != 200:
            return r.status_code, None, None, None

        item = r.json()['Items'][0]
        return r.status_code, item['lname'], item['email'], item['fname']

    def delete(self, user_id):
        """Delete an user info.

        Parameters
        ----------
        TODO: fill this parameters
        """
        requests.delete(
            self._url + user_id,
            headers={'Authorization': self._auth}
        )

    def update(self, lname, email, fname, user_id):
        """Update an user info.

        Parameters
        ----------
        TODO: fill this parameters
        """
        r = requests.put(
            self._url + user_id,
            json={"lname": lname,
                  "email": email,
                  "fname": fname},
            headers={'Authorization': self._auth}
        )
        return r.status_code
