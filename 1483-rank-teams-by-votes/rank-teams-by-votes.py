class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        ranks = len(votes[0])
        teams = list(votes[0])
        
        counts = {t: [0] * ranks for t in teams}
        for vote in votes:
            for i, t in enumerate(vote):
                counts[t][i] += 1
        
        def sortKey(t):
            return tuple(-r for r in counts[t]) + (t,)
        teams.sort(key=sortKey)
        return ''.join(teams)