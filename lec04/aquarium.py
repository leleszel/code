# enables methods to return their own class type:
from __future__ import annotations

from typing import List, Optional
from enum import Enum, auto
from lib230 import record, Factory


class WaterType(Enum):
    """Represents the type of water that a fish requires."""
    FRESH = auto()
    BRACKISH = auto()
    SALT = auto()


@record
class Fish:
    """Represents a pet fish.

    >>> f = Fish('name', 5, 10)
    >>> f.weight_kg
    5
    >>> f.age_days
    10
    >>> f.species
    'unknown'
    """

    name:       str
    weight_kg:  float
    age_days:   int = 0
    species:    str = 'unknown'
    water_type: WaterType = WaterType.FRESH

    def increment_age(self) -> None:
        """Adds one day to the age of the fish.
        >>> f = Fish('Cleo', 0.03, 18, 'goldfish', WaterType.FRESH)
        >>> g = Fish('Cleo', 0.03, 18, 'goldfish', WaterType.FRESH)
        >>> h = f
        >>> f == g
        True
        >>> f is g
        False
        >>> f is h
        True
        >>> f.age_days
        18
        >>> f.increment_age()
        >>> f.age_days
        19
        >>> f.increment_age()
        >>> f.age_days
        20
        >>> g.age_days
        18
        >>> h.increment_age()
        >>> h.age_days
        21
        >>> f.age_days
        21
        """
        self.age_days += 1


@record
class Aquarium:
    """Represents an aquarium of two fish.

    >>> aq = Aquarium()
    >>> aq.append(Fish('A', 10))
    >>> aq.append(Fish('B', 8))
    >>> aq.append(Fish('C', 6))
    >>> aq.append(Fish('D', 10))
    >>> len(aq.all_fish)
    4
    >>> aq.all_fish[0].weight_kg
    10
    """

    all_fish: List[Fish] = Factory(list)

    def append(self, a_fish: Fish) -> None:
        self.all_fish.append(a_fish)

    def increment_all_ages(self) -> None:
        for fish in self.all_fish:
            fish.increment_age()

    def heaviest_fish(self) -> Optional[Fish]:
        best: Optional[Fish] = None
        for fish in self.all_fish:
            if best is None or fish.weight_kg > best.weight_kg:
                best = fish
        return best


    # def average_weight(self) -> float:
    #     return (self.fish1.weight_kg
    #             + self.fish2.weight_kg
    #             + self.fish3.weight_kg) / 3
    #


