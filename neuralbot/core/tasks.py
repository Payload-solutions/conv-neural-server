"""
Examine and check the content files ernumerating it
Every time that the bot verify taht

:author: Arturo Negreiros (aka H0n3yL04d)
"""

from .lib.shell_process import shell_execution
from .lib.generics import ExaminePath
import subprocess


def testing(task_path: ExaminePath) -> ExaminePath:
    # command = task_path["command"]
    # # target = task_path["content"]

    # content = shell_execution(f"{command}")
    # print(content)

    output = subprocess.check_output("flask test", stderr=subprocess.STDOUT, shell=True)

    print(output.decode())



def examine(task_path: ExaminePath, listen: bool=True) -> ExaminePath:
    command = task_path["command"]
    target = task_path["target"]
    description = task_path["description"]

    content = shell_execution(cmd_command=f"{command} \
        {target} | wc -l")
    
    task_path["content"] = content
    return task_path


def evaluate(task_path: ExaminePath) -> ExaminePath:
    command = task_path["command"]
    target = task_path["target"]
    description = task_path["description"]
    content = shell_execution(cmd_command=f"{command}")
    print(content)
