#
# Index file
#
#

# Dependencies
from grid import Grid
import json

# Read configuration file
file = open("config.json")
# Load json data
data = json.load(file)

# Create object
grid = Grid(data["size"], data["cycles"], data["popSize"])
# Initialise loop
grid.displayGrid()
grid.runCycle()
