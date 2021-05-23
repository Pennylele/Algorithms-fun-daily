class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node) # Trie setup.
        self.content = ""
        
class FileSystem:

    def __init__(self):
        self.root = Node()
        
    def findNode(self, path): 
        cur = self.root
        if path == "/": # a bit confused
            return self.root
        for ch in path.split("/")[1:]: # first element is an empty string
            cur = cur.children[ch]
        return cur
        
    def ls(self, path: str) -> List[str]:
        cur = self.findNode(path)
        if cur.content:
            return [path.split("/")[-1]] # required to output in a list format
        return sorted(cur.children.keys()) # not sure where this requirement comes from
                         

    def mkdir(self, path: str) -> None:
        self.findNode(path)

                
    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.findNode(filePath)
        cur.content += content       

    def readContentFromFile(self, filePath: str) -> str:
        node = self.findNode(filePath)
        return node.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)