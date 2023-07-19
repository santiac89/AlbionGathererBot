from pynput.keyboard import Key, Listener

class KeyboardCapture:
    def __init__(self):
        self.key = None
        self.listener = None
        self.func = None

    def on_key(self, func):
        self.func = func

    def on_release(self, key):
        self.func(key)

    def start(self):
        self.listener = Listener(on_release=self.on_release)
        self.listener.start()
        self.listener.join()

    def stop(self):
        self.listener.stop()