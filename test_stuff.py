import pytest

from main import is_pink, get_player_choice

def test_is_pink_true():
    assert is_pink("hot pink") == True
    assert is_pink("light pink") == True


def test_is_pink_false():
    assert is_pink("blue") == False
    assert is_pink("green") == False
    assert is_pink("red") == False


def test_is_pink_case_insensitive():
    # If you implemented lowercase handling
    assert is_pink("Hot Pink".lower()) == True
    assert is_pink("LIGHT PINK".lower()) == True

def test_valid_input(monkeypatch):
    # Simulate user typing "blue"
    monkeypatch.setattr("builtins.input", lambda _: "blue")
    
    color_list = [
        "red", "orange", "yellow", "green", "blue",
        "purple", "white", "hot pink", "black",
        "navy", "light pink"
    ]
    
    choice = get_player_choice(color_list)
    assert choice == "blue"


def test_invalid_then_valid_input(monkeypatch):
    # Simulate user typing invalid input first, then valid
    inputs = iter(["brown", "green"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    color_list = [
        "red", "orange", "yellow", "green", "blue",
        "purple", "white", "hot pink", "black",
        "navy", "light pink"
    ]
    
    choice = get_player_choice(color_list)
    assert choice == "green" 