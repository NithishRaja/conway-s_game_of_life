#!/usr/bin/env python
# coding: utf-8

# In[112]:


#
# File containing code for grid
#
#


# In[113]:


# Dependencies
import matplotlib.pyplot as plt
import random
from celluloid import Camera


# In[114]:


# Initialise class for grid
class Grid():
    def __init__(this, size, cycles, popSize):
        """Initialise grid to initial state i.e., all cells set to zero.

        Keyword Arguments:
        size -- integer specifying no of rows and columns in the grid
        cycles -- integer storing no of iterations
        popSize -- float specifying initial size of population as a fraction of grid size
        """
        # Initialise size
        this.size = size

        # Initialise no of cycles
        this.cycles = cycles

        # Initialise population size
        this.popSize = popSize

        # Initialise grid
        this.grid = []

        # Initialise array to hold coordinates of cells to toggle
        this.x = []
        this.y = []
        
        # Add camera to animate
        fig = plt.figure()
        this.camera = Camera(fig)

        # Add rows to grid
        for i in range(this.size):
            this.grid.append([])
            # Initialise cells to 0
            for j in range(this.size):
                this.grid[i].append(0)

        # Initialise grid
        this.initialiseGrid()


# In[115]:


class Grid(Grid):
    def getAliveNeighbourCount(this, row, column):
        """Returns count of alive neighbours for current cell.

        Keyword Arguments:
        row -- row number of current cell
        column -- column number of current cell
        """
        # Initialise variable to track number of alive neighbours
        count = 0 - this.grid[row][column]

        # Iterate over each neighbour row
        for i in range(-1, 2):
            # Iterate over each neighbour cell in row
            for j in range(-1, 2):
                # Set coordinates of neighbour
                r = row + i
                c = column + j
                # Check if values are below lower limit
                if r < 0:
                    r = r + this.size
                if c < 0:
                    c = c + this.size
                # Check if values are above upper limit
                if r >= this.size:
                    r = r - this.size
                if c >= this.size:
                    c = c - this.size
                # Update count
                count = count + this.grid[r][c]

        return count


# In[116]:


class Grid(Grid):
    def checkCell(this, row, column):
        """Check if cell should be toggled or not.

        Keyword Arguments:
        row -- row number of current cell
        column -- column number of current cell
        """
        count = this.getAliveNeighbourCount(row, column)

        status = this.grid[row][column]

        newStatus = 0

        if status == 1 and (count < 2 or count > 3):
            this.x.append(row)
            this.y.append(column)
        elif status == 0 and count == 3:
            this.x.append(row)
            this.y.append(column)


# In[117]:


class Grid(Grid):
    def updateGrid(this):
        """Iterate over each cell and call updateCell."""
        # Iterate over rows
        for i in range(this.size):
            # Iterate over columns
            for j in range(this.size):
                # Call updateCell function
                this.checkCell(i, j)

        # Iterate over all coordinates
        for i in range(len(this.x)):
            # Toggle cell
            this.grid[this.x[i]][this.y[i]] = (this.grid[this.x[i]][this.y[i]] + 1)%2

        # Reset arrays x and y
        this.x = []
        this.y = []


# In[118]:


class Grid(Grid):
    def displayGrid(this):
        """Display grid using a scatter plot."""
        # Initialise arrays to hold live cell coordinates
        x = []
        y = []
        # Iterate over each row
        for row in range(this.size):
            # Iterate over each column
            for column in range(this.size):
                # Check if current cell is a live cell
                if this.grid[row][column] == 1:
                    # Add coordinates of live cell to list
                    x.append(row)
                    y.append(column)
        # Plot live cells on graph
        plt.scatter(x, y, label= "stars", color= "green", marker= "*", s=30)
        # Plot lines to separte cells
#         for i in range(-1, 2*this.size, 2):
#             plt.axhline(y=i/2)
#             plt.axvline(x=i/2)
        # Add graph as frame
        this.camera.snap()


# In[119]:


class Grid(Grid):
    def runCycle(this):
        """Perform operations for each cycle."""
        # Iterate over each cycle
        for i in range(this.cycles):
            # Update grid
            this.updateGrid()
            # Display grid
            this.displayGrid()
        
        animation = this.camera.animate()
        animation.save('conway_game_of_life.gif', writer = 'imagemagick')


# In[120]:


class Grid(Grid):
    def initialiseGrid(this):
        """Initialise random cells to 1."""
        # Iterate over number of cells to initialise
        for i in range(int(this.size*this.size*this.popSize)):
            # Get random coordinates
            row = random.randint(0, this.size-1)
            column = random.randint(0, this.size-1)
            # Set cell to 1
            this.grid[row][column] = 1

