def bad_char_table(pattern):
    table = {}
    for i in range(len(pattern)):
        table[pattern[i]] = i
    return table

def boyer_moore_search(haystack, needle):
    if not needle or not haystack or len(needle) > len(haystack):
        return []

    bad_char = bad_char_table(needle)
    m = len(needle)
    n = len(haystack)
    indices = []

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and needle[j] == haystack[s + j]:
            j -= 1
        if j < 0:
            indices.append(s)
            s += m
        else:
            shift = j - bad_char.get(haystack[s + j], -1)
            s += max(1, shift)

    return indices








