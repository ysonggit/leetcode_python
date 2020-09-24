class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = set()
        area = 0
        for r in rectangles:
            area += (r[3]-r[1])*(r[2]-r[0])
            for p in [(r[0],r[1]), (r[2],r[3]), (r[0],r[3]), (r[2],r[1])]:
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)
        if len(corners) != 4:
            return False
        corners = sorted(list(corners))
        return area == (corners[-1][0]-corners[0][0])*(corners[-1][1] - corners[0][1])