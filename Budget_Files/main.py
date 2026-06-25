import os
import shutil
from python_scripts_automation import monthly_budget_folders

year = 2026
main_folder = f"Records {year}"

# Check if the directory exists
if os.path.exists(main_folder):
    # Remove the directory
    shutil.rmtree(main_folder)

receipts_folders = monthly_budget_folders.generate_monthly_budget_folders(year)
os.makedirs(main_folder)

shutil.move(receipts_folders, main_folder)


