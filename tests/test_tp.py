from math import ceil

import numpy as np

from mapie.utils import _compute_classification_quantile


def test_classification_quantile_matches_expected_order_statistic():
    for n in [9, 20, 50, 100]:
        scores = np.arange(n)
        for alpha in [0.1, 0.2, 0.3, 0.5]:
            got = _compute_classification_quantile(scores.reshape(-1, 1), np.array([alpha]))[0]
            expected = np.sort(scores)[ceil((1 - alpha) * (n + 1)) - 1]
            assert got == expected
