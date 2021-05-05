from tourny import controller


def start_program():
    """Start the program by running the controller initialisation."""
    start = controller.Controller()
    return start


if __name__ == "__main__":
    """Start the programm as __main__"""
    start_program()
