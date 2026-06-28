def safe_lookup(data, keys):
    """
    Safely retrieves a value from nested dictionaries.
    
    Args:
        data (dict): The nested dictionary.
        keys (list): List of keys representing the lookup path.

    Returns:
        The value if found, otherwise None.
    """
    try:
        for key in keys:
            data = data[key]
        return data
    except (KeyError, TypeError):
        return None


# Sample Input
result = safe_lookup({'a': {'b': 2}}, ['a', 'x', 'y'])

# Output
print("Return Value:", result)