def priority_replay_sample(priorities, alpha, beta):
    """
    Compute sampling probabilities and importance sampling weights for PER.
    """
    import numpy as np
    n = len(priorities)
    p_i = [i**alpha for i in priorities]
    total = sum(p_i)
    P_i = [i/total for i in p_i]
    w_i = [(n*i)**-beta for i in P_i]
    w_o = [i/max(w_i) for i in w_i]
    return [P_i, w_o]