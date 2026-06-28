class SystemExecutionError(Exception):
    """Custom high-level exception."""
    pass


def extract_index_record(out_of_bounds_index):
    records = ["Record1", "Record2", "Record3"]

    try:
        return records[out_of_bounds_index]
    except IndexError as e:
        # Exception chaining
        raise SystemExecutionError(
            "SystemExecutionError caused by underlying IndexError"
        ) from e


# Sample Input
try:
    extract_index_record(99)
except SystemExecutionError:
    import traceback
    traceback.print_exc()