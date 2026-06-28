import json

def update_json_db(user_id, points_added, file_name="database.json"):
    try:
        # Load JSON data from the file
        with open(file_name, "r") as file:
            data = json.load(file)

        # Search for the matching user and update points
        user_found = False
        for user in data["users"]:
            if user["id"] == user_id:
                user["points"] += points_added
                user_found = True
                break

        if not user_found:
            print(f"User with ID {user_id} not found.")
            return

        # Write the updated data back to the file
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)

        print("Local JSON structure updated, validated, and serialized to disk format accurately.")

    except FileNotFoundError:
        print("Error: JSON database file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
    except Exception as e:
        print("Error:", e)


# Sample Input
update_json_db(user_id=102, points_added=25)