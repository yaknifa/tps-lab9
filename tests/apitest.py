import requests
import pytest

URL = "https://jsonplaceholder.typicode.com"

class TestApi:
    def test_get_post(self):
        r = requests.get(f"{URL}/posts/1", timeout=10)
        assert r.status_code == 200

    def test_post_fields(self):
        r = requests.get(f"{URL}/posts/1", timeout=10)
        d = r.json()
        assert "id" in d
        assert "title" in d
        assert "userId" in d

    def test_create_post(self):
        pld = {"title": "CI Test Post", "body": "Automated pipeline run", "userId": 1}
        r = requests.post(f"{URL}/posts", json=pld, timeout=10)
        assert r.status_code == 201
        assert r.json()["title"] == "CI Test Post"
