import pytest

# Local modules
import playlist


@pytest.fixture
def pserv(request, playlist_url, auth):
    return playlist.Playlist(playlist_url, auth)


@pytest.fixture
def playlist_ex(request):
    return ['1', '2', '3']  # TODO: Music IDs?


# Uncomment lines when implemented
# This is more of an integration test
def test_simple_run(pserv, playlist_ex):
    # Test creation
    user_id = "dummy_uid"
    music_ids = [playlist_ex[0], playlist_ex[1]]
    trc, p_id = pserv.create(user_id, music_ids)
    assert trc == 200

    # Test list all playlists
    trc, items = pserv.getAll()
    p_list = []
    for i in items:
        if i['playlist_id'] == p_id:
            p_list = (i['MusicIds'])
    assert trc == 200 and set(p_list) == set(music_ids)

    # Test read one playlist
    trc, items = pserv.get(p_id)
    p_list = []
    for i in items:
        p_list = i['MusicIds']
    assert trc == 200 and set(p_list) == set(music_ids)

    # Test updating
    trc = pserv.update(p_id, [playlist_ex[2]])
    assert trc == 200
    trc, p_list = pserv.get(p_id)
    assert trc == 200 #and p_list == playlist_ex  # noqa E261 E262

    trc = pserv.delete(p_id)
    # assert trc == 200
    assert trc != 200  # TODO: Change when implemented
