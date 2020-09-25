class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students_scores = {}
        for item in items:
            s_id, score = item[0], item[1]
            if s_id in students_scores:
                students_scores[s_id].append(score)
            else:
                students_scores[s_id] = [score]
        res = []
        for s_id, scores in students_scores.items():
            top_five = sum(sorted(scores, reverse=True)[:5])//5
            res.append([s_id, top_five])
        return res