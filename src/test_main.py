from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_simple():
    for o in ["add", "sub", "div", "mul"]:
        response = client.get(f"/v1/problem/math/simple/{o}")
        assert response.status_code == 200
        assert len(response.json()) == 25

        for p in response.json():
            assert p["type"] == "simple"
            assert p["operator"] == o
            assert p["users_answer"] is None
            assert "solution" in p
            assert isinstance(p["numbers"], list)
            assert len(p["numbers"]) == 2


def test_simple_no_of_problems():
    response = client.get(f"/v1/problem/math/simple/add?no_of_problems=1")
    assert response.status_code == 200
    assert len(response.json()) == 1

    response = client.get(f"/v1/problem/math/simple/add?no_of_problems=100")
    assert response.status_code == 200
    assert len(response.json()) == 100

    # Must be positive int
    response = client.get(f"/v1/problem/math/simple/add?no_of_problems=0")
    assert response.status_code == 422

    # No more than 100 problems pr. request
    response = client.get(f"/v1/problem/math/simple/add?no_of_problems=101")
    assert response.status_code == 422
