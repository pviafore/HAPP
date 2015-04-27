from Queue import Queue

queue = Queue()

def get_command_queue():
    return queue

def get_input_commands():
    while True:
        yield queue.get(True)
