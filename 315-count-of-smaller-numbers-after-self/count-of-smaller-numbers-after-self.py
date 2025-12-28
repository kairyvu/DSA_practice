class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_unique = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(sorted_unique)}
        n = len(sorted_unique)

        tree = defaultdict(int)

        def update(i):
            while i <= n:
                tree[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += tree[i]
                i -= i & -i
            return res

        result = []
        for num in reversed(nums):
            r = rank[num]
            result.append(query(r - 1))
            update(r)

        return result[::-1]