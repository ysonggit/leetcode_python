class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        boxes = 0
        total = 0
        for boxNum, units in boxTypes:
            # max boxes to add:
            boxesToAdd = max(min(truckSize - boxes, boxNum), 0)
            boxes += boxesToAdd
            total += boxesToAdd * units
            if boxesToAdd == truckSize:
                break
        return total
