# enables methods to return their own class type:
from __future__ import annotations
from typing import NamedTuple, List, Optional
from enum import Enum, auto


class WaterType(Enum):
    """Represents the type of water that a fish requires."""
    FRESH = auto()
    BRACKISH = auto()
    SALT = auto()


class Fish0(NamedTuple):
    """Represents a pet fish."""

    name:       str
    weight_kg:  float
    age_days:   int = 0
    species:    str = 'unknown'
    water_type: WaterType = WaterType.FRESH

    def increment_age(self) -> Fish0:
        """Adds one day to the age of this fish.

        >>> fish0 = Fish0('Cleo', 0.03, 18, 'goldfish', WaterType.FRESH)
        >>> fish0.age_days
        18
        >>> fish1 = fish0.increment_age()
        >>> fish1.age_days
        19
        >>> fish2 = fish1.increment_age()
        >>> fish2.age_days
        20
        >>> fish0.age_days
        18
        """
        return Fish0(self.name,
                    self.weight_kg,
                    self.age_days + 1,
                    self.species,
                    self.water_type)

    # changes how the object prints in the console:
    def __repr__(self) -> str:
        return self.name


class Aquarium2(NamedTuple):
    """Represents an aquarium of two fish."""

    fish1: Fish0
    fish2: Fish0

    def increment_all_ages(self) -> Aquarium2:
        """Returns a new aquarium in which every fish is one day
        older.

        >>> aq0 = Aquarium2(Fish0('Cleo', 0.03, 18, 'goldfish', WaterType.FRESH),
        ...                 Fish0('Larry', 150, 700, 'shark', WaterType.SALT))
        >>> (aq0.fish1.age_days, aq0.fish2.age_days)
        (18, 700)
        >>> aq1 = aq0.increment_all_ages()
        >>> (aq1.fish1.age_days, aq1.fish2.age_days)
        (19, 701)
        """
        return Aquarium2(self.fish1.increment_age(),
                         self.fish2.increment_age())

    def heaviest_fish(self) -> Fish0:
        """Returns whichever fish is heaviest. Ties go to fish1.

        >>> Aquarium2(Fish0('dory', 5), Fish0('nemo', 10)).heaviest_fish()
        nemo
        >>> Aquarium2(Fish0('dory', 15), Fish0('nemo', 10)).heaviest_fish()
        dory
        >>> Aquarium2(Fish0('dory', 10), Fish0('nemo', 10)).heaviest_fish()
        dory
        """
        if self.fish1.weight_kg >= self.fish2.weight_kg:
            return self.fish1
        else:
            return self.fish2

    def average_weight(self) -> float:
        """Returns the average fish weight
        >>> Aquarium2(Fish0('dory', 5), Fish0('nemo', 10)).average_weight()
        7.5
        >>> Aquarium2(Fish0('dory', 15), Fish0('nemo', 10)).average_weight()
        12.5
        """
        return (self.fish1.weight_kg + self.fish2.weight_kg) / 2


class Aquarium3(NamedTuple):
    """Represents an aquarium of three fish."""

    fish1: Fish0
    fish2: Fish0
    fish3: Fish0

    def increment_all_ages(self) -> Aquarium3:
        """Returns a new aquarium in which every fish is one day
        older.

        >>> aq0 = Aquarium3(Fish0('Cleo', 0.03, 18, 'goldfish', WaterType.FRESH),
        ...                 Fish0('Larry', 150, 700, 'shark', WaterType.SALT),
        ...                 Fish0('Otto', 500, 45, 'goldfish?', WaterType.FRESH))
        >>> (aq0.fish1.age_days, aq0.fish2.age_days, aq0.fish3.age_days)
        (18, 700, 45)
        >>> aq1 = aq0.increment_all_ages()
        >>> (aq1.fish1.age_days, aq1.fish2.age_days, aq1.fish3.age_days)
        (19, 701, 46)
        """
        return Aquarium3(self.fish1.increment_age(),
                         self.fish2.increment_age(),
                         self.fish3.increment_age())

    def heaviest_fish(self) -> Fish0:
        """Returns whichever fish is heaviest. Ties go to earliest."""
        def max_fish(f1: Fish0, f2: Fish0) -> Fish0:
            return Aquarium2(f1, f2).heaviest_fish()
        return max_fish(self.fish1, max_fish(self.fish2, self.fish3))

    def average_weight(self) -> float:
        """Returns the average fish weight."""
        return (self.fish1.weight_kg
                + self.fish2.weight_kg
                + self.fish3.weight_kg) / 3


class Fish:
    """Represents a pet fish."""

    name:       str
    weight_kg:  float
    age_days:   int
    species:    str
    water_type: WaterType

    def __init__(self,
                 name:       str,
                 weight_kg:  float,
                 age_days:   int = 0,
                 species:    str = 'unknown',
                 water_type: WaterType = WaterType.BRACKISH) -> None:
        self.name = name
        self.weight_kg = weight_kg
        self.age_days = age_days
        self.species = species
        self.water_type = water_type

    def increment_age(self) -> None:
        """Adds one day to the age of this fish.

        >>> fish0 = Fish('Cleo', 0.03, 18, 'goldfish', WaterType.FRESH)
        >>> fish1 = fish0
        >>> fish0.age_days
        18
        >>> fish0.increment_age()
        >>> fish0.age_days
        19
        >>> fish0.increment_age()
        >>> fish0.age_days
        20
        >>> fish1.age_days
        20
        """
        self.age_days += 1

    # changes how the object prints in the console:
    def __repr__(self) -> str:
        return self.name


class Aquarium(NamedTuple):
    """An aquarium of any number of fish."""
    all_fish: List[Fish] = []

    def append(self, fish: Fish) -> None:
        self.all_fish.append(fish)

    def increment_all_ages(self) -> None:
        for fish in self.all_fish:
            fish.increment_age()

    def heaviest_fish(self) -> Optional[Fish]:
        best = None
        for fish in self.all_fish:
            if best is None or fish.weight_kg > best.weight_kg:
                best = fish
        return best

    # average_weight?
    # all_heaviest_fish?

