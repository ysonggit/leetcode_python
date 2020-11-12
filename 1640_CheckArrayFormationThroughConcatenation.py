class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        m = sum([len(p) for p in pieces])
        if m != n:
            return False
        i = 0
        while i < n:
            cur = arr[i]
            in_piece = False
            match_piece_idx = -1
            for j, piece in enumerate(pieces):
                if cur in piece:
                    in_piece = True
                    match_piece_idx = j
            if not in_piece:
                return False
            else:
                match_piece = pieces[match_piece_idx]
                match_size = len(match_piece)
                for k in range(match_size):
                    if arr[i+k] != match_piece[k]:
                        return False
                i += match_size
                continue
            i+= 1
        return True
