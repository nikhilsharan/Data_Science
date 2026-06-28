def execute_transaction(valid_query=True):
    try:
        print("Connecting to database...")

        if not valid_query:
            raise Exception("Invalid database query.")

        print("Executing transaction...")

    except Exception as e:
        print("Error:", e)

    else:
        print("Transaction logged successfully.")

    finally:
        print("Closing database connections resources cleanly.")


# Sample Input
execute_transaction(valid_query=True)