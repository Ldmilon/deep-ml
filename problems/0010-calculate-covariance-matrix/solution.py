def calculate_covariance_matrix(vectors):
    n = len(vectors)
    N = len(vectors[0])
    means = [sum(v) / N for v in vectors]

    result = []
    for i in range(n):
        row = []
        for j in range(n):
            cov = sum(
                (vectors[i][k] - means[i]) *
                (vectors[j][k] - means[j])
                for k in range(N)
            ) / (N - 1)
            row.append(float(cov))
        result.append(row)

    return result
