def catalog_coverage(recommendations: list, n_items: int) -> float:
    """
    Returns the fraction of catalog items that were recommended.
    """
    # Write code here
    item = set()

    for i in recommendations:
        item.update(i)

    return len(item) / n_items if n_items>0 else 0.0