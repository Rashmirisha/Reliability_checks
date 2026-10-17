
import pytest

from reliability_checks import (
    validate_labels,
    check_prediction_consistency,
)


def test_valid_labels():
    assert validate_labels(["cat", "dog"], {"cat", "dog"}) is True


def test_missing_label():
    with pytest.raises(ValueError, match="Missing ground-truth label"):
        validate_labels(["cat", None], {"cat", "dog"})


def test_invalid_label():
    with pytest.raises(ValueError, match="Invalid ground-truth label"):
        validate_labels(["cat", "bird"], {"cat", "dog"})


def test_empty_labels():
    with pytest.raises(ValueError, match="cannot be empty"):
        validate_labels([], {"cat", "dog"})


def test_consistent_predictions():
    predictions = {
        "image_1": ["cat", "cat", "cat"],
        "image_2": ["dog", "dog", "dog"],
    }
    assert check_prediction_consistency(predictions) is True


def test_inconsistent_predictions():
    predictions = {"image_1": ["cat", "cat", "dog"]}

    with pytest.raises(ValueError, match="Inconsistent predictions"):
        check_prediction_consistency(predictions)


def test_empty_predictions():
    with pytest.raises(ValueError, match="cannot be empty"):
        check_prediction_consistency({})


def test_input_without_predictions():
    predictions = {"image_1": []}

    with pytest.raises(ValueError, match="No predictions provided"):
        check_prediction_consistency(predictions)
