class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = ""
        if numerator ^ denominator < 0:
            sign = "-"
        n, d = abs(numerator), abs(denominator)
        int_part = str(n//d)
        frac_part = ""
        if n%d != 0:
            frac_part += "."
            rem = n%d
            rem_pos = {}
            while rem != 0:
                if rem in rem_pos:
                    recur_start = rem_pos[rem]
                    non_recur = frac_part[:recur_start]
                    recur = frac_part[recur_start:]
                    return sign+int_part+non_recur+"("+recur+")"
                rem_pos[rem] = len(frac_part)
                frac_part += str(rem * 10//d)
                rem = rem*10%d
        return sign+int_part+frac_part
