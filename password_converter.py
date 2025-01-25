"""
This is a converter script for a .txt file export from StickPass (a password manager)
into a CSV format which works for ProtonPass.

This conversion enabled me to move all passwords across.
"""
import os
import csv

def parse_txt_file(file_path):
    """Parse the .txt file and extract account information."""
    with open(file_path, 'r') as file:
        content = file.read()

    accounts = []
    entries = content.split("\n\n")  # Split into account entries by double newline
    for entry in entries:
        lines = entry.strip().split("\n")  # Split each entry into lines
        if len(lines) == 4:
            account = {
                "name": lines[0].split(": ")[1],
                "url": lines[1].split(": ")[1],
                "email": lines[2].split(": ")[1],
                "username": lines[2].split(": ")[1],
                "password": lines[3].split(": ")[1],
                "note": "",
                "totp": "",
                "vault": "Personal",
            }
            accounts.append(account)

    return accounts

def save_as_csv(accounts, output_file):
    """Save the accounts data as a CSV file."""
    header = [
        "name", "url", "email", "username", "password", "note", "totp", "vault"
    ]

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        # Add the informational row
        writer.writerow({
            "name": "Info about importing",
            "note": "All fields in this CSV are optional and can be empty. Please do not modify the titles of the columns. For security, you may delete this file after successfully importing passwords to Proton Pass."
        })
        for account in accounts:
            writer.writerow(account)

def main():
    input_file = "MainDatabase.txt"  # Replace with your input file path
    output_csv = "web_accounts.csv"

    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    accounts = parse_txt_file(input_file)

    # Save as CSV
    save_as_csv(accounts, output_csv)
    print(f"Accounts saved to CSV file: {output_csv}")

if __name__ == "__main__":
    main()
    