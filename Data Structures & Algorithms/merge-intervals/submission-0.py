class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ls = sorted(intervals)
        output = [ls[0]]

        for start, end in ls[1:]:
            lastEnd = output[-1][-1]

            if start <= lastEnd:
                output[-1][-1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output             