import logging


# Assumptions
# the lower-left coordinates are assumed to be 0,0.
# The square directly North from (x, y) is (x, y+1).
# Each rover will be finished sequentially


# The roverCoordinates function returns the position of the rover after the series of signals
# are executed by the rover
def roverCoordinates(plateauArea, roverPos, roverMotionInput):
    roverMotion = list(roverMotionInput)
    for motion in roverMotion:
        if (motion == "L") | (motion == "R"):
            roverPos["dir"] = rotations(roverPos["dir"], motion)
        elif motion == "M":
            roverPos = nextPosition(plateauArea, roverPos)
    return roverPos


# The Rotations function returns the rover's current direction after turning
# Left or Right in response to the provided signal.
def rotations(initDir, turn):
    nextDir = ""
    if initDir == "N":
        if turn == "L":
            nextDir = "W"
        else:
            nextDir = "E"

    elif initDir == "S":
        if turn == "L":
            nextDir = "E"
        else:
            nextDir = "W"

    elif initDir == "E":
        if turn == "L":
            nextDir = "N"
        else:
            nextDir = "S"

    elif initDir == "W":
        if turn == "L":
            nextDir = "S"
        else:
            nextDir = "N"
    return nextDir


# The nextPosition function returns the current position of the rover after moving
# forward in response to the signal provided
def nextPosition(plateauArea, roverPos):
    if roverPos["dir"] == "N":
        if plateauArea["y"] >= roverPos["y"] + 1:
            roverPos["y"] = roverPos["y"] + 1
        else:
            logging.error("The rover is moving out of the plateau area. Cannot perform Action")
            return roverPos
    elif roverPos["dir"] == "S":
        if 0 <= roverPos["y"] - 1:
            roverPos["y"] = roverPos["y"] - 1
        else:
            logging.error("The rover is moving out of the plateau area. Cannot perform Action")
            return roverPos
    elif roverPos["dir"] == "E":
        if plateauArea["x"] >= roverPos["x"] + 1:
            roverPos["x"] = roverPos["x"] + 1
        else:
            logging.error("The rover is moving out of the plateau area. Cannot perform Action")
            return roverPos
    else:
        if 0 <= roverPos["x"] - 1:
            roverPos["x"] = roverPos["x"] - 1
        else:
            logging.error("The rover is moving out of the plateau area. Cannot perform Action")
            return roverPos
    return roverPos


if __name__ == '__main__':
    # Input Data 1
    plateauArea = {"x": 5, "y": 5}
    roverPos = {"x": 1, "y": 2, "dir": "N"}
    roverMotionInput = "LMLMLMLMM"

    print(roverCoordinates(plateauArea, roverPos, roverMotionInput))

    # Input Data 2
    plateauArea = {"x": 5, "y": 5}
    roverPos = {"x": 3, "y": 3, "dir": "E"}
    roverMotionInput = "MMRMMRMRRM"

    print(roverCoordinates(plateauArea, roverPos, roverMotionInput))
