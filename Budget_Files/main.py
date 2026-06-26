import os
import shutil
import unittest
import sys
from python_scripts_automation import monthly_budget_folders
from python_scripts_automation.Constants import Constants

def run_tests():
    print("Running tests...")
    loader = unittest.TestLoader()
    suite = loader.discover('tests')
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)
    if not result.wasSuccessful():
        print("Tests failed. Exiting.")
        sys.exit(1)
    print("Tests passed.\n")

# Run tests
run_tests()

# Ask for years
years_input = input(f"{Constants.ENTER} {Constants.THE} {Constants.YEARS} {Constants.YOU} {Constants.WANT} {Constants.TO} {Constants.GENERATE} {Constants.FOLDERS} {Constants.FOR} ({Constants.SEPARATED} {Constants.BY} {Constants.COMMA}, {Constants.EG} {Constants.TWENTY_TWENTY_FIVE}{Constants.COMMA} {Constants.TWENTY_TWENTY_SIX}): ")
years = [y.strip() for y in years_input.split(",")]

root_records_folder = Constants.RECORDS
if not os.path.exists(root_records_folder):
    os.makedirs(root_records_folder)

for year in years:
    main_folder = os.path.join(root_records_folder, f"{Constants.RECORDS} {year}")

    # Check if the directory exists
    if os.path.exists(main_folder):
        # Remove the directory
        shutil.rmtree(main_folder)

    receipts_folders = monthly_budget_folders.generate_monthly_budget_folders(year)
    os.makedirs(main_folder)

    shutil.move(receipts_folders, main_folder)


