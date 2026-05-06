def test_unregister_success(client, reset_activities):
    """Test successful unregister from an activity."""
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already registered
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/unregister?email={email}"
    )
    
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"


def test_unregister_not_signed_up(client, reset_activities):
    """Test unregister fails when student is not signed up."""
    # Arrange
    activity_name = "Chess Club"
    email = "notstudent@mergington.edu"  # Not registered
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/unregister?email={email}"
    )
    
    # Assert
    assert response.status_code == 400
    assert "not signed up" in response.json()["detail"]


def test_unregister_activity_not_found(client, reset_activities):
    """Test unregister fails when activity does not exist."""
    # Arrange
    activity_name = "Nonexistent Activity"
    email = "student@mergington.edu"
    
    # Act
    response = client.post(
        f"/activities/{activity_name}/unregister?email={email}"
    )
    
    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_unregister_reflects_in_activities_list(client, reset_activities):
    """Test that unregister updates the activities list."""
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already registered
    
    # Act
    unregister_response = client.post(
        f"/activities/{activity_name}/unregister?email={email}"
    )
    activities_response = client.get("/activities")
    
    # Assert
    assert unregister_response.status_code == 200
    assert activities_response.status_code == 200
    activities_data = activities_response.json()
    assert email not in activities_data[activity_name]["participants"]
