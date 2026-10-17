
# Reliability Checks

A small Python project for checking two reliability issues:

1. Missing or invalid ground-truth labels.
2. Inconsistent repeated predictions for the same input.

## Requirements

- Python 3.11 or later
- pytest 9.1.1 (used during testing)

## Setup

Open a terminal in the project root directory and install pytest:

```bash
python -m pip install pytest
```

## Run the tests

From the project root, run:

```bash
python -m pytest -v
```

The test suite contains eight tests. A successful run should finish with a summary showing:

```text
8 passed
```

The exact duration and formatting may vary.

## Check 1: Ground-truth label validation

The `validate_labels(labels, valid_labels)` function checks that:

- The labels collection is not empty.
- No label is `None`.
- Every label belongs to the permitted set of labels.

It returns `True` for valid input and raises `ValueError` for invalid input.

Example:

```python
validate_labels(["cat", "dog"], {"cat", "dog"})
```

## Check 2: Repeated-prediction consistency

The `check_prediction_consistency(predictions)` function checks that repeated predictions for each input agree.

The input is a dictionary mapping each input ID to a non-empty list of predictions.

Example:

```python
check_prediction_consistency({
    "image_1": ["cat", "cat", "cat"],
    "image_2": ["dog", "dog", "dog"],
})
```

It returns `True` when all repeated predictions agree and raises `ValueError` when they disagree or the input is empty or contains an input with no predictions.

## Scope and limitations

- Automated tests use synthetic examples.
- No model training or dataset download is required.
- Prediction consistency means exact agreement between repeated outputs.
- Agreement does not establish that a prediction is correct.
- These checks cover only the two specified failure modes and do not establish overall model reliability.
