import logging
from python_scripts_automation.Constants import Constants
from python_scripts_automation.file_system_manager import FileSystemManager
from python_scripts_automation.budget_folder_manager import BudgetFolderManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def generate_monthly_budget_folders(year):
    months = [Constants.JANUARY, Constants.FEBRUARY, Constants.MARCH, Constants.APRIL, Constants.MAY, Constants.JUNE, Constants.JULY, Constants.AUGUST, Constants.SEPTEMBER, Constants.OCTOBER,
              Constants.NOVEMBER, Constants.DECEMBER]

    manager = BudgetFolderManager(year)
    dest_folder = f"{Constants.RECEIPTS} {year}"
    logger.info(f"{Constants.CREATING} {Constants.RECEIPTS} {year} {Constants.FOLDER}")
    FileSystemManager.ensure_directory_exists(dest_folder)

    for i, month in enumerate(months, start=1):
        abbreviated_month = month[:3]

        # Format the index as a two-digit number
        folder_number = str(i).zfill(2)

        # Creating Monthly Receipts Folder
        monthReceiptsFolder = f"{folder_number}_{Constants.RECEIPTS} {month} {year}"
        logger.info(f"{Constants.MONTH} {Constants.RECEIPT} {Constants.FOLDER} {Constants.NAME}: {monthReceiptsFolder}")
        FileSystemManager.ensure_directory_exists(monthReceiptsFolder)

        # Creating Market Receipts Folder
        marketReceiptsFolder = f"{Constants.MARKET} {Constants.RECEIPTS} {month} {year}"
        FileSystemManager.ensure_directory_exists(marketReceiptsFolder)

        # Creating Gym Receipts Folder
        gymReceiptsFolder = f"{Constants.GYM} {Constants.RECEIPTS} {month} {year}"
        FileSystemManager.ensure_directory_exists(gymReceiptsFolder)

        # Creating Account Receipts Folder
        accountReceiptsFolder = f"{Constants.ACCOUNT} {Constants.RECEIPTS} {month} {year}"
        FileSystemManager.ensure_directory_exists(accountReceiptsFolder)

        # Creating All Banks Folder
        alliedBankReceiptsFolder = manager.create_bank_receipts_folder(Constants.ALLIED_BANK, month)
        bankAlfalahReceiptsFolder = manager.create_bank_receipts_folder(Constants.BANK_ALFALAH, month)
        easyPaissaReceiptsFolder = manager.create_bank_receipts_folder(Constants.EASY_PAISSA, month)
        firstPayReceiptsFolder = manager.create_bank_receipts_folder(Constants.HBL_MICROFINANCE, month)
        jazzCashReceiptsFolder = manager.create_bank_receipts_folder(Constants.JAZZ_CASH, month)
        mashreqReceiptsFolder = manager.create_bank_receipts_folder(Constants.MASHREQ_BANK, month)
        meezanBankReceiptsFolder = manager.create_bank_receipts_folder(Constants.MEEZAN_BANK, month)
        nayaPayReceiptsFolder = manager.create_bank_receipts_folder(Constants.NAYA_PAY, month)
        sadaPayReceiptsFolder = manager.create_bank_receipts_folder(Constants.SADA_PAY, month)
        standardCharteredBankReceiptsFolder = manager.create_bank_receipts_folder(Constants.STANDARD_CHARTERED_BANK, month)
        uPaisaReceiptsFolder = manager.create_bank_receipts_folder(Constants.U_PAISA, month)
        zindgiReceiptsFolder = manager.create_bank_receipts_folder(Constants.ZINDIGI, month)
        raqamiReceiptsFolder = manager.create_bank_receipts_folder(Constants.RAQAMI, month)
        aikReceiptsFolder = manager.create_bank_receipts_folder(Constants.AIK, month)
        ublReceiptsFolder = manager.create_bank_receipts_folder(Constants.UNITED_BANK_LIMITED, month)
        tradingReceiptsFolder = manager.create_bank_receipts_folder(Constants.TRADING, month)

        # Setup Bank Folders
        logger.info(f"{Constants.STERIC} {Constants.ALLIED_BANK} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.ALLIED_BANK_ABBREVIATION, alliedBankReceiptsFolder, abbreviated_month)
        logger.info(f"{Constants.STERIC} {Constants.BANK_ALFALAH} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.BANK_ALFALAH_ABBREVIATION, bankAlfalahReceiptsFolder, abbreviated_month, has_orbit=True)
        logger.info(f"{Constants.STERIC} {Constants.EASY_PAISSA} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.EASY_PAISSA_ABBREVIATION, easyPaissaReceiptsFolder, abbreviated_month)
        logger.info(f"{Constants.STERIC} {Constants.HBL_MICROFINANCE} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.HBL_MICROFINANCE_ABBREVIATION, firstPayReceiptsFolder, abbreviated_month)
        logger.info(f"{Constants.STERIC} {Constants.JAZZ_CASH} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.JAZZ_CASH_ABBREVIATION, jazzCashReceiptsFolder, abbreviated_month)
        logger.info(f"{Constants.STERIC} {Constants.MASHREQ_BANK} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.MASHREQ_BANK_ABBREVIATION, mashreqReceiptsFolder, abbreviated_month)
        logger.info(f"{Constants.STERIC} {Constants.MEEZAN_BANK} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.MEEZAN_BANK_ABBREVIATION, meezanBankReceiptsFolder, abbreviated_month)
        logger.info(f"{Constants.STERIC} {Constants.NAYA_PAY} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.NAYA_PAY_ABBREVIATION, nayaPayReceiptsFolder, abbreviated_month)
        logger.info(f"{Constants.STERIC} {Constants.SADA_PAY} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.SADA_PAY_ABBREVIATION, sadaPayReceiptsFolder, abbreviated_month)
        logger.info(f"{Constants.STERIC} {Constants.STANDARD_CHARTERED_BANK} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.STANDARD_CHARTERED_BANK_ABBREVIATION, standardCharteredBankReceiptsFolder, abbreviated_month)
        logger.info(f"{Constants.STERIC} {Constants.U_PAISA} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.U_PAISA_ABBREVIATION, uPaisaReceiptsFolder, abbreviated_month)
        logger.info(f"{Constants.STERIC} {Constants.ZINDIGI} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.ZINDIGI_ABBREVIATION, zindgiReceiptsFolder, abbreviated_month)
        logger.info(f"{Constants.STERIC} {Constants.RAQAMI} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.RAQAMI_ABBREVIATION, raqamiReceiptsFolder, abbreviated_month)
        logger.info(f"{Constants.STERIC} {Constants.AIK} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.AIK_ABBREVIATION, aikReceiptsFolder, abbreviated_month)
        logger.info(f"{Constants.STERIC} {Constants.UNITED_BANK_LIMITED} {Constants.STERIC}")
        manager.setup_bank_folders(Constants.UNITED_BANK_LIMITED_ABBREVIATION, ublReceiptsFolder, abbreviated_month)

        # Creating Trading Receipt Folder
        logger.info(f"{Constants.STERIC} {Constants.TRADING} {Constants.STERIC}")
        cDCReceiptFolder = BudgetFolderManager.create_named_subfolder(f"{Constants.CDC} {Constants.RECEIPT}", abbreviated_month, year)
        cGTReceiptFolder = BudgetFolderManager.create_named_subfolder(f"{Constants.CGT} {Constants.RECEIPT}", abbreviated_month, year)
        kTradeReceiptFolder = BudgetFolderManager.create_named_subfolder(f"{Constants.KTRADE} {Constants.RECEIPT}", abbreviated_month, year)

        # Creating KTrade Receipt Folder
        kTradeDividendStatementFolder = BudgetFolderManager.create_named_subfolder(f"{Constants.KTRADE} {Constants.DIVIDEND} {Constants.STATEMENT}", abbreviated_month, year)
        kTradeEStatementFolder = BudgetFolderManager.create_named_subfolder(f"{Constants.KTRADE} {Constants.E_STATEMENT}", abbreviated_month, year)
        kTradeTradeConfirmationFolder = BudgetFolderManager.create_named_subfolder(f"{Constants.KTRADE} {Constants.TRADE} {Constants.CONFIRMATION}", abbreviated_month, year)

        # Moving kTrade Dividend Statement & kTrade E Statement & KTrade Trade Confirmation into kTrade Receipts Folder
        FileSystemManager.move_folder_if_exists(kTradeDividendStatementFolder, kTradeReceiptFolder)
        FileSystemManager.move_folder_if_exists(kTradeEStatementFolder, kTradeReceiptFolder)
        FileSystemManager.move_folder_if_exists(kTradeTradeConfirmationFolder, kTradeReceiptFolder)

        # Moving kTrade Receipts & CGT Receipts & CDC Receipts into Trading Receipts Folder
        FileSystemManager.move_folder_if_exists(kTradeReceiptFolder, tradingReceiptsFolder)
        FileSystemManager.move_folder_if_exists(cGTReceiptFolder, tradingReceiptsFolder)
        FileSystemManager.move_folder_if_exists(cDCReceiptFolder, tradingReceiptsFolder)

        # Moving All Bank Folders into Account Receipts Folder
        logger.info(f"{Constants.STERIC} {Constants.MOVE} {Constants.ALL} {Constants.BANK} {Constants.FOLDERS} {Constants.INTO} {Constants.ACCOUNT} {Constants.RECEIPTS} {Constants.FOLDER} {Constants.STERIC}")
        FileSystemManager.move_folder_if_exists(alliedBankReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(bankAlfalahReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(easyPaissaReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(firstPayReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(jazzCashReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(mashreqReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(meezanBankReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(nayaPayReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(sadaPayReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(standardCharteredBankReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(uPaisaReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(zindgiReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(raqamiReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(aikReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(ublReceiptsFolder, accountReceiptsFolder)
        FileSystemManager.move_folder_if_exists(tradingReceiptsFolder, accountReceiptsFolder)

        # Moving Gym Receipts Folder into Market Receipts Folder
        FileSystemManager.move_folder_if_exists(gymReceiptsFolder, marketReceiptsFolder)

        FileSystemManager.move_folder_if_exists(accountReceiptsFolder, monthReceiptsFolder, log_message=f"{Constants.MOVE} {Constants.ACCOUNT} {Constants.RECEIPTS} {Constants.FOLDER} {Constants.IN} {Constants.MONTH} {Constants.RECEIPTS} {Constants.FOLDER}")

        FileSystemManager.move_folder_if_exists(marketReceiptsFolder, monthReceiptsFolder, log_message=f"{Constants.MOVE} {Constants.MARKET} {Constants.RECEIPTS} {Constants.FOLDER} {Constants.IN} {Constants.MONTH} {Constants.RECEIPTS} {Constants.FOLDER}")

        FileSystemManager.move_folder_if_exists(monthReceiptsFolder, dest_folder, log_message=f"{Constants.MOVE} {Constants.MONTH} {Constants.RECEIPTS} {Constants.FOLDER} {Constants.IN} {Constants.RECEIPTS} {Constants.FOLDER}\n")

    return dest_folder

