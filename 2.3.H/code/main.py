"""程式啟動點"""
from world import World


# 執行世界生物碰撞程序
if __name__ == "__main__":
    world = World()
    world.init(mode="random")
    print(world.sprites)

    while len(world.sprites):
        c1 = int(input("Input a coord of a sprite (int): "))
        c2 = int(input("Move to another coord (int): "))
        s1, s2 = world.get_sprite(coord=c1), world.get_sprite(coord=c2)
        assert s1.coord == c1
        if s2 is not None:
            world.collisionHandleChain.herohero.handle(
                source_sprite=s1, target_sprite=s2, world=world
            )
        else:
            world.move_sprite(source_coord=s1.coord, target_coord=c2)

        print(world.sprites)
