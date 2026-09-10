def rating_normalization(matrix: list) -> list:
    """
    Returns the mean-centered user-item matrix.
    """
    # Write code here
    result = []
    for i in matrix:
        rated = [v for v in i if v != 0]
        if len(rated) == 0:
            result.append([0.0] * len(i))
            continue
        mean = sum(rated) / len(rated)
        result.append([v - mean if v != 0 else 0.0 for v in i])
    return result