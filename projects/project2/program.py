from datastructures.array2d import Array2D, IArray2D
from typing import Optional, Sequence, Iterator
from dataclasses import dataclass
from random import random
from time import sleep

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
        return " `" if self.isBoarder else " x" if self.isAlive else " -"

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

    def nextIteration(self):
        self.__iteration += 1
        self.__currentGridIndex = self.__iteration % len(self.__grids)

        for position, cell in self.__grids[self.__currentGridIndex]:
            cell.isAlive = self.__grids[self.__currentGridIndex-1].checkCell(*position)
    
    def run(self):
        hasLooped: bool = False
        while not hasLooped:
            self.nextIteration()
            print(self)
            sleep(1)
            for i, grid in enumerate(self.__grids):
                if i == self.__currentGridIndex:
                    continue
                hasLooped = hasLooped or grid == self.__grids[self.__currentGridIndex]
    
    def __str__(self) -> str:
        return f"Generation {self.__iteration}\n{str(self.__grids[self.__currentGridIndex])}"

def main():
    game = GameController()
    game.run()
    print("Hello, World!")

if __name__ == '__main__':
    main()
