def magical_mirror_array(arr):
    """
    Rearranges array elements so that adjacent elements
    have the largest possible absolute difference.

    Example:
    Input: [1, 2, 3, 4, 5, 6, 7]
    Output: [1, 7, 2, 6, 3, 5, 4]
    """

    arr.sort()
    left, right = 0, len(arr) - 1
    result = []

    while left <= right:
        if left == right:
            result.append(arr[left])
            break
        result.append(arr[left])
        result.append(arr[right])
        left += 1
        right -= 1

    return result


# ----------- DRIVER CODE -------------
if __name__ == "__main__":
    arr = [5, 1, 9, 2, 7, 3, 6, 4]
    print("Original:", arr)
    print("Magical Mirror Array:", magical_mirror_array(arr))

    # To verify difference effect:
    diff = [abs(a - b) for a, b in zip(magical_mirror_array(arr), magical_mirror_array(arr)[1:])]
    print("Neighbor differences:", diff)
    print("Average difference:", round(sum(diff) / len(diff), 2))
