def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    re = []
    for mean, votes in items:
        wr = (votes/(votes+min_votes)) * mean + (min_votes/(votes+min_votes)) * global_mean
        re.append(wr)
    return re