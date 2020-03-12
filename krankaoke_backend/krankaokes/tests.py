import pytest
import tempfile
from rest_framework.test import APIClient

from krankaokes.models import Krankaoke


@pytest.mark.django_db
def test_krankaoke_timings_storage(create_user):
    user = create_user
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Token " + user.auth_token.key)

    with tempfile.TemporaryFile() as fp:
        fp.write(bytes([1]))
        fp.seek(0)
        data = {
            "artist": "test",
            "title": "testtitle",
            "audio": fp,
            "user": user.id,
            "timings": '{"hello": [1000, 2000], "world": [2001, 3000]}',
        }
        response = client.post(
            "/api/v1/krankaokes/",
            data,
            format="multipart",
            headers={"Content-Type": "multipart/form-data"},
        )
    assert response.status_code == 201

    krankaoke = Krankaoke.objects.first()
    assert krankaoke.artist == "test"
    assert krankaoke.title == "testtitle"
    assert krankaoke.timings == {
        "hello": [1000, 2000],
        "world": [2001, 3000],
    }
