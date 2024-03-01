UNINTIALIZED_OBJECT = None

class Array:
    def __init__(self, data_type: type, size: int):
        self.data_type = data_type
        self.size = size

        self.items = [UNINTIALIZED_OBJECT]*size
        # Denotes the memory ^^^^

    def __setitem__(self, idx: int, value) -> None:
        return

    
