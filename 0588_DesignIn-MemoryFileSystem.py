class MyFile:
    def __init__(self):
        self.filesMap = {}
        self.isFile = False # by default dir
        self.content = ""

class FileSystem:
    def __init__(self):
        self.root = MyFile() 

    def ls(self, path: str) -> List[str]:
        cur = self.root
        fileList = []
        if path != '/': # /a/b/c
            subpaths = path.split("/")[1:]
            for i, d in enumerate(subpaths):
                cur = cur.filesMap[d]
            if cur.isFile:
                fileList.append(subpaths[-1]) 
                return fileList 
        # sort root directory and display all files and dirs
        return sorted(cur.filesMap.keys())

    def mkdir(self, path: str) -> None:
        cur = self.root
        subpaths = path.split("/")[1:]
        for d in subpaths:
            if d not in cur.filesMap:
                cur.filesMap[d] = MyFile()
            cur = cur.filesMap[d]
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.root
        subpaths = filePath.split("/")[1:]
        filename = subpaths[-1]
        for d in subpaths[:-1]:
            cur = cur.filesMap[d]
        if filename not in cur.filesMap:
            cur.filesMap[filename] = MyFile()
            cur.filesMap[filename].isFile = True
        cur.filesMap[filename].content += content
        
    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        subpaths = filePath.split("/")[1:]
        filename = subpaths[-1]
        for d in subpaths[:-1]:
            cur = cur.filesMap[d]
        return cur.filesMap[filename].content
