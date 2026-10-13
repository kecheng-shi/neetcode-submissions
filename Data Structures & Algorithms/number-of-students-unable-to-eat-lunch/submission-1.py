class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dq_students = deque(students)
        dq_sandwiches = deque(sandwiches)
        skipped = 0

        while dq_students:
            if dq_students[0] == dq_sandwiches[0]:
                dq_students.popleft()
                dq_sandwiches.popleft()
                skipped = 0
            else:
                dq_students.append(dq_students.popleft())
                skipped += 1
            
            if skipped > len(students):
                return len(dq_students)
        
        return len(dq_students)
