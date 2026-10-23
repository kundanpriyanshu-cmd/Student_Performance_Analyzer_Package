# performance_analyzer/validator.py 
"""Sub-Module 1: Score Input Validation Engine""" 

import math


def validate_score(score_input): 
    """Validates if score is numeric and within bounds [0, 100].""" 
    if isinstance(score_input, bool):
        return False, 0.0

    try:
        val = float(score_input)
    except (TypeError, ValueError, OverflowError):
        return False, 0.0

    if not math.isfinite(val) or not 0.0 <= val <= 100.0:
        return False, 0.0

    return True, val
