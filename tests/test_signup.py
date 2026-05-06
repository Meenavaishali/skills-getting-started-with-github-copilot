def test_signup_success(client, reset_activities):
    """Test successful signup for an activity."""
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for {activity_name}"


def test_signup_already_registered(client, reset_activities):
    """Test signup fails when student is already registered."""
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already registered
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    
    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_activity_not_found(client, reset_activities):
    """Test signup fails when activity does not exist."""
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "student@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_signup_reflects_in_activities_list(client, reset_activities):
    """Test that signup updates the activities list."""
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"
    
    # Act
    signup_response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    activities_response = client.get("/activities")
    
    # Assert
    assert signup_response.status_code == 200
    assert activities_response.status_code == 200
    activities_data = activities_response.json()
    assert email in activities_data[activity_name]["participants"]
