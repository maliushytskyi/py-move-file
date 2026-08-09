import os


def move_file(command: str) -> None:
    """
    Move a file from one location to another, similar to the Linux
    'mv' command. Creates any missing intermediate directories.

    :param command: str, a command string in the form
        "mv <source_file> <destination_path>". If the destination
        path ends with '/', it's treated as a directory and the file
        keeps its original name inside it.
    """
    _, source_file, destination = command.split()

    if destination.endswith("/"):
        file_name = os.path.basename(source_file)
        destination = destination + file_name

    destination_dir = os.path.dirname(destination)

    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    with open(source_file, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source_file)
