from CardGame.utils import log_setting
from main_controller import MainController
from tank import Tank
from telecom import Telecom
from tank_commands import TankMoveForward, TankMoveBackward
from telecom_commands import TelecomConnect, TelecomDisconnect


if __name__ == "__main__":

    log_setting(log_folder="logs-3.2.H")

    tank = Tank()
    telecom = Telecom()
    controller = MainController()
    controller.command_pool = [TankMoveForward(tank), TankMoveBackward(tank), TelecomConnect(telecom), TelecomDisconnect(telecom)]
    controller.interact()
