class Class:
    prev_value = 0

    @staticmethod
    def get_number():
        if Class.prev_value == 0:
            Class.prev_value = 1
            return 1
        else:
            Class.prev_value *= 2
            return Class.prev_value
