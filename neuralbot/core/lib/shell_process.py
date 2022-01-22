
from subprocess import (
    check_output,
    STDOUT
)

def shell_execution(cmd_command: str) -> str:
    output = check_output(cmd_command, 
            stderr=STDOUT, 
            shell=True).decode().strip("\n")
    return output


