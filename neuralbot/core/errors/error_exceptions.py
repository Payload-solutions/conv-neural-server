



class CommandNotFoundException(Exception):
    def __init__(self, message: str = """the command that you try
            to execute, it's not found"""):
        self.message = message
        super().__init__(self.message)

class FileFormaterError(Exception):
    def __init__(self, message: str="""The format file that
    you're trying to use it's not permited for this function
    Files permited:
        -json
        -yaml
        -yml
    """):
        self.message = message
        super().__init__(self.message)


class ElementNotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)