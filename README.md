# FakerSmith: Identity Generator

FakerSmith is a command-line tool for generating fake identities, complete with realistic details like names, addresses, SSNs, car numbers, and more. This project uses the Faker library and `randomuser.me` API to provide comprehensive fake profiles that can be used for testing or research purposes.

## Features

- Generate detailed fake identities, including:
  - Name (First and Last)
  - Address (Street, City, State)
  - Username and Password (Securely generated)
  - Date of Birth
  - Gender
  - SSN (Social Security Number)
  - Car Number
  - Phone Number
  - Email Address
  - Relatives' names
- Save generated identities to a CSV file.
- Display previously generated identities.
- Search for identities by name.

## Requirements

To run FakerSmith, you need the following installed on your system:

- Python 3.x
- `requests` library
- `faker` library
- `rich` library for improved console output

You can install the required Python libraries by running:

```sh
pip install requests faker rich
```

## Usage

To use FakerSmith, simply run the Python script from your terminal or command prompt:

```sh
python fakersmith.py
```

Alternatively, you can use the provided batch script to quickly launch FakerSmith:

1. Create a batch file (e.g., `open_fakersmith.bat`) in the same folder as `fakersmith.py`.
2. Use the following content for the batch file:

```batch
@echo off
rem Batch script to open FakerSmith Identity Generator

set SCRIPT_PATH="fakersmith.py"

if exist %SCRIPT_PATH% (
    echo Starting FakerSmith Identity Generator...
    python %SCRIPT_PATH%
) else (
    echo Error: Could not find FakerSmith script in the current directory.
    pause
)

pause
```
3. Save the batch file and double-click it to start FakerSmith.

## Menu Options

Upon running `fakersmith.py`, you'll be presented with the following menu options:

1. **Generate Basic Identity**: Creates a new fake identity and displays it.
2. **Generate and Save Identity to CSV**: Creates a new identity and saves it to a CSV file.
3. **View Last Generated Identity**: Displays the last generated identity saved in the CSV file.
4. **Delete CSV File Contents**: Clears all saved identities from the CSV file.
5. **Display All Identities in CSV File**: Lists all saved identities.
6. **Generate Custom Number of Identities and Save to CSV**: Generate multiple identities and save them.
7. **Search Identity by Name in CSV File**: Search for a specific identity by name.
8. **Exit**: Exits the program.

## CSV Storage

All identities generated with the "Save" option are stored in a CSV file named `fake_identities.csv`. You can open this file with any text editor or spreadsheet software to view or modify the generated data.

## Example

Here is an example of what the generated identity might look like:

```
================ Generated Identity ===============
First Name: John
Last Name: Doe
Address: 123 Main Street, Springfield, Illinois
Username: johndoe123
Password: !P@ssword2024
Date of Birth: 15/6/1990
Gender: Male
SSN: 123-45-6789
Car Number: XYZ 1234
Relatives: Jane Doe, Alice Doe
Phone Number: (123) 456-7890
Email: johndoe@example.com
===================================================
```

## License

This project is licensed under the MIT License.

## Disclaimer

FakerSmith is intended for educational, testing, and research purposes only. Please do not use the generated identities for any unlawful activities.

## Contribution

Feel free to contribute to FakerSmith! If you have suggestions or improvements, please submit a pull request or open an issue on the repository.
