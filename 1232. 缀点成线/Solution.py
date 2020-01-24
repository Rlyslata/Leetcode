from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        return all((coordinates[0][1] - coordinates[1][1]) * (coordinates[0][0] - coordinates[i][0]) == (coordinates[0][1] - coordinates[i][1]) * (coordinates[0][0] - coordinates[1][0]) for i in range(2, len(coordinates)))
        # (y0-y1)/(x0-x1) == (y0-yi)/(x0-xi)
        # ===>
        # (y0-y1)(x0-xi) == (y0-yi)*(x0-x1)
