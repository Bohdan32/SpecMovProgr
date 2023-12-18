def write_into_file(file_path: str, text: str) -> None:
    """
    Write text into a file. May raise PermissionError or OSError.

    :param file_path:
    :param text:
    :raises PermissionError: If the user does not have permission to write to the file.
    :raises OSError: If the file is not a file.
    :raises FileNotFoundError: If the file does not exist.
    """
    with open(file_path, "w") as file:
        file.write(text)


def read_from_file(file_path: str) -> str:
    """
    Read text from a file. May raise FileNotFoundError, PermissionError, or OSError.

    :param file_path: The path to the file to read from.
    :return: The content of the file as a string.
    :raises FileNotFoundError: If the file does not exist.
    :raises PermissionError: If the user does not have permission to read the file.
    :raises OSError: If the file is not a file.
    """
    with open(file_path, "r") as file:
        return file.read()
