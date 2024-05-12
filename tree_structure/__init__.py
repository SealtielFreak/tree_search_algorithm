import dataclasses

from tree_structure.point import Point
from tree_structure.rect import Rect
from tree_structure.tree import TreeNode


@dataclasses.dataclass
class TreeConfiguration:
    rect: Rect
    size: tuple
    n_it: int


class Vector:
    def __init__(self, position: Point, z: float | int, parent=None):
        self.position = position
        self.__z = z
        self.__parent = parent

    @property
    def parent(self):
        return self.__parent

    @property
    def z(self):
        return self.__z

    def __gt__(self, other: int | float):
        return self.z < other

    def __lt__(self, other: int | float):
        return self.z > other

    def __iter__(self):
        return iter(self.position)
