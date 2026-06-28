"""
Utilize Python's native `abc` module to design an abstract contract blueprint class `PaymentProcessor` that
contains an `@abstractmethod` definition named `process_transaction()`. Create specialized concrete
subclasses `StripeProcessor` and `PayPalProcessor` that conform to this interface to show polymorphic
runtime execution.
Sample Input: processors = [StripeProcessor(), PayPalProcessor()];
[p.process_transaction(50) for p in processors]
Expected Output: Polymorphic calls successfully dispatching individual target
implementations.
"""
from abc import ABC, abstractmethod

# Abstract Base Class
class PaymentProcessor(ABC):

    @abstractmethod
    def process_transaction(self, amount):
        pass


# Concrete Subclass 1
class StripeProcessor(PaymentProcessor):

    def process_transaction(self, amount):
        print(f"Stripe: Processed payment of ${amount}.")


# Concrete Subclass 2
class PayPalProcessor(PaymentProcessor):

    def process_transaction(self, amount):
        print(f"PayPal: Processed payment of ${amount}.")


# Sample Input
processors = [StripeProcessor(), PayPalProcessor()]

# Polymorphic method calls
[p.process_transaction(50) for p in processors]