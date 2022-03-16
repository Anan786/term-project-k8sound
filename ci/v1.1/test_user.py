# Installed packages
import pytest

# Local modules
import user


@pytest.fixture
def userv(request, user_url, auth):
    return user.User(user_url, auth)


@pytest.fixture
def user(request):
    return ('Jobs', 'stevejobs@apple.com', 'Steve')


@pytest.fixture
def user_update(request):
    return ('Cook', 'timcook@apple.com', 'Tim')


def test_simple_run(userv, user, user_update):
    trc, u_id = userv.create(user[0], user[1], user[2])
    assert trc == 200
    trc, lname, email, fname = userv.read(u_id)
    assert trc == 200 and lname == user[0] and email == user[1] and fname == user[2]
    trc = userv.update(user_update[0], user_update[1], user_update[2], u_id)
    assert trc == 200
    trc, lname, email, fname = userv.read(u_id)
    assert trc == 200 and lname == user[0] and email == user[1] and fname == user[2]
    userv.delete(u_id)
    # No status to check
