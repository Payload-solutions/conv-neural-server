"""
Examine and check the content files ernumerating it
Every time that the bot verify taht

:author: Arturo Negreiros (aka H0n3yL04d)
"""
from typing import (
    Dict,
    Any
)
from core.lib.shell_process import shell_execution
from core.lib.generics import ExaminePath



def examine(task_path: ExaminePath, listen: bool=True) -> ExaminePath:
    command = task_path["command"]
    target = task_path["target"]
    description = task_path["description"]

    content = shell_execution(cmd_command=f"{command} \
        {target} | wc -l")
    
    task_path["content"] = content
    return task_path

    
    