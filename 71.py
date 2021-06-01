class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/") # /home//foo/" => ['', 'home', '', 'foo', '']
        stack = []
        
        for i in path_list:
            if i == "." or i == "": #"" not " "
                continue
            elif i == "..":
                if stack: stack.pop()
            else:
                stack.append(i)
        
        return "/" + "/".join(stack)