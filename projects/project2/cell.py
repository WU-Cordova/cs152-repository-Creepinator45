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
