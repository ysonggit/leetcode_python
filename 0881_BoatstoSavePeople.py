class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        boats = 0
        i,j = 0, len(people)-1
        while i <= j:
            if (i != j and people[i] + people[j] <= limit) or (i==j and people[i] <= limit):
                i += 1
                j -= 1
            else:
                i += 1
            boats += 1
        return boats
