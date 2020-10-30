class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        res = PolyNode(0,0)
        cur = res
        while poly1 and poly2:
            if poly1.power > poly2.power:
                cur.next = PolyNode(poly1.coefficient, poly1.power)
                cur = cur.next
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                cur.next = PolyNode(poly2.coefficient, poly2.power)
                poly2 = poly2.next
                cur = cur.next
            else:
                coeff = poly1.coefficient + poly2.coefficient
                p = poly1.power
                poly1 = poly1.next
                poly2 = poly2.next
                if coeff != 0:
                    cur.next = PolyNode(coeff, p)
                    cur = cur.next
        cur.next = poly1 or poly2
        return res.next