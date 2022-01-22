#!/usr/bin/python3


from typing import (
    Any,
    Dict,
    List
)
import requests
import time
import os
import sys
from pwn import *
import json
import subprocess
from pprint import pprint
import argparse




class CommandNotFoundException(Exception):
    def __init__(self, message="The command presented"):
        self.message = message
        super().__init__(self.message)

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
        self.JSON_PATH = "roadmap"

    
    def overwrite(self, content: roadmap_path, file_path: str, type: str):
        type_save = None
        if type == "new appending":
            type_save = "a"


        with open(file_path, type_save) as file:
            pass

    def execute_tasks(self, command: str):
        """
        {
            "tasks":{
                "examine":{
                    "enumerate folders":"ls -la",
                    "content": ""
                },
                "enumerate": "",
                "replicate":"cp",
                "execute":"./",
                "evaluate":{
                    "description":"virtual assistant for the improving of the neural network accuracy",
                    "command":"python ",
                    "target":".bacteria_trained.hdf5",
                    "enumerate folders":"ls",
                    "accuracy":"",
                    "content":""
                },
                "testing":{
                    "description":"testing the web application",
                    "command":"python ",
                    "target":".bacteria_trained.hdf5",
                    "enumerate folders":"ls",
                    "accuracy":"",
                    "content":""
                }
            }
        }
        """
        command = command.lower()
        if command == "examine":
            try:
                command = "examine"
                print(command)
                my_path = self.task_list[command]
                # print("my_path", my_path["content"])
                try:
                    if isinstance(my_path["content"], list):
                        log.info("List content...")
                        log.info("appending...")
                        self.task_list[command]["content"].append(os.listdir())
                    else:
                        log.info("it's not a list()...")
                        list_content = list()
                        list_content.append(os.listdir())
                        self.task_list[command]["content"] = list_content
                except Exception as e:
                    log.warn(f"{str(e)}")
            except KeyboardInterrupt:
                log.info("Exiting...")
                exit(1)
            except Exception as e:
                log.warn(str(e))
                
            self.index_another_task(content=self.tasks, new_name="new_roadmap")

        elif command == "":
            pass


    def index_another_task(self, content: roadmap_path, new_name: str) -> None:
        
        with open(f"{new_name}.json", "w") as file:
            json.dump(content, file, indent=4)
        log.success("new roadmap file saved...")

    def go_to_sleep(self, duration: int):
        """
        Args:
            duration (int): [the duration variable must be
            in integer, denoting the number os seconds, perhaps
            you should to set as for example: 600 seconds to 
            indicate that the time to sleep should be 10 minutes]
        """
        time.sleep(duration)
    


def main():

    bot = ArthurBot("roadmap.json")
    command = input("")
    bot.execute_tasks(command)

if __name__ == "__main__":
    main()


