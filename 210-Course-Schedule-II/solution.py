class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        neighbors = [[] for i in xrange(numCourses)]
        indegree = [0]*numCourses
        courses = {i for i in xrange(numCourses)}
        for pre in prerequisites:
            neighbors[pre[0]].append(pre[1])
            indegree[pre[1]] += 1
        while True:
            mark = False
            temp = []
            for course in courses:
                if indegree[course] == 0:
                    mark = True
                    temp.append(course)
            if not mark: break
            res += temp
            for ele in temp:
                for neighbor in neighbors[ele]:
                    indegree[neighbor] -= 1
                courses.remove(ele)
        if len(courses) != 0: return []
        return res[::-1]
        