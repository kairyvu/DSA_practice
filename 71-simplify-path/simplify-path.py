class Solution:
    def simplifyPath(self, path: str) -> str:
        pathArr = path.split("/")
        resPath = []

        for p in pathArr:
            if p in ["", "."]:
                continue
            elif p != "..":
                resPath.append(p)
            elif resPath and p == "..":
                resPath.pop()
        
        return "/" + "/".join(resPath)