import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ON = 255
OFF = 0

def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = (  grid[(i-1)%N,(j-1)%N]
                    + grid[(i-1)%N,j]
                    + grid[(i-1)%N,(j+1)%N]
                    + grid[i,(j-1)%N]
                    + grid[i,(j+1)%N]
                    + grid[(i+1)%N,(j-1)%N]
                    + grid[(i+1)%N,j]
                    + grid[(i+1)%N,(j+1)%N])/255

            if grid[i,j] == ON and (total < 2 or total > 3):
                newGrid[i,j] = OFF
            elif grid[i,j] == OFF and total == 3:
                newGrid[i,j] = ON

    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

def main():
    N = 100
    grid = np.zeros((N, N))
    grid[1,2] = ON
    grid[2,3] = ON
    grid[3,1] = ON
    grid[3,2] = ON
    grid[3,3] = ON

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update,
                                  fargs=(img, grid, N, ),
                                  frames=1000,
                                  save_count=50)
    plt.show()

main()
