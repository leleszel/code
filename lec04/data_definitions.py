"""More examples of data definitions (classes).

Two kinds:

  - Structs (named tuples)
  - Enums

Each class should have a purpose statement, and maybe some doctests.
"""


from enum import Enum, auto
from typing import Optional, NamedTuple
from lib230 import record


# Example 1: car share ride


class Person2(NamedTuple):
    id:     int
    name:   str


@record
class Person:
    id:     int
    name:   str


# TODO
@record
class Location:
    pass


@record
class Ride:
    """Represents a car-share ride.

    >>> Ride(3, 4, 5, 6)
    Ride(passenger=3, driver=4, start=5, end=6)
    >>> ride = Ride(3, 4, 5, 6)
    >>> ride.passenger
    3
    >>> ride.end
    6
    """
    passenger:  Person
    driver:     Person
    start:      Location
    end:        Location


# Example 2: cardinal directions


class CardinalDirection(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


def is_north_or_south(cd: CardinalDirection) -> bool:
    return (cd is CardinalDirection.NORTH
            or cd is CardinalDirection.SOUTH)


def is_multiple_of_3_or_5(n: int) -> bool:
    b3_ = n % 3 == 0
    b5_ = n % 5 == 0
    return b3_ or b5_


# Example 3: flowering plants


# Every plant has:
#  - name
#  - maximum height
#  - sun preference, which is one of:
#     - shade
#     - partial
#     - full


class SunPreference(Enum):
    SHADE = auto()
    PARTIAL = auto()
    FULL = auto()


@record
class FloweringPlant:
    name: str
    max_height: float
    sun_preference: SunPreference


def okay_for_under_ledge(audrey2: FloweringPlant) -> bool:
    return audrey2.max_height < 10 and \
           audrey2.sun_preference is not SunPreference.FULL


# Example 4: electronic medical records


class Sex(Enum):
    FEMALE = auto()
    MALE = auto()
    INTER = auto()


@record
class Biometrics:
    height:         float
    weight:         float
    age:            float
    sex:            Sex


@record
class BloodPressure:
    systolic:  float
    diastolic: float


@record
class Vitals:
    body_temperature: float
    blood_pressure: BloodPressure
    heart_rate: int
    breath_rate: int


@record
class MedicalRecord:
    id:             int
    name:           str
    biometrics:     Biometrics
    vitals:         Optional[Vitals]



