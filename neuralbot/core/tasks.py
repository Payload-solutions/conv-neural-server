"""
Examine and check the content files ernumerating it
Every time that the bot verify taht

:author: Arturo Negreiros (aka H0n3yL04d)
"""

from .lib.shell_process import shell_execution
from .lib.generics import ExaminePath
import subprocess
import requests
import hashlib

def testing(task_path: ExaminePath) -> ExaminePath:
    """
    The testing task wont make a change in the roadmap.jsonfile, 
    this is only for prove that the unittesting works fine.
    """
    command = task_path["command"]
    # target = task_path["content"]
    content = shell_execution(f"{command}")
    print(content)


def examine(task_path: ExaminePath, listen: bool = True) -> ExaminePath:
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


def test_url_method(url: str) -> bool:

    sess = requests.session()
    ress = sess.post(url=url, files={
        "formImageFiles": open("arturo.jpg", "rb")
    })
    print(ress.text)


# utilities
def choose_the_bigger():
    data_val = {
        "prediction": {
            "low": "0.6167120933532715",
            "non": "0.006852846127003431",
            "reg": "0.3764350414276123"
        }
    }
    pred = data_val["prediction"]
    list_acc = sorted([pred[x] for x in pred], reverse=True)
    bigger = {key: val for key, val in pred.items()
              if val == list_acc[0]}
    return bigger


# hasing files
def encoding_file_name(file_name: str) -> str:
    file_name = file_name.split(".")[0]
    file_encoded = hashlib.md5(file_name.encode()).hexdigest()
    return file_encoded+".png"



def selection_image(convolution_prove: Dict[str, float],
                    temporal_path: str) -> None:
    r"""
    Basically, this function it's whenever neural training have 
    to make a decission for the image saved in the tem/image

    >>> if the accuracy is lesser or equal to the max accuracy
        and greter the loss value, then save the image in the

    :params: convolution_prove=The content whenever a test of
                image works, but we need to know if the value 
                it's secure to save in the folders for the neural
                test.

                if convolution_prove["wherever key"] <= 0.74 \
                    and convolution_prove["wherever key] > 0.68:

                    save_the_image("path_image")
                else:
                    remove_image_from_temporal_folder 
    """
    pass
