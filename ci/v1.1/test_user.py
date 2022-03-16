# Installed packages
import pytest

# Local modules
import user


@pytest.fixture
def userv(request, user_url, auth):
    return user.User(user_url, auth)


@pytest.fixture
def user_info(request):
    return ('Jobs', 'stevejobs@apple.com', 'Steve')


@pytest.fixture
def info_update(request):
    return ('Cook', 'timcook@apple.com', 'Tim')


def test_simple_run(userv, user_info, info_update):
    trc, u_id = userv.create(user_info[0], user_info[1], user_info[2])
    assert trc == 200
    trc, lname, email, fname = userv.read(u_id)
    assert trc == 200 and lname == user_info[0] and \
        email == user_info[1] and fname == user_info[2]
    trc = userv.update(info_update[0], info_update[1], info_update[2], u_id)
    assert trc == 200
    trc, lname, email, fname = userv.read(u_id)
    assert trc == 200 and lname == info_update[0] and \
        email == info_update[1] and fname == info_update[2]
    userv.delete(u_id)
    # No status to check
