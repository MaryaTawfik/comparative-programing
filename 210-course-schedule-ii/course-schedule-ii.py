from collections import deque , defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[]for  _ in range(numCourses)]
        in_degree=[0]*(numCourses)
        order=[]
        queue=deque()
        for course ,pre in prerequisites:
            graph[pre].append(course)
            in_degree[course]+=1

        queue =deque([])
        for i in range(len(in_degree)):
            if in_degree[i]==0:
                queue.append(i)
        while queue:
            node=queue.popleft()
            order.append(node)
            for nei in graph[node]:
                in_degree[nei]-=1

                if in_degree[nei]==0:
                    queue.append(nei)
        if len(order) != numCourses:
            return[]
        return order


        # graph=defaultdict(list)
        # for i in range(numCourses):
        #     graph[prerequisites[i][0]].append(prerequisites[i][1])
        # queue=deque()
        # def bfs(source,visited):
            
        