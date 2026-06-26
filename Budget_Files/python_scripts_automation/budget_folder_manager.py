import logging
from python_scripts_automation.Constants import Constants
from python_scripts_automation.file_system_manager import FileSystemManager

logger = logging.getLogger(__name__)

class BudgetFolderManager:
    def __init__(self, year):
        self.year = year
        logger.info(f"{Constants.INITIALIZED} {Constants.BUDGET} {Constants.FOLDER} {Constants.MANAGER} {Constants.FOR} {Constants.YEAR}: {self.year}\n")

    @staticmethod
    def create_named_subfolder(full_name, abbreviated_month, year):
        folder_path = f"{full_name} {abbreviated_month} {year}"
        FileSystemManager.ensure_directory_exists(folder_path)
        logger.info(f"{Constants.CREATING} {Constants.NAME} {Constants.FOLDER}: {folder_path}")
        return folder_path

    def create_bank_receipts_folder(self, bank_name, month):
        folder_path = f"{bank_name} {Constants.RECEIPTS} {month} {self.year}"
        FileSystemManager.ensure_directory_exists(folder_path)
        logger.info(f"{Constants.CREATING} {Constants.RECEIPTS} {Constants.FOLDER}: {folder_path}")
        return folder_path

    def setup_bank_folders(self, abbreviation, bank_receipts_folder, abbreviated_month, has_orbit=False):
        logger.info(f"{Constants.SETTING} {Constants.UP} {Constants.BANK} {Constants.FOLDERS} {Constants.FOR}: {abbreviation}")
        # Create subfolders
        credit_receipts_folder = self.create_named_subfolder(f"{abbreviation} {Constants.CREDIT} {Constants.RECEIPT}", abbreviated_month, self.year)
        debit_receipts_folder = self.create_named_subfolder(f"{abbreviation} {Constants.DEBIT} {Constants.RECEIPT}", abbreviated_month, self.year)
        
        # Transactions
        credit_app_trans = self.create_named_subfolder(f"{abbreviation} {Constants.CREDIT} {Constants.APP} {Constants.TRANSACTION}", abbreviated_month, self.year)
        credit_card_trans = self.create_named_subfolder(f"{abbreviation} {Constants.CREDIT} {Constants.CARD} {Constants.TRANSACTION}", abbreviated_month, self.year)
        credit_cash_trans = self.create_named_subfolder(f"{abbreviation} {Constants.CREDIT} {Constants.CASH} {Constants.TRANSACTION}", abbreviated_month, self.year)
        
        debit_app_trans = self.create_named_subfolder(f"{abbreviation} {Constants.DEBIT} {Constants.APP} {Constants.TRANSACTION}", abbreviated_month, self.year)
        debit_card_trans = self.create_named_subfolder(f"{abbreviation} {Constants.DEBIT} {Constants.CARD} {Constants.TRANSACTION}", abbreviated_month, self.year)
        debit_cash_trans = self.create_named_subfolder(f"{abbreviation} {Constants.DEBIT} {Constants.CASH} {Constants.TRANSACTION}", abbreviated_month, self.year)
        
        # E-Statements
        credit_card_estmt = self.create_named_subfolder(f"{abbreviation} {Constants.CREDIT} {Constants.CARD} {Constants.E_STATEMENT}", abbreviated_month, self.year)
        debit_card_estmt = self.create_named_subfolder(f"{abbreviation} {Constants.DEBIT} {Constants.CARD} {Constants.E_STATEMENT}", abbreviated_month, self.year)
        
        # Orbit
        orbit_stmt = None
        if has_orbit:
            orbit_stmt = self.create_named_subfolder(f"{abbreviation} {Constants.ORBIT} {Constants.STATEMENT}", abbreviated_month, self.year)
        
        # Move Transactions
        FileSystemManager.move_folder_if_exists(credit_app_trans, credit_receipts_folder)
        FileSystemManager.move_folder_if_exists(credit_card_trans, credit_receipts_folder)
        FileSystemManager.move_folder_if_exists(credit_cash_trans, credit_receipts_folder)
        
        FileSystemManager.move_folder_if_exists(debit_app_trans, debit_receipts_folder)
        FileSystemManager.move_folder_if_exists(debit_card_trans, debit_receipts_folder)
        FileSystemManager.move_folder_if_exists(debit_cash_trans, debit_receipts_folder)
        
        # Move to bank folder
        FileSystemManager.move_folder_if_exists(credit_card_estmt, bank_receipts_folder)
        FileSystemManager.move_folder_if_exists(credit_receipts_folder, bank_receipts_folder)
        FileSystemManager.move_folder_if_exists(debit_card_estmt, bank_receipts_folder)
        FileSystemManager.move_folder_if_exists(debit_receipts_folder, bank_receipts_folder)
        
        if has_orbit and orbit_stmt:
            FileSystemManager.move_folder_if_exists(orbit_stmt, bank_receipts_folder)
        logger.info(f"{Constants.SEPARATOR} {Constants.FINISHED} {Constants.SETTING} {Constants.UP} {Constants.BANK} {Constants.FOLDERS} {Constants.FOR}: {abbreviation} {Constants.SEPARATOR}\n\n")
