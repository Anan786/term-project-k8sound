import pytest

# Local modules
import playlist


@pytest.fixture
def pserv(request, playlist_url, auth):
    return playlist.Playlist(playlist_url, auth)


@pytest.fixture
def playlist_ex(request):
    return [1, 2, 3]  # TODO: Music IDs?


def test_simple_run(pserv, playlist_ex):
    # Test creation and reading
    first_playlist = [playlist_ex[0], playlist_ex[1]]
    trc, p_id = pserv.create(first_playlist)
    assert trc == 200
    trc, p_list = pserv.read(p_id)
    assert trc == 200 and p_list == first_playlist

    # Test updating
    trc = pserv.update(p_id, [playlist_ex[2]])
    assert trc == 200
    trc, p_list = pserv.read(p_id)
    assert trc == 200 and p_list == playlist_ex

    trc = pserv.delete(p_id)
    assert trc == 200
