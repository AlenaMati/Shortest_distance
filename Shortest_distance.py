class QueueItem:
    def __init__(self, row, col, dist, route):
        self.row = row
        self.col = col
        self.dist = dist
        self.route = route

    def go_up(self):
        self.route.append('up')

    def go_down(self):
        self.route.append('down')

    def go_left(self):
        self.route.append('left')

    def go_right(self):
        self.route.append('right')


grid = [[False, False, False, 'B', True, False],
        [True, False, False, False, True, False],
        [True, True, True, True, True, True],
        [False, False, False, False, True, False],
        [True, True, 'A', False, True, True],
        [True, False, True, True, True, False]]


def find_shortest_path(grid):
    start = QueueItem(0, 0, 0, [])

    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'A':
                start.row = row
                start.col = col
                break

    # To maintain location "visit" status, assign "False" to all cells in the grid
    visited = [[False for i in range(len(grid[0]))]
               for i in range(len(grid))]

    queue = []
    # adding starting point to the queue:
    queue.append(start)
    # changing the cell of the starting point to "True":
    visited[start.row][start.col] = True

    while len(queue) != 0:

        # changing the starting point to the element at the beginning of the queue:
        start = queue.pop(0)
        # If destination found we should return the route:
        if grid[start.row][start.col] == 'B':
            return start.dist, start.route

        # moving up
        if is_valid(start.row - 1, start.col, grid, visited):
            new_item = QueueItem(start.row - 1, start.col, start.dist + 1, start.route)
            new_item.go_up()
            queue.append(new_item)
            visited[start.row - 1][start.col] = True

        # moving down
        if is_valid(start.row + 1, start.col, grid, visited):
            new_item = QueueItem(start.row + 1, start.col, start.dist + 1, start.route)
            new_item.go_down()
            queue.append(new_item)
            visited[start.row + 1][start.col] = True

        # moving left
        if is_valid(start.row, start.col - 1, grid, visited):
            new_item = QueueItem(start.row, start.col - 1, start.dist + 1, start.route)
            new_item.go_left()
            queue.append(new_item)
            visited[start.row][start.col - 1] = True

        # moving right
        if is_valid(start.row, start.col + 1, grid, visited):
            new_item = QueueItem(start.row, start.col + 1, start.dist + 1, start.route)
            new_item.go_right()
            queue.append(new_item)
            visited[start.row][start.col + 1] = True

    return 'No path found.'


# checking whether move is valid or not:
def is_valid(x, y, grid, visited):
    if ((x >= 0 and y >= 0) and
            (x < len(grid) and y < len(grid[0])) and
            (grid[x][y] != False) and (visited[x][y] == False)):
        return True
    return False


print(find_shortest_path(grid))
