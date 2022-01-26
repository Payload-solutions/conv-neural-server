#!/usr/bin/python3

"""
This is the simulation of a virtual assistant
obviously, make your life more easy :)

Indeed, this virtual assistas as it's described
in the parser arguments, try to make your training,

"""

from subprocess import(
    check_output,
    STDOUT
)
import textwrap
from typing import (Any,
                    Dict
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
import yaml
from neuralbot.core.tasks import (
    testing,
    examine,
    evaluate
)

try:
    import yaml
except ImportError as e:
    print("Not installed yaml, please try to install using \
            the pip install pyyaml")


NEW_TASK_CONTENT = """
{
    "tasks":{
        "examine":{
          "command":"ls -l",
          "target":"file_test_dirs",
          "content": "",
          "description":"enumerate all folder content to \
                  get the actual content"
        },
        "replicate":{
            "command": "cp",
            "target":"",
            "description":"clone differents files from \
                    the director target"
        },
        "execute":{
            "command":"./",
            "target":"",
            "description":"run an executable file of the \
                    following form: './example.py' "
        },
        "evaluate":{
            "description":"virtual assistant for the improving \
                    of the neural network accuracy",
            "command":"python ",
            "target":".bacteria_trained.hdf5",
            "enumerate folders":"ls",
            "accuracy":"",
            "content":""
        },
        "testing":{
            "description":"testing the web application",
            "command":"python ",
            "target":"tests/"
        }
    }
}

"""


class ArthurBot:

    def __init__(self, path: str, args: Any):
        self.args = args
        log.progress("Executing bot. ready for tasks")
        time.sleep(2)
        self.path = path

        with open(self.path, "r") as file:
            self.task_file = json.load(file)

        self.tasks = self.task_file["tasks"]
        self.pid = os.getpid()
        
        # the original size of the 
        # train, test and validator directory...
        self.train_dir = self.image_directory("train")
        self.test_dir = self.image_directory("test")
        self.valid_dir = self.image_directory("validator")

    def image_directory(self, directory: str):
        low = len(os.listdir(f"app/Net/image_set/{directory}/Low_fat_yogurt"))
        non = len(os.listdir(f"app/Net/image_set/{directory}/Non_fat_yogurt"))
        reg = len(os.listdir(f"app/Net/image_set/{directory}/Regular_yogurt"))

        dir_object =  {
            "low":low,
            "non":non,
            "reg":reg
        }

        all_dir = sum([x for k, x in dir_object.items()])

        return all_dir

    def overwrite(self, content: Any, file_type: str = "json"):
        file_type = file_type.lower()
        file_confirmation: bool = file_type == "json" or \
            file_type == "yaml" or file_type == "yml"

        if not file_confirmation:
            raise FileFormaterError()

        log.info("Everything ok!!")

    def execute_tasks(self):

        task = self.args.task.lower()
        if self.args.listen:
            try:
                while True:

                    log.info("executing command...")
                    log.info("getting and writing the new content")

                    self.task_file["tasks"][task] = examine(self.tasks[task])
                    self.save_roadmap(self.task_file)

                    log.info("sleeping...")
                    self.go_to_sleep(3)

            except KeyboardInterrupt:
                log.info("[!] Exiting...")
                exit(0)
            except Exception as e:
                log.warn("[x] Something went wrong")
                print(f"\n\nError by: {str(e)}\n\n")
                exit(1)

        self.task_file["tasks"][task] = examine(self.tasks[task])
        self.save_roadmap(self.task_file)
    
    def evaluate_tasks(self):
        task = self.args.task.lower()

        try:
            evaluate(self.tasks[task])
        except Exception as e:
            print(f"{str(e)}")
            exit(1)
        finally:
            log.success("evaluations finished, no errors ocurred!")

    def testing_tasks(self):

        os.environ["FLASK_ENV"] = "testing"

        try:
            task = self.args.task.lower()
            pprint(self.tasks[task])
            log.info("Implementing the testing")
            testing(self.tasks[task])
        except Exception as e:
            log.warn(f"Something went wrong in the {task}!")
            print(f"{str(e)}")
            exit(1)
        except KeyboardInterrupt:
            log.warn("finishing...")
            exit(0)
        finally:
            log.success(f"{task} finsihed, no errors ocurred!")
        

    def save_roadmap(self,
                     content: Any,
                     new_name: str = "task_files/") -> None:

        try:
            with open(f"{new_name}new_backup.json", "w") as file:
                json.dump(content, file, indent=4)
            
            with open(f"{new_name}new_backup.yaml", "w") as file:
                yaml.dump(content, file, indent=4)

        except Exception as e:
            print(f"Error by {str(e)}")

    def go_to_sleep(self, duration: int):
        time.sleep((duration*60))


    def run(self):
        # automatic function

        task, listen = self.args.task, self.args.listen
        log.info("Loading the number of the directory...")
        print(self.train_dir)
        
        
        while True:
            self.train_dir = self.image_directory("train")
            try:
                train_dir = self.train_dir
                log.info(f"The current size of the directory is {train_dir}")
                new_train_dir = self.image_directory("train")
                time.sleep(3)
                log.info(f"The new current directory size {new_train_dir}")

                time.sleep(3)
                log.info("initializing the training...")
                evaluate(self.tasks["evaluate"])
                # self.go_to_sleep(2)
                
            except KeyboardInterrupt:
                log.warn(f"finishing the {task}")
                exit(0)
            except Exception as e:
                print(str(e))
                exit(0)




def main():
    parser = argparse.ArgumentParser(description='AthurBot, virtual \
            assistant',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent(f"""
            1) You must make executable the bot => chmod +x neuron-bot.py

            2) Here is the content of the possibles task to perform by
                the bot
            
            3) If you want to use the automatic task, first you must to
                select --task automatic or -t auotmatic, followd by the 
                -l or --listen to make the bot automatic for several tasks
    """))

    parser.add_argument('-t', '--task',
            help='task to do')
    parser.add_argument('-m', '--mode',
            help="indicate the mode to the neuron bot")

    parser.add_argument('-l', '--listen', action="store_true",
            help="indicate if the bot will be in listen mode or not")

    args = parser.parse_args()


    try:
        bot = ArthurBot(path="neuralbot/task_files/roadmap.json",
                        args=args)
        
        if args.task == "examine":
            bot.execute_tasks()
        
        elif args.task == "evaluate":
            bot.evaluate_tasks()
        
        elif args.task == "testing":
            bot.testing_tasks()

        elif args.task == "automatic" and args.listen:
            bot.run()
        
        # elif args.task == 

    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
