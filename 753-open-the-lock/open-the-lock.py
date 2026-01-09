class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        invalid = set(deadends)
        if target in invalid or "0000" in invalid:
            return -1
        
        def nextMoves(numLst):
            allMoves = []
            for i in range(4):
                increase = numLst[:i] + str((int(numLst[i]) + 1) % 10) + numLst[i+1:]
                decrease = numLst[:i] + str((int(numLst[i]) - 1) % 10) + numLst[i+1:]
                allMoves.append(increase)
                allMoves.append(decrease)
            return allMoves

        q = deque(["0000"])
        move = 0
        while q:
            for _ in range(len(q)):
                currKey = q.popleft()
                if currKey == target:
                    return move
                for nxtMove in nextMoves(currKey):
                    if nxtMove not in invalid:
                        invalid.add(nxtMove)
                        q.append(nxtMove)
            move += 1
        return -1