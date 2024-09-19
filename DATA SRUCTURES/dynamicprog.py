def max_subarray_sum(arr):
    n = len(arr)
    if n == 0:
        return 0, []

    max_sum = arr[0]
    current_sum = arr[0]

    start_index = 0
    end_index = 0
    temp_start_index = 0

    for i in range(1, n):
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start_index = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start_index = temp_start_index
            end_index = i

    return max_sum, arr[start_index:end_index + 1]

def get_user_input():
    arr = []

    i = 0
    while i < 10:
        arr.append(int(input(f"Enter element {i + 1}: ")))
        i += 1

    return arr


if __name__ == "__main__":
    arr = get_user_input()

    if arr:
        max_sum, max_subarray = max_subarray_sum(arr)
        print(f"Array: {arr}")
        print(f"Maximum subarray: {max_subarray}")
        print(f"Maximum sum: {max_sum}")
