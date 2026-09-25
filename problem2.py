from collections import deque

def longest_stable_window(values, k):
    n = len(values)
    max_deque = deque()  # thedeque is storing only indices, values decreasing front to back
    min_deque = deque()  # thedeque is storing only indices, values increasing front to back

    left = 0
    best_len = 0
    best_start = 0

    for right in range(n):
        while max_deque and values[max_deque[-1]] <= values[right]:
            max_deque.pop()
        max_deque.append(right)

        while min_deque and values[min_deque[-1]] >= values[right]:
            min_deque.pop()
        min_deque.append(right)

        while values[max_deque[0]] - values[min_deque[0]] > k:
            if max_deque[0] == left:
                max_deque.popleft()
            if min_deque[0] == left:
                min_deque.popleft()
            left += 1

        window_len = right - left + 1
        if window_len > best_len:
            best_len = window_len
            best_start = left

    return best_len, best_start + 1

n = int(input())
values = list(map(int, input().split()))
k = int(input())

length, start = longest_stable_window(values, k)
print(length, start)