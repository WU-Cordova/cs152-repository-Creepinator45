from os import path
from datastructures.array2d import Array2D, IArray2D
from typing import Optional, Sequence, Iterator, TextIO
from projects.project2.kbhit import KBHit
from dataclasses import dataclass
from random import random
from time import sleep
from itertools import chain

class Cell:
    def __init__(self) -> None:
        self.__isBoarder: bool = False
        self.__isAlive: bool = False

    @property
    def isBoarder(self) -> bool:
        return self.__isBoarder
    
    @property
    def isAlive(self) -> bool:
        return self.__isAlive
    
    @isAlive.setter
    def isAlive(self, isAlive: bool) -> None:
        #boarder cells are immutable
        if not self.isBoarder:
            self.__isAlive = isAlive

    def __str__(self) -> str:
        return "" if self.isBoarder else " x" if self.isAlive else " -"

    def __eq__(self, value) -> bool:
        if not isinstance(value, Cell):
            return False
        
        return (self.isBoarder and value.isBoarder) or (self.isAlive == value.isAlive)

class Grid:
    def __init__(self, rows: int = 32, cols: int = 32) -> None:
        self.__grid: IArray2D = Array2D.empty(rows, cols, Cell)

        #setup boarder
        for cell in self.__grid[0]:
            cell._Cell__isBoarder = True
        for cell in self.__grid[-1]:
            cell._Cell__isBoarder = True
        for row in self.__grid:
            row[0]._Cell__isBoarder = True
            row[-1]._Cell__isBoarder = True
    
    @staticmethod
    def randomGrid(rows: int = 32, cols: int = 32) -> Array2D:
        grid = Grid(rows, cols)
        for _, cell in grid:
            if random() < 0.5:
                cell.isAlive = True
        return grid
    
    #iterate through non-boarder cells, also returns position of cell
    def __iter__(self) -> Iterator[tuple[tuple[int, int], Cell]]:
        for i, row in enumerate(self.__grid):
            #I would have much preferred doing this by iterating self.__grid[1:-2], but our Array2D can't handle slices
            if i == 0 or i == len(self.__grid)-1:
                continue
            for j, cell in enumerate(row):
                if j == 0 or j == len(row)-1:
                    continue
                yield ((i, j), cell)
    
    def __len__(self) -> int:
        return len(self.__grid) * len(self.__grid[0])
    
    def __str__(self) -> str:
        return f"{"\n".join(f"{"".join(f"{str(cell)}" for cell in row)}" for row in self.__grid)}" 
    
    def __eq__(self, value) -> bool:
        if not isinstance(value, Grid):
            return False
        
        if len(self) != len(value):
            return False
        
        for (_, cell1), (_, cell2) in zip(self, value):
            if cell1 != cell2:
                return False
            
        return True
    
    def checkCell(self, row, col) -> bool:
        """
        checks cell's state and neighbors and returns its isAlive for the next generation
        """
        cell:Cell = self.__grid[row][col]
        if cell.isBoarder:
            raise ValueError("attempted to check boarder cell")
        
        cellsToCheck = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        liveNeighbors = 0
        for (offsetX, offsetY) in cellsToCheck:
            #adds 1 if neighbor is alive
            liveNeighbors += self.__grid[row + offsetX][col + offsetY].isAlive
        
        match liveNeighbors:
            case 0|1:
                return False
            case 2:
                return cell.isAlive
            case 3:
                return True
            case 4|5|6|7|8:
                return False

