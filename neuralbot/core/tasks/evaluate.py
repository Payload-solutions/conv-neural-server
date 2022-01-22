
from core.lib.shell_process import shell_execution
from core.lib.generics import ExaminePath


def evaluate(task_path: ExaminePath) -> ExaminePath:
    command = task_path["command"]
    target = task_path["target"]
    description = task_path["description"]

    content = shell_execution(cmd_command=f"cd /home/payload/Projects/conv-neural-server;{command}")
    
    print(content)