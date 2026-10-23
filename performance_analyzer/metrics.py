# performance_analyzer/metrics.py 
"""Sub-Module 2: Grading Rules & Class Analytics Engine""" 

from .validator import validate_score


def compute_grade(score): 
    """Returns letter grade and GPA points for a validated score.""" 
    try:
        numeric_score = float(score)
    except (TypeError, ValueError, OverflowError):
        return 'F', 0

    is_valid, numeric_score = validate_score(numeric_score)
    if not is_valid:
        return 'F', 0

    if numeric_score >= 90.0:
        return 'O', 10
    if numeric_score >= 80.0:
        return 'A+', 9
    if numeric_score >= 70.0:
        return 'A', 8
    if numeric_score >= 60.0:
        return 'B+', 7
    if numeric_score >= 50.0:
        return 'B', 6
    if numeric_score >= 40.0:
        return 'C', 5
    return 'F', 0


def analyze_class(student_records): 
    """Calculates class average score, pass percentage, and top scorer.""" 
    if not student_records:
        return 0.0, 0.0, 'None'

    valid_records = []
    for record in student_records:
        if not isinstance(record, dict) or 'name' not in record:
            continue

        score = record.get('score')
        is_valid, validated_score = validate_score(score)
        if is_valid:
            valid_records.append({**record, 'score': validated_score})

    if not valid_records:
        return 0.0, 0.0, 'None'

    total_score = sum(record['score'] for record in valid_records)
    avg = total_score / len(valid_records)
    passed_count = sum(1 for record in valid_records if record['score'] >= 40.0)
    pass_rate = (passed_count / len(valid_records)) * 100.0
    top_student = max(valid_records, key=lambda x: x['score'])['name']
    return round(avg, 2), round(pass_rate, 2), top_student
