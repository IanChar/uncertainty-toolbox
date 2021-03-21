"""
Tests for data.
"""

from uncertainty_toolbox.data import (
    synthetic_arange_random,
    synthetic_sine_heteroscedastic,
)


def test_synthetic_arange_random_n_data():
    """Test if correct data quantity is generated by synthetic_arange_random."""
    n_list = [10, 20]
    for n in n_list:
        y_pred, y_std, y_true, x = synthetic_arange_random(n)
        assert len(y_pred) == n
        assert len(y_std) == n
        assert len(y_true) == n
        assert len(x) == n


def test_synthetic_sine_heteroscedastic_n_data():
    """Test if correct data quantity is generated by synthetic_sine_heteroscedastic."""
    n_list = [10, 20]
    for n in n_list:
        y_pred, y_std, y_true, x = synthetic_sine_heteroscedastic(n)
        assert len(y_pred) == n
        assert len(y_std) == n
        assert len(y_true) == n
        assert len(x) == n
