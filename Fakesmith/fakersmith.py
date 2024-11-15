import random
import json
import requests
import csv
import os
import faker
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()
fake = faker.Faker()

# Step 1: Generate Fake Identity
def generate_fake_identity():
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        data = response.json()['results'][0]
        identity = {
            "first_name": data['name']['first'],
            "last_name": data['name']['last'],
            "address": str(data['location']['street']['number']) + " " + data['location']['street']['name'],
            "city": data['location']['city'],
            "state": data['location']['state'],
            "username": data['login']['username'],
            "password": fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True),
            "dob_day": str(data['dob']['date'].split('-')[2][:2]),
            "dob_month": str(int(data['dob']['date'].split('-')[1])),  # Month as integer string
            "dob_year": str(data['dob']['date'].split('-')[0]),
            "gender": "1" if data['gender'] == 'male' else "2",
            "ssn": fake.ssn(),
            "car_number": fake.license_plate(),
            "relatives": [fake.name() for _ in range(random.randint(1, 3))],
            "phone_number": fake.phone_number(),
            "email": data['email']
        }
        return identity
    else:
        raise Exception("Failed to generate identity from API.")

# Step 2: Store generated identities in CSV file
def store_identity_csv(identity, filename='fake_identities.csv'):
    try:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([identity['first_name'], identity['last_name'], identity['address'], identity['city'], identity['state'], identity['username'], identity['password'], identity['dob_day'], identity['dob_month'], identity['dob_year'], identity['gender'], identity['ssn'], identity['car_number'], ";".join(identity['relatives']), identity['phone_number'], identity['email']])
    except Exception as e:
        console.print(f"[bold red]Failed to save identity to CSV:[/bold red] {e}")

# Step 3: Display Menu Options
def display_menu():
    console.print("\n[bold cyan]================= FakerSmith: Identity Generator ==================[/bold cyan]")
    console.print("1. Generate Basic Identity")
    console.print("2. Generate and Save Identity to CSV")
    console.print("3. View Last Generated Identity")
    console.print("4. Delete CSV File Contents")
    console.print("5. Display All Identities in CSV File")
    console.print("6. Generate Custom Number of Identities and Save to CSV")
    console.print("7. Search Identity by Name in CSV File")
    console.print("8. Exit")
    console.print("[bold cyan]====================================================================\n[/bold cyan]")

# Step 4: Handle Menu Actions
def handle_menu_action(choice):
    if choice == '1':
        identity = generate_fake_identity()
        display_identity(identity)
    elif choice == '2':
        identity = generate_fake_identity()
        display_identity(identity)
        store_identity_csv(identity)
    elif choice == '3':
        try:
            with open('fake_identities.csv', 'r') as file:
                lines = file.readlines()
                if lines:
                    last_identity = lines[-1].strip().split(',')
                    display_last_identity(last_identity)
                else:
                    console.print("[bold yellow]No identities found in CSV file.[/bold yellow]")
        except FileNotFoundError:
            console.print("[bold red]No CSV file found.[/bold red]")
    elif choice == '4':
        try:
            open('fake_identities.csv', 'w').close()
            console.print("[bold green]CSV file contents deleted successfully.[/bold green]")
        except Exception as e:
            console.print(f"[bold red]Failed to delete CSV file contents:[/bold red] {e}")
    elif choice == '5':
        try:
            with open('fake_identities.csv', 'r') as file:
                lines = file.readlines()
                if lines:
                    table = Table(title="All Identities in CSV File", box=box.ROUNDED)
                    table.add_column("Name", style="cyan", no_wrap=True)
                    table.add_column("Email", style="magenta")
                    table.add_column("Phone", style="green")
                    for line in lines:
                        identity = line.strip().split(',')
                        table.add_row(f"{identity[0]} {identity[1]}", identity[15], identity[14])
                    console.print(table)
                else:
                    console.print("[bold yellow]No identities found in CSV file.[/bold yellow]")
        except FileNotFoundError:
            console.print("[bold red]No CSV file found.[/bold red]")
    elif choice == '6':
        try:
            count = int(input("Enter the number of identities to generate: "))
            for _ in range(count):
                identity = generate_fake_identity()
                store_identity_csv(identity)
            console.print(f"[bold green]{count} identities generated and saved to CSV file.[/bold green]")
        except ValueError:
            console.print("[bold red]Invalid number. Please enter a valid integer.[/bold red]")
    elif choice == '7':
        name_to_search = input("Enter the first name or last name to search: ").lower()
        try:
            with open('fake_identities.csv', 'r') as file:
                lines = file.readlines()
                found = False
                for line in lines:
                    identity = line.strip().split(',')
                    if name_to_search in identity[0].lower() or name_to_search in identity[1].lower():
                        console.print(f"\n[bold green]Found Identity:[/bold green] {identity[0]} {identity[1]}, Address: {identity[2]}, {identity[3]}, {identity[4]}, Email: {identity[15]}, Phone: {identity[14]}")
                        found = True
                if not found:
                    console.print("[bold yellow]No identity found with the given name.[/bold yellow]")
        except FileNotFoundError:
            console.print("[bold red]No CSV file found.[/bold red]")
    elif choice == '8':
        console.print("[bold cyan]Exiting... Goodbye! Press Enter to close.[/bold cyan]")
        input()  # Wait for user to press Enter before closing
        exit()
    else:
        console.print("[bold red]Invalid choice. Please select a valid option.[/bold red]")

# Step 5: Display Generated Identity
def display_identity(identity):
    table = Table(title="Generated Identity", box=box.ROUNDED)
    table.add_column("Attribute", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    table.add_row("First Name", identity['first_name'])
    table.add_row("Last Name", identity['last_name'])
    table.add_row("Address", f"{identity['address']}, {identity['city']}, {identity['state']}")
    table.add_row("Username", identity['username'])
    table.add_row("Password", identity['password'])
    table.add_row("Date of Birth", f"{identity['dob_day']}/{identity['dob_month']}/{identity['dob_year']}")
    table.add_row("Gender", "Male" if identity['gender'] == '1' else "Female")
    table.add_row("SSN", identity['ssn'])
    table.add_row("Car Number", identity['car_number'])
    table.add_row("Relatives", ', '.join(identity['relatives']))
    table.add_row("Phone Number", identity['phone_number'])
    table.add_row("Email", identity['email'])
    console.print(table)

# Step 6: Display Last Generated Identity
def display_last_identity(last_identity):
    table = Table(title="Last Generated Identity", box=box.ROUNDED)
    table.add_column("Attribute", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    table.add_row("First Name", last_identity[0])
    table.add_row("Last Name", last_identity[1])
    table.add_row("Address", f"{last_identity[2]}, {last_identity[3]}, {last_identity[4]}")
    table.add_row("Username", last_identity[5])
    table.add_row("Password", last_identity[6])
    table.add_row("Date of Birth", f"{last_identity[7]}/{last_identity[8]}/{last_identity[9]}")
    table.add_row("Gender", "Male" if last_identity[10] == '1' else "Female")
    table.add_row("SSN", last_identity[11])
    table.add_row("Car Number", last_identity[12])
    table.add_row("Relatives", last_identity[13].replace(';', ', '))
    table.add_row("Phone Number", last_identity[14])
    table.add_row("Email", last_identity[15])
    console.print(table)

# Step 7: Main Process
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        handle_menu_action(choice)

if __name__ == "__main__":
    main()
