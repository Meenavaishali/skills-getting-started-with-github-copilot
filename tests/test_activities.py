def test_get_activities_success(client, reset_activities):
    """Test retrieving all activities."""
    # Arrange
    # Activities already loaded via reset_activities fixture
    
    # Act
    response = client.get("/activities")
    
    # Assert
    assert response.status_code == 200
    activities_data = response.json()
    assert "Chess Club" in activities_data
    assert "Programming Class" in activities_data
    assert "Gym Class" in activities_data
    assert len(activities_data) == 3


def test_get_activities_contains_participant_info(client, reset_activities):
    """Test that activities list includes participant information."""
    # Arrange
    # Activities already loaded via reset_activities fixture
    
    # Act
    response = client.get("/activities")
    
    # Assert
    activities_data = response.json()
    chess_club = activities_data["Chess Club"]
    assert "participants" in chess_club
    assert "michael@mergington.edu" in chess_club["participants"]
    assert "daniel@mergington.edu" in chess_club["participants"]
    assert chess_club["max_participants"] == 12
