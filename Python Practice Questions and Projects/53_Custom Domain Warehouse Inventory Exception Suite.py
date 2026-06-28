class InventoryDeficitError(Exception):
    """Custom exception raised when inventory is insufficient."""

    def __init__(self, sku, deficient_quantity):
        self.sku = sku
        self.deficient_quantity = deficient_quantity
        super().__init__(
            f"{sku} requires {deficient_quantity} more units to fulfill total order."
        )


# Sample inventory
inventory = {
    "SKU-902": 380
}


def deduct_stock(sku, quantity_demanded):
    if sku not in inventory:
        raise ValueError(f"SKU '{sku}' not found.")

    available = inventory[sku]

    if quantity_demanded > available:
        deficit = quantity_demanded - available
        raise InventoryDeficitError(sku, deficit)

    inventory[sku] -= quantity_demanded
    print(f"Stock deducted successfully. Remaining stock: {inventory[sku]}")


# Sample Input
try:
    deduct_stock(sku="SKU-902", quantity_demanded=500)
except InventoryDeficitError as e:
    print(f"Raises: InventoryDeficitError('{e}')")