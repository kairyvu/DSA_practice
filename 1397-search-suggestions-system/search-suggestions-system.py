class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        n = len(products)
        l, r = 0, n - 1
        res = []
        
        for i in range(len(searchWord)):
            suggestedWord = []
            currChar = searchWord[i]
            
            while l <= r and (len(products[l]) <= i or currChar != products[l][i]):
                l += 1
            
            while l <= r and (len(products[r]) <= i or currChar != products[r][i]):
                r -= 1
            
            for j in range(l, min(l + 3, r + 1)):
                suggestedWord.append(products[j])
            res.append(suggestedWord)
        return res