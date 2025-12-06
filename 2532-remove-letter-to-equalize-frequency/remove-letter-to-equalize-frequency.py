class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = defaultdict(int)
        for c in word:
            freq[c] += 1
        
        for c in freq:
            freq[c] -= 1
            freqs = [v for v in freq.values() if v > 0]
            if not freqs or len(set(freqs)) == 1:
                return True
            freq[c] += 1

        return False