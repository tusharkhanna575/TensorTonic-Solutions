def discount_returns(rewards: list, gamma: float) -> list:
    """
    Returns the discounted return at every timestep.
    """
    # Write code here
    n = len(rewards)
    dp = [0.0] * n
    dp[n - 1] = float(rewards[n - 1])

    for i in range(n - 2, -1, -1):
        dp[i] = float(rewards[i]) + gamma * dp[i + 1]

    return [round(i, 4) for i in dp]