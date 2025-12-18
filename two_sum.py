import time

arr = [
    2,3,4,5,7,7,9,3,4,2,3,4,5,1,7,8,3,4
] * 1300   # simulate large input
arr += [13, 100]

target = 113

def two_sum_bruteforce(arr, target):
    start = time.perf_counter()

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                end = time.perf_counter()
                return {
                    "pair": (arr[i], arr[j]),
                    "time_ms": (end - start) * 1000
                }
def two_sum_two_pointer(arr, target):
    start = time.perf_counter()

    arr = sorted(arr)
    l, r = 0, len(arr) - 1

    while l < r:
        s = arr[l] + arr[r]
        if s == target:
            end = time.perf_counter()
            return {
                "pair": (arr[l], arr[r]),
                "time_ms": (end - start) * 1000
            }
        elif s < target:
            l += 1
        else:
            r -= 1

bf_result = two_sum_bruteforce(arr, target)
tp_result = two_sum_two_pointer(arr, target)

print("Brute Force Result:", bf_result)
print("Two Pointer Result:", tp_result)


#output
# Brute Force Result: {'pair': (13, 100), 'time_ms': 4034.5648439833894}
# Two Pointer Result: {'pair': (13, 100), 'time_ms': 1.2981920153833926}



