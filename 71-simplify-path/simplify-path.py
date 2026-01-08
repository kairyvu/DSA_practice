class Solution:
    def simplifyPath(self, path: str) -> str:
        pathArr = path.split("/")
        resPath = []

        for p in pathArr:
            if p == "..":
                if not resPath:
                    continue
                resPath.pop()
                resPath.pop()
            elif not p or p == ".":
                continue
            else:
                resPath.append("/")
                resPath.append(p)
        
        return "/" if len(resPath) == 0 else "".join(resPath)