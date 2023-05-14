"""程式啟動點"""
from world import World


# 執行世界生物碰撞程序
if __name__ == "__main__":
    world = World()
    world.init(mode="random")
    print(world._sprites_position_dict)

    while len(world._sprites_position_dict):
        c1 = int(input("Input a coord of a sprite (int): "))
        c2 = int(input("Move to another coord (int): "))
        s1, s2 = world.get_sprite(coord=c1), world.get_sprite(coord=c2)
        assert s1.coord == c1
        if s2 is not None:
            world._collisionHandleChain.herohero.handle(
                source_sprite=s1, target_sprite=s2, world=world
            )
        else:
            world.move_sprite(source_coord=s1.coord, target_coord=c2)

        print(world._sprites_position_dict)
