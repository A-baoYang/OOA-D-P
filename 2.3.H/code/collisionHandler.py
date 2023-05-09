"""定義碰撞處理及子類別"""
from abc import ABC, abstractmethod

from sprite import Sprite, Hero, Water, Fire


class CollisionHandler(ABC):
    """類別：碰撞處理"""

    def __init__(self) -> None:
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, handler: "CollisionHandler"):
        self._next = handler

    @abstractmethod
    def handle(
        self, source_sprite: Sprite, target_sprite: Sprite, world: "World"
    ) -> None:
        pass


class HeroHeroHandler(CollisionHandler):
    def __init__(self) -> None:
        super().__init__()

    def handle(
        self, source_sprite: Sprite, target_sprite: Sprite, world: "World"
    ) -> None:
        if isinstance(source_sprite, Hero) and isinstance(target_sprite, Hero):
            print("Move failed.")
        else:
            self.next.handle(
                source_sprite=source_sprite, target_sprite=target_sprite, world=world
            )


class HeroWaterHandler(CollisionHandler):
    def __init__(self) -> None:
        super().__init__()

    def handle(
        self, source_sprite: Sprite, target_sprite: Sprite, world: "World"
    ) -> None:
        if isinstance(source_sprite, Hero) and isinstance(target_sprite, Water):
            source_sprite.HP += 10
            target_coord = target_sprite.coord
            world.remove_sprite(coord=target_coord)
            world.move_sprite(
                source_coord=source_sprite.coord, target_coord=target_coord
            )
            source_sprite.coord = target_coord
        else:
            self.next.handle(
                source_sprite=source_sprite, target_sprite=target_sprite, world=world
            )


class HeroFireHandler(CollisionHandler):
    def __init__(self) -> None:
        super().__init__()

    def handle(
        self, source_sprite: Sprite, target_sprite: Sprite, world: "World"
    ) -> None:
        if isinstance(source_sprite, Hero) and isinstance(target_sprite, Fire):
            source_sprite.HP -= 10
            target_coord = target_sprite.coord
            world.remove_sprite(coord=target_coord)
            world.move_sprite(
                source_coord=source_sprite.coord, target_coord=target_coord
            )
            source_sprite.coord = target_coord
        else:
            self.next.handle(
                source_sprite=source_sprite, target_sprite=target_sprite, world=world
            )


class WaterWaterHandler(CollisionHandler):
    def __init__(self) -> None:
        super().__init__()

    def handle(
        self, source_sprite: Sprite, target_sprite: Sprite, world: "World"
    ) -> None:
        if isinstance(source_sprite, Water) and isinstance(target_sprite, Water):
            print("Move failed.")
        else:
            self.next.handle(
                source_sprite=source_sprite, target_sprite=target_sprite, world=world
            )


class WaterFireHandler(CollisionHandler):
    def __init__(self) -> None:
        super().__init__()

    def handle(
        self, source_sprite: Sprite, target_sprite: Sprite, world: "World"
    ) -> None:
        if isinstance(source_sprite, Water) and isinstance(target_sprite, Fire):
            world.remove_sprite(coord=source_sprite.coord)
            world.remove_sprite(coord=target_sprite.coord)
        else:
            self.next.handle(
                source_sprite=source_sprite, target_sprite=target_sprite, world=world
            )


class FireFireHandler(CollisionHandler):
    def __init__(self) -> None:
        super().__init__()

    def handle(
        self, source_sprite: Sprite, target_sprite: Sprite, world: "World"
    ) -> None:
        if isinstance(source_sprite, Fire) and isinstance(target_sprite, Fire):
            print("Move failed.")
        else:
            self.next.handle(
                source_sprite=source_sprite, target_sprite=target_sprite, world=world
            )
