def detect_drift(reference_counts, production_counts, threshold):
    """
    Compare reference and production distributions to detect data drift.
    """
    # Write code here
    ref=[i/sum(reference_counts) for i in reference_counts]
    prod=[i/sum(production_counts) for i in production_counts]
    # print(ref)
    # print(prod)
    ans=0
    for i in range(len(ref)):
        ans += abs(prod[i]-ref[i])
    ans/=2
    drift=bool(ans>threshold)
    return {"score": ans, "drift_detected": drift}