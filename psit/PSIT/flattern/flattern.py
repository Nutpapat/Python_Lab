"""Flatten problem"""
import json
 
def flatten_recursive(inlist):
    """Return flatten list from inlist."""
    outlist = []
    for item in inlist:
        if isinstance(item, list):
            outlist.extend(flatten_recursive(item))
        else:
            outlist.append(item)
    outlist.sort(reverse=True)
    return outlist
 
print(flatten_recursive(json.loads(input())))
