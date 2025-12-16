class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        personTrans = defaultdict(list)
        n = len(transactions)
        invalid = [False] * n

        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            amount = int(amount)
            time = int(time)
            if amount > 1000:
                invalid[i] = True
            personTrans[name].append((time, city, i))
        
        for name, trans in personTrans.items():
            trans.sort()
            for i in range(len(trans)):
                time, city, index = trans[i]
                j = i + 1
                while j < len(trans) and trans[j][0] - time <= 60:
                    _, cityJ, indexJ = trans[j]
                    if city != cityJ:
                        invalid[index] = True
                        invalid[indexJ] = True
                    j += 1
        res = []
        for i in range(len(transactions)):
            if invalid[i]:
                res.append(transactions[i])
        return res