class GameController:
    def __init__(self, rows: int = 32, cols: int = 32, history_length:int = 5) -> None:
        self.__dimensions: tuple[int, int] = (rows, cols)
        #this would be better as a fixed length array instead than a list, but I'd rather it hold references instead of deepcopies, so our Array implementation is unsuitable
        self.__grids: list[Grid] = [Grid(*self.__dimensions) for _ in range(history_length+1)]
        self.__grids[0] = Grid.randomGrid(*self.__dimensions)
        self.__iteration: int = 0
        self.__currentGridIndex:int = 0

    @staticmethod
    def fromArray2D(startingArray: Array2D[Cell], history_length: int = 5) -> "GameController":
        #add rows and cols for boarder
        output = GameController(len(startingArray)+2, len(startingArray[0])+2, history_length)
        for (_, cell), startingCell in zip(output.__grids[output.__currentGridIndex], chain.from_iterable(startingArray)):
            cell.isAlive = startingCell.isAlive
        return output

    @staticmethod
    def fromConfig(config: TextIO) -> "GameController":
        nonCommentLines = 0
        for line in config.readlines():
            if line[0] == "#":
                continue
            line = "".join(line.split())

            match nonCommentLines:
                case 0:
                    historyLen = int(line)
                case 1:
                    rows = int(line)
                case 2:
                    cols = int(line)
                    startingGrid = Array2D([[Cell() for _ in range(rows)] for _ in range(cols)])
                case _:
                    rowNum = nonCommentLines-3
                    for colNum, char in enumerate(line):
                        match char:
                            case "-":
                                pass
                            case "x":
                                startingGrid[rowNum][colNum].isAlive = True
                            case "#":
                                break
            nonCommentLines += 1
        return(GameController.fromArray2D(startingGrid, historyLen))

    @staticmethod
    def fromUserInput() -> "GameController":
        def askYesOrNo(question: str) -> bool:
            """
            Ask a yes or no question
            Return True if y, false if n
            If not y or n, re-ask question
            """
            while True:
                match input(question):
                    case "y":
                        return True
                    case "n":
                        return False
                    case _:
                        print("Invalid input, please answer with \"y\" or \"n\"")
        def askNumerical(question: str) -> int:
            """
            Ask numerical question
            Return integer answer
            If invalid int, re-ask question
            """
            while True:
                rawInput = input(question)
                try:
                    answer =  int(rawInput)
                except:
                    print("Invalid numerical input")
                else:
                    return answer
        def askConfig(question: str) -> GameController:
            """
            Ask for config file path
            Return game initialized from config
            If invalid config file, re-ask question
            """
            while True:
                rawConfigFile = input(question)
                try:
                    with open(path.normpath(rawConfigFile), "r") as config:
                        game = GameController.fromConfig(config)
                except:
                    print("Invalid config file")
                else:
                    return game
        def askCoordinate(question: str, maximum: tuple[Optional[int], Optional[int]] = (10000, 10000)) -> tuple[int, int]:
            """
            Ask for coordinate, formatted as "x,y"
            Return coordinate
            If invalid coordinate, re-ask question and prompt for correct formatting
            """
            while True:
                rawCoordinateInput = input(question)
                try:
                    coordinate = rawCoordinateInput.split(",")
                    x, y = int(coordinate[0]), int(coordinate[1])
                except:
                    print("Invalid coordinate")
                    print("Proper formatting is \"x,y\"")
                else:
                    if x>maximum[0]:
                        print("x out of range")
                        continue
                    if y>maximum[1]:
                        print("y out of range")
                        continue
                    return (x,y)

        if askYesOrNo("Read from config file (y/n)? "):
            return askConfig("Config file path: ")
        else:
            historyLen = askNumerical("How long is history length? ")
            rows = askNumerical("Length in x: ")
            cols = askNumerical("Length in y: ")
            if askYesOrNo("Manually input starting cells (y/n)? "):
                print("Note: it's reccomended to use a config file for extensive starting cell arrangements")
                startingArrangement = Array2D.empty(rows, cols, data_type=Cell)
                numberOfStartingCells = askNumerical("How many starting cells? ")
                for _ in range(numberOfStartingCells):
                    x,y = askCoordinate("Coordinate of live cell (x,y): ", (rows, cols))
                    startingArrangement[x][y].isAlive = True
                return GameController.fromArray2D(startingArrangement, historyLen)
            else:
                return GameController(rows, cols, historyLen)
        
    def nextIteration(self):
        self.__iteration += 1
        self.__currentGridIndex = self.__iteration % len(self.__grids)

        for position, cell in self.__grids[self.__currentGridIndex]:
            cell.isAlive = self.__grids[self.__currentGridIndex-1].checkCell(*position)
    
    def run(self):
        hasLooped: bool = False
        kbhit = KBHit()
        print(self)
        #variables for tracking user input
        waitTime = 1
        manuallyStep = True
        print("Currently manually stepping through simulation")
        print("Press \"enter\" to step to next generation")
        print("Use number keys to enable auto step through, and set speed")
        print("Press \"q\" to quite")

        while not hasLooped:
            #will set to True if detects user inputted enter
            #if manuallyStep and not takeNextStep, will not progress to next iteration this loop
            takeNextStep = False
            #query for user input
            if kbhit.kbhit():
                key = kbhit.getch()
                match key:
                    case "q":
                        print("Ended by keyboard input")
                        break
                    case n if n.isdigit():
                        if manuallyStep:
                            print("Enabled auto step through")
                            print("Press \"enter\" to re-enable manual step through")
                            manuallyStep = False
                        waitTime = int(n)/4.5
                        print(f"set speed to {waitTime} seconds")
                    case "\r" if not manuallyStep:
                        print("Enabled manual step through")
                        manuallyStep = True
                    case "\r":
                        takeNextStep = True

            if manuallyStep:
                if not takeNextStep:
                    continue
            else:
                sleep(waitTime)

            self.nextIteration()
            print(self)

            #check for match in grid history
            for i, grid in enumerate(self.__grids):
                if i == self.__currentGridIndex:
                    continue
                if grid == self.__grids[self.__currentGridIndex]:
                    print("Detected repeat")
                    hasLooped = True
        print("Ended simulation")
    
    def __str__(self) -> str:
        return f"Generation {self.__iteration}\n{str(self.__grids[self.__currentGridIndex])}"

def main():
    game = GameController.fromUserInput()
    game.run()

if __name__ == '__main__':
    main()
