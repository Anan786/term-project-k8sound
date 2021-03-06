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
    assert trc == 200 and p_id and type(p_id) is str  # Check if p_id exists

    # Test list all playlists
    trc, total_records = pserv.getAll()
    assert trc == 200 and total_records == 1

    # Test read one playlist
    trc, p_list = pserv.get(p_id)
    assert trc == 200 and set(p_list) == set(music_ids)

    # Test updating
    trc = pserv.update(p_id, user_id, [playlist_ex[2]])
    assert trc == 200
    trc, p_list = pserv.get(p_id)
    assert trc == 200 and p_list == [playlist_ex[2]]

    # Test delete
    trc = pserv.delete(p_id)
    assert trc == 200
