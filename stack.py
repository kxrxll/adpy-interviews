class Stack:
    def __init__(self):
        self._stack_container = []
        self._last_object_index = -1

    def isEmpty(self) -> bool:
        if not self._stack_container:
            return True
        return False

    def push(self, object_to_add: any) -> None:
        self._stack_container.append(object_to_add)
        self._last_object_index += 1

    def pop(self) -> any:
        result = self._stack_container[self._last_object_index]
        del self._stack_container[self._last_object_index]
        self._last_object_index -= 1
        return result

    def peek(self) -> any:
        return self._stack_container[self._last_object_index]

    def size(self) -> int:
        return self._last_object_index + 1
