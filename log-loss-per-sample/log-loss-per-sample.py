import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    ans=[]

    for y,p in zip(y_true, y_pred):
        pc=max(eps,min(1-eps,p))
        l=-(y*math.log(pc)+(1-y)*math.log(1-pc))
        ans.append(l)
    return ans