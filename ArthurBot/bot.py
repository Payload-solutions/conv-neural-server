#!/usr/bin/python3

import requests
import time
import os
import sys
from pwn import *
import json
import subprocess
from pprint import pprint



class ArthurBot:

    def __init__(self, path: str):
        log.progress("Executing bot. ready for tasks")
        time.sleep(2)
        self.path = path
        with open(self.path, "r") as file:
            self.tasks = json.load(file)

        self.keys = [x for x in self.tasks.keys()]
        self.task_list = [self.tasks[x] for x in self.keys][0]
        self.pid = os.getpid()

    def execute_tasks(self, command: str):
        try:
            my_path = self.task_list[command]

            if isinstance(my_path, dict):
                for x in my_path:
                    if my_path[x] == "":
                        print(my_path[x], x)
            else:
                os.system(my_path)

        except KeyboardInterrupt:
            exit(1)
        except Exception as e:
            log.error(str(e))
    
    def index_another_task(self,keyname: str, command: str):
        # log.info(str(self.pid))
        self.execute_tasks(self.task_list["replicate"])
        # log.info(self.tasks["tasks"])
        # log.info(self.keys)
        # log.info(self.task_list)
    
    def go_to_sleep(self, duration: int):
        time.sleep(duration)
        

def main():

    bot = ArthurBot("roadmap.json")
    # bot.index_another_task("", "")
    bot.execute_tasks("examine")

if __name__ == "__main__":
    main()

