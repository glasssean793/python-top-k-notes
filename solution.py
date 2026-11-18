import heapq

def solve(value):
    return heapq.nlargest(value["k"], value["items"]) if value["k"] >= 0 else (_ for _ in ()).throw(ValueError("k must be nonnegative"))
