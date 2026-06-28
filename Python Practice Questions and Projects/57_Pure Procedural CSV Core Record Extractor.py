# Read the CSV file without using the csv module
filtered_rows = []

with open("employees.csv", "r") as file:
    # Skip the header row
    next(file)

    for line in file:
        # Remove newline and split manually using commas
        fields = line.strip().split(",")

        # Filter rows where Age > 25
        if int(fields[1]) > 25:
            filtered_rows.append(fields)

# Display the filtered rows
print("Filtered output for Age > 25:", filtered_rows)