class Event:
    def __init__(self):
        self.handlers = []

    def subscribe(self, handler):
        # Add the handler to the list if it's not already subscribed
        if handler not in self.handlers:
            self.handlers.append(handler)

    def unsubscribe(self, handler):
        # Remove the handler from the list if it exists
        if handler in self.handlers:
            self.handlers.remove(handler)

    def emit(self, *args):
        # Call all the stored handlers with the provided arguments
        for handler in self.handlers:
            handler(*args)
