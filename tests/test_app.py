from fastapi.testclient import TestClient

from src.app import activities, app


def test_student_cannot_sign_up_twice_for_same_activity():
    client = TestClient(app)
    activity_name = "Chess Club"
    email = "duplicate-test@mergington.edu"

    first_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )
    assert first_response.status_code == 200

    second_response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email},
    )

    assert second_response.status_code == 400
    assert second_response.json()["detail"] == "Student is already signed up"
    assert activities[activity_name]["participants"].count(email) == 1
