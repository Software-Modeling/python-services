"""
This is a module used to define an example of an abstract class.

Author: Juan Bedoya <jebedoyal@udistrital.edu.co>
==================================================
LICENSE - FOSS [Free Open Software Source]
"""

from abc import ABC, abstractmethod
from typing import Any #type-hint

class AbstracClass(ABC):
    """This class is a fingerprint for some concrete example classes."""

    def __init__(self, parameter:Any):
        self.main_attr = parameter
    
    @abstractmethod
    def abstract_method(self):
        """This method is an abstract method."""

    
class ConcreteClass(AbstracClass):
    """This class is a concrete example of the abstract class."""

    def __init__(self, parameter:Any):
        super().__init__(parameter)

    def abstract_method(self):
        print(f"ConcreteClass: {self.main_attr}")

if __name__ == "__main__":
    concrete_object = ConcreteClass("Hello")
    concrete_object.abstract_method()
