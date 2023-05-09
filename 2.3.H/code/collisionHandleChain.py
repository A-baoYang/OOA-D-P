"""將 Handler 彼此串連"""
from collisionHandler import (
    HeroHeroHandler,
    HeroWaterHandler,
    HeroFireHandler,
    WaterWaterHandler,
    WaterFireHandler,
    FireFireHandler,
)


class CollisionHandleChain:
    def __init__(self) -> None:
        self.herohero = HeroHeroHandler()
        self.herowater = HeroWaterHandler()
        self.herofire = HeroFireHandler()
        self.waterwater = WaterWaterHandler()
        self.waterfire = WaterFireHandler()
        self.firefire = FireFireHandler()

    def chain(self) -> None:
        self.herohero.next = self.herowater
        self.herowater.next = self.herofire
        self.herofire.next = self.waterwater
        self.waterwater.next = self.waterfire
        self.waterfire.next = self.firefire
