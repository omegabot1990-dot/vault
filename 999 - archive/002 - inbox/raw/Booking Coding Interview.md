---
tags:
  - inbox
description:
due date: 2026-02-15
start date: 2026-02-03
end date:
status: In Progress
importance level: important
urgency level: urgent
task type: execute
story points:
parent nodes:
child nodes:
recurrent:
---

| Signal                      | Bucket           |
| --------------------------- | ---------------- |
| Match / valid               | Stack            |
| Count / group               | Hashmap          |
| Top k                       | Heap             |
| Longest / shortest subarray | Sliding Window   |
| Choices + min/max           | DP               |
| Sorted input, pairs         | Two pointers     |
| Intervals                   | Sorting + Greedy |
| Trees                       | DFS/BFS          |

---

1. https://leetcode.com/problems/two-sum/
	1. HashMap (value->index) + One Pass
		1. Scan nums; for each x, check if (target-x) already seen, else store x’s index.

2. https://leetcode.com/problems/valid-parentheses/
	1. Stack
		1. Push opening brackets; on closing, it must match stack top; stack ends empty.

3. https://leetcode.com/problems/reward-top-k-students/
	1. HashSet + MinHeap (size K)
		1. Score each report via pos/neg word sets, then keep top-K with a min-heap of (score, id).

4. https://leetcode.com/problems/minimum-array-sum/
	1. DP (2D / state by index + operations)
		1. DP[i][j] = minimum sum using first i elements with j operations, transition by applying/not applying ops to nums[i].

5. https://leetcode.com/problems/valid-anagram/
	1. Frequency Counting (HashMap / Array[26])
		1. Count chars in s and subtract with t; all counts must end at 0.

6. https://leetcode.com/problems/group-anagrams/
	1. HashMap + Canonical Key (sorted string or 26-count tuple)
		1. Map each word’s signature to a bucket; output all buckets.

7. https://leetcode.com/problems/top-k-frequent-elements/
	1. HashMap + MinHeap (size K)  (or Bucket Sort)
		1. Count frequencies, then keep a size-K min-heap of (freq, num) to output top-K.

8. https://leetcode.com/problems/roman-to-integer/
	1. Greedy Scan (with lookahead)
		1. Walk left→right adding value, but subtract when a smaller numeral precedes a larger one.

9. https://leetcode.com/problems/sort-characters-by-frequency/
	1. Frequency Counting + Bucket Sort (or Sorting)
		1. Count chars, then output characters in descending frequency (via buckets or sorted counts).

10. https://leetcode.com/problems/k-closest-points-to-origin/
	1. Heap (MaxHeap size K)  (or Quickselect)
		1. Maintain K closest by keeping a max-heap on distance; pop when size exceeds K.

11. https://leetcode.com/problems/string-to-integer-atoi/
	1. Parsing + Bounds/Clamping
		1. Skip spaces, parse optional sign + digits, stop at first non-digit, clamp to 32-bit int range.

12. https://leetcode.com/problems/most-common-word/
	1. String Parsing + HashMap + Set
		1. Normalize (lowercase, split on non-letters), count non-banned words, return max frequency.

13. https://leetcode.com/problems/custom-sort-string/
	1. Frequency Counting + Custom Order Build
		1. Count chars in s, emit in order of “order” using counts, then append remaining chars.

14. https://leetcode.com/problems/longest-substring-without-repeating-characters/
	1. Sliding Window + HashMap (last seen index)
		1. Expand right; when repeat, move left to lastSeen[char]+1; track max window length.

15. https://leetcode.com/problems/maximum-units-on-a-truck/
	1. Greedy + Sorting
		1. Sort box types by units/box descending, take as many as possible until truck is full.

16. https://leetcode.com/problems/merge-intervals/
	1. Sorting + Greedy Merge
		1. Sort by start; either extend the last merged interval or start a new one.

17. https://leetcode.com/problems/insert-interval/
	1. Intervals + Linear Scan (merge while inserting)
		1. Add all intervals ending before new, merge overlaps with new, then append the rest.

18. https://leetcode.com/problems/array-partition/
	1. Greedy + Sorting
		1. Sort and sum every other element (the mins of each pair) to maximize total.

19. https://neetcode.io/problems/meeting-schedule-ii
	1. Sweep Line / Two Pointers (sorted starts & ends)
		1. Sort start and end times; increment rooms when a meeting starts before the earliest end, else release a room.
	2. https://leetcode.com/problems/car-pooling/
		1. Sweep Line (Difference Array)
			1. Use diff[t] += passengers at start and diff[t] -= at end; prefix sum must never exceed capacity.

20. https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons
	1. Greedy + Sorting by End
		1. Sort by end coordinate; shoot an arrow at current end, and only add a new arrow when next start > current end.

21. https://leetcode.com/problems/non-overlapping-intervals/
	1. Greedy + Sorting by End
		1. Pick maximum number of non-overlapping intervals by earliest finish; removals = n - kept.

22. https://leetcode.com/problems/can-place-flowers/
	1. Greedy + Linear Scan
		1. Place a flower when current plot and neighbors are 0 (treat edges as 0), decrement n until done.

23. https://leetcode.com/problems/task-scheduler/
	1. Greedy + Counting (Math)
		1. Let maxFreq be highest count and numMax how many share it; answer = max(len(tasks), (maxFreq-1)*(n+1)+numMax).

24. https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
	1. One Pass DP / Greedy
		1. Track min price so far; at each price update best profit = max(best, price - minPrice).

25. https://leetcode.com/problems/maximum-subarray/
	1. Dynamic Programming (Kadane) + One Pass
		1. At each index, bestEnding = max(nums[i], bestEnding+nums[i]) and keep a global maximum.

26. https://leetcode.com/problems/gas-station/
	1. Greedy + Prefix Sum / Running Balance
		1. If total gas is sufficient, there’s a unique valid start; whenever the tank goes negative, all earlier stations are invalid, so we restart from the next one.

27. https://leetcode.com/problems/jump-game/
	1. Greedy + Reachability (One-pass, running maximum reach)
		1. I greedily track the farthest index reachable so far; if at any point the current index is beyond that, it’s impossible to proceed.

