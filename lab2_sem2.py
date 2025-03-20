

def painting_time(k, t, long):
    if not long:
        return False

    left, right = max(long) * t, sum(long) * t
    if k >= len(long):
        return max(long) * t

    def paint_in_time(time_limit):
        painters_used = 1
        current_sum = 0

        for length in long:
            if current_sum + length * t <= time_limit:
                current_sum += length * t
            else:
                painters_used += 1
                current_sum = length * t
                if painters_used > k:
                    return False
        return True

    while left < right:
        mid = (left + right) // 2
        if paint_in_time(mid):
            right = mid
        else:
            left = mid + 1

    return left
