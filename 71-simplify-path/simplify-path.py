class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")
        
        for part in parts:
            if part == "" or part == ".":
                # Skip empty or current directory
                continue
            elif part == "..":
                # Go up one level if possible
                if stack:
                    stack.pop()
            else:
                # Valid directory name
                stack.append(part)
        
        # Build canonical path
        return "/" + "/".join(stack)
