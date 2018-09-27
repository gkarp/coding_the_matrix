def dict2list(dct, keylist): return [dct[k] for k in keylist]

def list2dict(L, keylist): return {k: v for (k, v) in zip(keylist, L)}
	
def listrange2dict(L): 
    """
    input: a list L
    output: a dictionary that, for i=0,1,2,...,len(L)-1, maps to L[i]
    """
    return {L[i]: i for i in range(len(L))}
