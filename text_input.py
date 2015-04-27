from threading import Thread
def load_text_input(queue):
    def get_user_input():
        while True:
            text = raw_input()
            queue.put(text)
    thread = Thread(target=get_user_input)
    thread.daemon = True
    thread.start()
