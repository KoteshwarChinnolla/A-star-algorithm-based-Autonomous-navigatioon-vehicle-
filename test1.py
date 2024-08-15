import matplotlib.pyplot as plt
import numpy as np
import heapq
import serial
import time

arduino = serial.Serial(port='COM7', baudrate=9600, timeout=1)

def plot_maze(maze):
    fig, ax = plt.subplots(figsize=(10, 10))
    colored_maze = np.zeros((maze.shape[0], maze.shape[1], 3))
    # Set walls to black
    colored_maze[maze == 0] = [0, 0, 0]
    # Set passages to white
    colored_maze[maze == 1] = [1, 1, 1]
    
    ax.imshow(colored_maze)
    ax.set_xticks([]), ax.set_yticks([])

    green_cells = []
    directions_1 = []
    cid = [None]  # List to hold connection id

    def on_click(event):
        if event.inaxes and event.button == 1:  # Check for left mouse button
            x, y = int(event.xdata + 0.5), int(event.ydata + 0.5)  # Round to nearest integer
            if maze[y, x] == 1:  # Only allow clicking on passages
                colored_maze[y, x] = [0, 1, 0]  # Set cell to green
                green_cells.append((y, x))
                ax.imshow(colored_maze)
                plt.draw()
                if len(green_cells) > 1:
                    # Find shortest path between last two green cells
                    path, directions = a_star_search(maze, green_cells[-2], green_cells[-1])
                    directions_1.append(directions)
                    print("Path:", path)
                    print("Directions:", directions)
                    # Draw the path
                    for i in range(len(path) - 1):
                        y1, x1 = path[i]
                        y2, x2 = path[i + 1]
                        ax.plot([x1, x2], [y1, y2], color='blue',linewidth = 5)
                        plt.draw()
                    print(costamise(directions))
                    
    cid[0] = fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()
    return directions_1

def a_star_search(maze, start, end):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    directions = ["right", "down", "left", "up"]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, end)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))

    while oheap:
        current = heapq.heappop(oheap)[1]

        if current == end:
            data = []
            dir_data = []
            while current in came_from:
                direction, prev = came_from[current]
                data.append(current)
                dir_data.append(direction)
                current = prev
            data.append(start)
            dir_data.append(None)  # No direction for the start
            return data[::-1], dir_data[::-1]  # Return reversed path and directions

        close_set.add(current)
        for idx, (i, j) in enumerate(neighbors):
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + 1

            if 0 <= neighbor[0] < maze.shape[0]:
                if 0 <= neighbor[1] < maze.shape[1]:
                    if maze[neighbor[0]][neighbor[1]] == 0:
                        continue
                else:
                    # neighbor is out of bounds
                    continue
            else:
                # neighbor is out of bounds
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = (directions[idx], current)
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, end)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return False

# Predefined maze matrix (1 for passages, 0 for walls)
maze = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

def costamise(d):
    prev='down'
    curr=''
    cusarray=[]
    for i in range(1,len(d)):
        curr=d[i]
        if prev=='down':
            prev=curr
            if curr =='down':
                cusarray.append('f')
            elif curr=='up':
                cusarray.append('b')
                cusarray.append('f')
            elif curr=='right':
                cusarray.append('r')
                cusarray.append('f')
            else:
                cusarray.append('l')
                cusarray.append('f')
        elif prev=='up':
            prev=curr
            if curr =='down':
                cusarray.append('b')
                cusarray.append('f')
            elif curr=='up':
                cusarray.append('f')

            elif curr=='right':
                cusarray.append('l')
                cusarray.append('f')
            else:
                cusarray.append('r')
                cusarray.append('f')
        elif prev=='left':
            prev=curr
            if curr =='down':
                cusarray.append('r')
                cusarray.append('f')
            elif curr=='up':
                cusarray.append('l')
                cusarray.append('f')
            elif curr=='right':
                cusarray.append('b')
                cusarray.append('f')
            else:
                cusarray.append('f')
        else:
            prev=curr
            if curr =='down':
                cusarray.append('l')
                cusarray.append('f')
            elif curr=='up':
                cusarray.append('r')
                cusarray.append('f')
            elif curr=='right':
                cusarray.append('f')
            else:
                cusarray.append('b')
                cusarray.append('f')
    functionsend(cusarray)
    return cusarray

def sendtoarduino(data):
    arduino.write((data + '\n').encode())
    if data=='f':
        time.sleep(0.07)
    else:
        time.sleep(0.07)

def functionsend(Directions):
    # Directions = plot_maze(maze)
    Directions.append('s')
    for d in Directions:
        sendtoarduino(d)
        print(f"Sent: {d}")
        time.sleep(0.9) 

if __name__=='__main__':
    plot_maze(maze)
