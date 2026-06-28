class TransactionalState:
    def __init__(self, state):
        self.state = state
        self._backup = None

    def __enter__(self):
        # Save a copy of the original state
        self._backup = self.state.copy()
        return self.state

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            # Roll back to the original state
            self.state.clear()
            self.state.update(self._backup)
            print("State rolled back to pre-block conditions.")
            print("Exception handled safely.")
            return True  # Suppress the exception

        return False  # No exception occurred


# Sample Input
my_dict = {"balance": 1000}

with TransactionalState(my_dict):
    my_dict["balance"] = 5000
    raise RuntimeError("Transaction failed")

# Verify the rollback
print(my_dict)