class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        eats = 0
        n = len(students)
        seq = set()
        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                eats += 1
            else:
                s =  "".join(list(map(str, students)))
                if s in seq:
                    break
                seq.add(s)
                students = students[1:] + students[0:1]
        return n - eats
