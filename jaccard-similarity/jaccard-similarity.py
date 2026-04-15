def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    deno= len(set(set_a).union(set(set_b)))
    num= len(set(set_a).intersection(set(set_b)))

    if num == 0 or deno==0:
        return 0.0
    return num/deno