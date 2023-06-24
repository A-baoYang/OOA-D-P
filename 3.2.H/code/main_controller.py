import logging
from collections import deque
from typing import List


class MainController:
    def __init__(self) -> None:
        self._commands = {}
        self._command_pool = []
        self._done_stack = deque()
        self._undo_stack = deque()

    @property
    def commands(self) -> dict:
        return self._commands
    
    @property
    def command_pool(self) -> list:
        return self._command_pool
    
    @command_pool.setter
    def command_pool(self, command_pool: list) -> None:
        self._command_pool = command_pool

    def display_command_pool(self) -> str:
        display_msg = ""
        for idx, command in enumerate(self.command_pool):
            display_msg += f"({idx}) {command} "
        return display_msg

    def display_command_table(self) -> str:
        display_msg = ""
        for key, commands in self.commands.items():
            display_msg += f'{key}: {" & ".join([str(c) for c in commands])}\n'
        return display_msg

    def set_hotkey(self, key: str, command: "Command") -> None:
        self.commands[key] = [command]
        logging.info(f"快捷鍵設置完成 - {key}: {command}")

    def set_marco(self, key: str, commands: List["Command"]) -> None:
        self.commands[key] = commands
        logging.info(f"巨集快捷鍵設置完成 - {key}: {commands}")

    def execute_commands(self, commands: list) -> None:
        for _command in commands:
            _status_msg = _command.execute()

    def undo_marco(self, commands: list) -> None:
        for _command in commands:
            _status_msg = _command.undo()

    def press_key(self, key: str) -> None:
        if key in self.commands:
            self.execute_commands(self.commands[key])
            self._done_stack.append(self.commands[key])
        else:
            logging.info("此快捷鍵尚未匹配到動作")
        
    def reset(self) -> None:
        self.commands = {}
        logging.info("Commands has been reseted.")
    
    def undo(self) -> None:
        if not self._done_stack:
            logging.info("No action to undo.")
        else:
            _command = self._done_stack.pop()
            self.undo_marco(commands=_command)
            self._undo_stack.append(_command)

    def redo(self) -> None:
        if not self._undo_stack:
            logging.info("No action to redo.")
        else:
            _command = self._undo_stack.pop()
            self.execute_commands(_command)
            self._done_stack.append(_command)

    def interact(self) -> None:
        logging.info("Welcome to Main Controller\n")
        while True:
            mode = input(
                f"快捷鍵列表:\n{self.display_command_table()}\n"
                "(1) 快捷鍵設置 (2) Undo (3) Redo (4) 按下字母快捷鍵執行動作:\n"
            )
            
            if mode == "1":
                is_marco = input("設置巨集指令 (y/n): ")
                target_key = input("按下快捷鍵: ")

                if is_marco == "y":
                    command_idx = input(f"要將哪些指令設置到快捷鍵 {target_key} 上 (輸入數字用空格隔開):\n{self.display_command_pool()}\n")
                    command_idx = command_idx.split(" ")
                    self.set_marco(key=target_key, commands=[self.command_pool[int(idx)] for idx in command_idx])
                else:
                    command_idx = input(f"要將哪一道指令設置到快捷鍵 {target_key} 上 (輸入數字):\n{self.display_command_pool()}\n")
                    self.set_hotkey(key=target_key, command=self.command_pool[int(command_idx)])
            
            elif mode == "2":
                self.undo()
            elif mode == "3":
                self.redo()
            else:
                self.press_key(key=mode)

