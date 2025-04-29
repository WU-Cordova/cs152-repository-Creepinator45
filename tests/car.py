
from enum import Enum, auto


class Color(Enum):
    """An enumeration to represent the color of a car. 
        The enumeration is provided as an example of a simple object that can be used to test with your data structures.
    """
    NOT_SET = 0
    RED = 1
    BLUE = 2
    GREEN = 3
    BLACK = 4
    WHITE = 5

class Make(Enum):
    """An enumeration to represent the make of a car. 
        The enumeration is provided as an example of a simple object that can be used to test with your data structures.
    """
    NOT_SET = auto()
    TOYOTA = auto()
    FORD = auto()
    HONDA = auto()
    CHEVROLET = auto()
    DODGE = auto()

class Model(Enum):
    """An enumeration to represent the model of a car. 
        The enumeration is provided as an example of a simple object that can be used to test with your data structures.
    """
    NOT_SET = auto()
    CAMRY = auto()
    COROLLA = auto()
    ACCORD = auto()
    CIVIC = auto()
    FOCUS = auto()
    FUSION = auto()

class Car:
    """A class to represent a car. 
        The class is provided as an example of a complex object that can be used to test with your data structures. 
        It's good to test with complex objects to ensure that your data structures can handle things like sorting, deep copying, etc.
        The class also demonstrates the use of properties, which are a way to encapsulate instance variables and provide a way to control access to them.
        Notice the use of the @property decorator to define the getter and setter methods for the instance variables.
    """
    def __init__(self, vin: str='', color: Color=Color.NOT_SET, make: Make=Make.NOT_SET, model: Model=Model.NOT_SET) -> None:
        """Initializes a new Car object with the given vin, color, make, and model.
        
        Args:
            vin (str): A string representing the vehicle identification number.
            color (Color): A string representing the color of the car.
            make (Make): A string representing the make of the car.
            model (Model): A string representing the model of the car.

        Returns:
            None
        """
        self._vin = vin
        self._color = color
        self._make = make
        self._model = model

    @property
    def vin(self) -> str:
        """Gets the vin of the car.
        
            Examples:
                >>> car = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
                >>> print(car.vin)
                1234567890

            Returns:
                vin (str): A string representing the vehicle identification number.
        """
        return self._vin
    
    @vin.setter
    def vin(self, vin: str) -> None:
        """Sets the vin of the car.

        Examples:
            >>> car = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
            >>> car.vin = '0987654321'
            >>> print(car.vin)
            0987654321


        Args:
            vin (str): A string representing the vehicle identification number.
            
        Returns:
            None
        """
        self._vin = vin

    @property
    def color(self) -> Color:
        """Gets the color of the car.

            Examples:
                >>> car = Car('1234567890', 'red', 'Toyota', 'Camry')
                >>> print(car.color)
                red
            
            Returns:
                color (Color): The color of the car.
        """
        return self._color
    
    @color.setter
    def color(self, color: Color) -> None:
        """Sets the color of the car.

            Examples:
                >>> car = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
                >>> car.color = Color.BLUE
                >>> print(car.color)
                Color.BLUE
            
            Args:
                color (Color): The color of the car.
            
            Returns:
                None
        """
        self._color = color
    
    @property
    def make(self) -> Make:
        """Gets the make of the car.
        
            Examples:
                >>> car = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
                >>> print(car.make)
                Make.TOYOTA
            
            Returns:
                make (Make.TOYOTA): The make of the car."""
        return self._make
    
    @make.setter
    def make(self, make: Make) -> None:
        """Sets the make of the car.
        
            Examples:
                >>> car = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
                >>> car.make = Make.FORD
                >>> print(car.make)
                Make.FORD
            
            Args:
                make (Make): The make of the car.
            
            Returns:
                None
        """
        self._make = make

    @property
    def model(self) -> Model:
        """Gets the model of the car.
        
            Examples:
                >>> car = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
                >>> print(car.model)
                Model.COROLLA
            
            Returns:
                model (model): The model of the car.
        """
        return self._model
    
    @model.setter
    def model(self, model: Model) -> None:
        """Sets the model of the car.
        
            Examples:
                >>> car = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
                >>> car.model = Model.FOCUS
                >>> print(car.model)
                Model.FOCUS
            
            Args:
                model (Model): The model of the car.
            
            Returns:
                None
        """
        self._model = model

    def __eq__(self, other: object) -> bool:
        """Compares two Car objects for equality. Two Car objects are considered equal if their vin, color, make, and model are the same.
        
        Examples:
            >>> car1 = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
            >>> car2 = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
            >>> car1 == car2
            True

        Args:
            other (object): The object to compare with.
        
        Returns:
            is_equal (bool): True if the two Car objects are equal, False otherwise.
        """
        if not isinstance(other, Car): 
            return False
        return self.vin == other.vin and self.color == other.color and self.make == other.make and self.model == other.model
    
    def __ne__(self, other: object) -> bool:
        """Compares two Car objects for inequality. Two Car objects are considered unequal if their vin, color, make, or model are different.
        
        Examples:
            >>> car1 = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
            >>> car2 = Car(vin='987654321', color=Color.BLUE, make=Make.TOYOTA, model=Model.CAMRY)
            >>> car1 != car2
            True

        Args:
            other (object): The object to compare with.
        
        Returns:
            is_not_equal (bool): True if the two Car objects are not equal, False otherwise.
            
        """
        return not self.__eq__(other)

    def __str__(self) -> str:
        """Returns a string representation of the Car object.

        Examples:
            >>> car = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
            >>> print(car)
            Car(vin=1234567890, color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
        
        Returns:
            car_str (str): A string representation of the Car object.
            
        """
        return f'Car(vin={self.vin}, color={self.color}, make={self.make}, model={self.model})'

    def __repr__(self) -> str:
        """Returns a string representation of the Car object.
            
            Examples:
                >>> car = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
                >>> print(repr(car))
                Car(vin=1234567890, color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
                
            
            Returns:
                car_str (str): A string representation of the Car object.
        """
        return self.__str__()

    def __hash__(self) -> int:
        """Returns the hash value of the Car object.
            
                Examples:
                    >>> car = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
                    >>> print(hash(car))
                    1234567890
                
                Returns:
                    hash_value (int): The hash value of the Car object.
        """
        return hash(self.vin)

    def __lt__(self, other: 'Car') -> bool:
        """Compares two Car objects to determine if one is less than the other based on the vin.

            Examples:
                >>> car1 = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
                >>> car2 = Car(vin='9876543210', color=Color.BLUE, make=Make.TOYOTA, model=Model.CAMRY)
                >>> car1 < car2
                True
            
            Args:
                other (Car): The Car object to compare with.

            Returns:
                is_less_than (bool): True if the vin of the first Car object is less than the vin of the second Car object, False otherwise.

        """
        return self.vin < other.vin

    def __le__(self, other: 'Car') -> bool:
        """Compares two Car objects to determine if one is less than or equal to the other based on the vin.
        
            Examples:
                >>> car1 = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
                >>> car2 = Car(vin='9876543210', color=Color.BLUE, make=Make.TOYOTA, model=Model.CAMRY)
                >>> car1 < car2
                True
            
            Args:
                other (Car): The Car object to compare with.

            Returns:
                is_less_than_or_equal (bool): True if the vin of the first Car object is less than or equal to the vin of the second Car object, False otherwise.
        """
        return self.vin <= other.vin

    def __gt__(self, other: 'Car') -> bool:
        """Compares two Car objects to determine if one is greater than the other based on the vin.
        
            Examples:
                >>> car1 = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
                >>> car2 = Car(vin='9876543210', color=Color.BLUE, make=Make.TOYOTA, model=Model.CAMRY)
                >>> car1 > car2
                False
            
            Args:
                other (Car): The Car object to compare with.

            Returns:
                is_greater_than (bool): True if the vin of the first Car object is greater than the vin of the second Car object, False otherwise.
        """
        return self.vin > other.vin

    def __ge__(self, other: 'Car') -> bool:
        """Compares two Car objects to determine if one is greater than or equal to the other based on the vin.
        
            Examples:
                >>> car1 = Car(vin='1234567890', color=Color.RED, make=Make.TOYOTA, model=Model.COROLLA)
                >>> car2 = Car(vin='9876543210', color=Color.BLUE, make=Make.TOYOTA, model=Model.CAMRY)
                >>> car1 > car2
                False
            
            Args:
                other (Car): The Car object to compare with.

            Returns:
                is_greater_than_or_equal (bool): True if the vin of the first Car object is greater than or equal to the vin of the second Car object, False otherwise.
        """
        return self.vin >= other.vin