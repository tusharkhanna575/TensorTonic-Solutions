import math

def cyclic_encoding(values: list, period: float) -> list:
    """
    Returns the sine and cosine encoding of every cyclic value.
    """
    # Write code here
    ans=[]
    for i in values:
        thetha=2*math.pi*i/period
        temp=[math.sin(thetha), math.cos(thetha)]
        ans.append(temp)
    return ans