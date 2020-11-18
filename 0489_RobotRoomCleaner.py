class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        difficult to represent robot's cur location and motions using 4 APIs
        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            0
        3       1
            2
        """
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()

        def back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def dfs(cur, direction, visited):
            robot.clean() 
            visited.add(cur)
            # The initial direction of the robot will be facing up.
            x, y = cur
            for i in range(4):
                nex_dir = (i + direction) %4
                nex_pos = (x + directions[nex_dir][0], y + directions[nex_dir][1])
                if nex_pos not in visited and robot.move():
                    dfs(nex_pos, nex_dir, visited)
                    back()
                # keep on clockwise motion to facing next direction (align direction with robot's orientation)
                robot.turnRight()
        dfs((0, 0), 0, visited)    
