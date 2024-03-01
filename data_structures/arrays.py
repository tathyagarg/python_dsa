class UninitializedObject:
    ...

class Array:
    def __init__(self, data_type: type, size: int):
        if size == 0:
            raise ValueError("Tried to initialize array with length 0.")

        self._data_type = data_type
        self._size = size

        self._items = [UninitializedObject()]*size
        # Denotes the memory ^^^^

    def _check_index_validity(self, idx: int) -> bool:
        check_idx: int = idx-1 if idx > 0 else abs(idx)

        if check_idx > self._size:
            raise IndexError(f"Attempted to access index {idx=} in array with only {self._size} items")
        return True
    
    def _check_value_type_validity(self, value, check_type: type = None) -> bool:
        check_type = check_type or self._data_type
        if not isinstance(value, check_type) and not (
                (type(value) is int and self._data_type is float) or 
                (type(value) is float and self._data_type is int)
            ):
            raise TypeError(f"Object {value=} has incorrect type. Expected type {check_type!r}, got {type(value)!r}")
        return True

    def __setitem__(self, idx: int, value) -> None:
        try:
            self._check_value_type_validity(value=value)
            self._items[idx] = value
        except IndexError as ie:
            return ie

    def __getitem__(self, idx: int):
        try:
            self._check_index_validity(idx=idx)

            item: self._data_type | UninitializedObject = self._items[idx]
            if isinstance(item, UninitializedObject):
                raise IndexError(f"Attempted to access uninitialized index {idx=} in array.")
            return item     
        except (TypeError, IndexError) as e:
            return e

    
    def __delitem__(self, idx: int):
        try:
            self._check_index_validity(idx)

            del self._items[idx]
            self._size -= 1
        except IndexError as ie:
            return ie

    def append(self, item):
        try:
            self._check_value_type_validity(value=item)

            self._size += 1
            self._items.append(item)
        except TypeError as te:
            return te
        
    def pop(self, index: int = -1):
        try:
            self._check_index_validity(idx=index)

            self._size -= 1
            return self._items.pop(index)
        except IndexError as ie:
            return ie

    def remove(self, value):
        try:
            self._check_value_type_validity(value=value)

            for index, item in self._items:
                if item == value:
                    self._items.remove(index)
                    return
            else:
                return ValueError(f"Could not location item {value} in array.")
        except (TypeError, ValueError) as e:
            return e

    def reverse(self) -> list:
        self._items = self._items[::-1]
        return self._items

    def __repr__(self) -> str:
        return f"Array<size={self._size}, data_type={self._data_type}, items={self._items}>"

    def __str__(self) -> str:
        return f"[" + ", ".join(list(map(str, self._items))) + "]"

    def extend(self, items):
        try:
            self._check_value_type_validity(items, self.__class__)
            if items._data_type != self._data_type and not (
                (items._data_type is int and self._data_type is float) or 
                (items._data_type is float and self._data_type is int)
            ):
                raise TypeError(f"Expected items to have type {self._data_type!r}, got {items._data_type!r}")
            
            self._size += items._size
            self._items.extend(items)
        except TypeError as e:
            return e
    
    def __iter__(self):
        yield from self._items

