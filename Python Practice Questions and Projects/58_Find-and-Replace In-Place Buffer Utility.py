def update_configuration(file_path, target_keyword, replacement):
    try:
        # Open the file and load its contents into memory
        with open(file_path, "r") as file:
            content = file.read()

        # Perform find-and-replace
        updated_content = content.replace(target_keyword, replacement)

        # Rewrite the updated content back to the file
        with open(file_path, "w") as file:
            file.write(updated_content)

        print("File updated and rewritten successfully with zero content duplication errors.")

    except FileNotFoundError:
        print("Error: Configuration file not found.")
    except Exception as e:
        print("Error:", e)


# Sample Input
update_configuration(
    "config.txt",
    "DEV_HOST",
    "PROD_DB"
)