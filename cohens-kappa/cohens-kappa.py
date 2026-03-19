import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    r1 = np.array(rater1)
    r2 = np.array(rater2)
    n = len(r1)
    pe = 0
    class_ = np.unique(np.concatenate([r1,r2]))
    po = np.mean(r1==r2)
    for i in class_:
        c1 = np.sum(r1 == i)/n
        c2 = np.sum(r2 == i)/n
        pe += c1 * c2
    if po == pe == 1:
        return 1
    return (po-pe)/(1-pe)