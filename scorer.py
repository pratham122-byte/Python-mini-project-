from analyzer import compare_skills


def calculate_score(resume, job):

    matched, missing = compare_skills(resume, job)

    total = len(matched) + len(missing)

    if total == 0:
        score = 0
    else:
        score = int((len(matched) / total) * 100)

    return score