def count_positives_sum_negatives(arr):
    if arr == []:
        return [] 
    pos = [n for n in arr if n > 0]
    neg = [n for n in arr if n < 0]
    return [len(pos), sum(neg)]
