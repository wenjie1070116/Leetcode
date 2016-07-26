class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites: return True
        neighbors = [[] for i in xrange(numCourses)]
        courses = {i for i in xrange(numCourses)}
        indegree = [0]*numCourses
        for pre in prerequisites:
            neighbors[pre[0]].append(pre[1])
            indegree[pre[1]] += 1
        while True:
            mark = False
            temp = []
            for i in courses:
                if indegree[i] == 0:
                    mark = True
                    temp.append(i)
            if not mark: break
            for num in temp:
                for neighbor in neighbors[num]:
                    indegree[neighbor] -= 1
                courses.remove(num)
        return len(courses) == 0    
        