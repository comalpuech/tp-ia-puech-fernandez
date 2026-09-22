from toolbox import is_palindrome, word_frequency, celsius_to_fahrenheit


def test_is_palindrome_simple():
    assert is_palindrome("radar") is True


def test_is_palindrome_with_spaces():
    assert is_palindrome("un roc si biscornu") is True  # échoue à cause du bug


def test_is_palindrome_false():
    assert is_palindrome("python") is False


def test_word_frequency_nominal():
    result = word_frequency("the cat and the dog")
    assert result == {"the": 2, "cat": 1, "and": 1, "dog": 1}


def test_word_frequency_case_insensitive():
    result = word_frequency("Hello HELLO hello")
    assert result == {"hello": 3}


def test_word_frequency_punctuation():
    result = word_frequency("Hello, world! Hello...")
    assert result == {"hello": 2, "world": 1}


def test_word_frequency_empty():
    result = word_frequency("")
    assert result == {}


def test_celsius_to_fahrenheit_freezing():
    assert celsius_to_fahrenheit(0) == 32.0


def test_celsius_to_fahrenheit_boiling():
    assert celsius_to_fahrenheit(100) == 212.0


def test_celsius_to_fahrenheit_body_temp():
    assert celsius_to_fahrenheit(37) == 98.6


def test_celsius_to_fahrenheit_negative():
    assert celsius_to_fahrenheit(-40) == -40.0


def test_celsius_to_fahrenheit_zero():
    assert celsius_to_fahrenheit(0) == 32.0
