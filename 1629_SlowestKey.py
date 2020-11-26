class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(keysPressed)
        durations = defaultdict(list)
        durations[releaseTimes[0]].append(keysPressed[0])
        max_dur = releaseTimes[0]
        for i in range(1, n):
            t = releaseTimes[i] - releaseTimes[i-1]
            durations[t].append(keysPressed[i])
            max_dur = max(max_dur, t)
        return max(durations[max_dur])
