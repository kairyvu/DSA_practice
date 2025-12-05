class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.currPage = 0
        self.lastPage = 0

    def visit(self, url: str) -> None:
        self.currPage += 1
        if len(self.history) == self.currPage:
            self.history.append(url)
        else:
            self.history[self.currPage] = url
        self.lastPage = self.currPage
        

    def back(self, steps: int) -> str:
        self.currPage = max(0, self.currPage - steps)
        return self.history[self.currPage]

    def forward(self, steps: int) -> str:
        self.currPage = min(self.lastPage, self.currPage + steps)
        return self.history[self.currPage]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)