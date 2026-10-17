
def validate_labels(labels, valid_labels):
    """Check that ground-truth labels are present and valid."""

    if not labels:
        raise ValueError("Ground-truth labels cannot be empty.")

    for index, label in enumerate(labels):
        if label is None:
            raise ValueError(
                f"Missing ground-truth label at index {index}."
            )

        if label not in valid_labels:
            raise ValueError(
                f"Invalid ground-truth label at index {index}: {label!r}."
            )

    return True


def check_prediction_consistency(predictions):
    """Check that repeated predictions for each input agree."""

    if not predictions:
        raise ValueError("Predictions cannot be empty.")

    for input_id, repeated_predictions in predictions.items():
        if not repeated_predictions:
            raise ValueError(
                f"No predictions provided for input {input_id!r}."
            )

        first_prediction = repeated_predictions[0]

        for prediction in repeated_predictions[1:]:
            if prediction != first_prediction:
                raise ValueError(
                    f"Inconsistent predictions for input {input_id!r}: "
                    f"{repeated_predictions!r}."
                )

    return True
