class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
        
        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        
        def dfs(course):
            if state[course] == 1:  # cycle detected
                return False
            if state[course] == 2:  # already processed
                return True
            state[course] = 1
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            state[course] = 2
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True