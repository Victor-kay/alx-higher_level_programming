def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    def binary_search_peak(left, right):
        if left == right:
            return list_of_integers[left]

        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            return binary_search_peak(left, mid)
        else:
            return binary_search_peak(mid + 1, right)

    return binary_search_peak(0, len(list_of_integers) - 1)
