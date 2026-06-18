"""
Design a function `create_id_generator` that demonstrates lexical scoping and variable encapsulation. It
must return an inner function closure that generates sequential, prefixed identity tracking strings (e.g.,
'EMP-1001', 'EMP-1002') every single time it is evaluated, without modifying any global state variables.
Sample Input: gen = create_id_generator('EMP', start=1000); gen(); gen()
Expected Output: First call: 'EMP-1000' | Second call: 'EMP-1001'
"""

def create_id_generator(prefix, start=1000):

    current = start

    def generate():
        nonlocal current

        result = f"{prefix}-{current}"
        current += 1

        return result

    return generate


gen = create_id_generator("EMP", start=1000)

print(gen())
print(gen())
print(gen())