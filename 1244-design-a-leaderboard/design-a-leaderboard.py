from sortedcontainers import SortedDict

class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict() # score -> count

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        
        else:
            oldScore = self.scores[playerId]
            newScore = oldScore + score
            self.scores[playerId] = newScore
            self.sortedScores[-oldScore] -= 1
            if self.sortedScores[-oldScore] == 0:
                del self.sortedScores[-oldScore]
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1

    def top(self, K: int) -> int:
        total = 0
        for score, count in self.sortedScores.items():
            total += min(K, count) * (-score)
            K -= count

            if K <= 0:
                break
        return total

    def reset(self, playerId: int) -> None:
        playerScore = self.scores[playerId]
        self.sortedScores[-playerScore] -= 1
        if self.sortedScores[-playerScore] == 0:
            del self.sortedScores[-playerScore]
        del self.scores[playerId]