import os
import shutil
from constants.Constants import Constants


def ensure_directory_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def create_bank_receipts_folder(bank_name, month, year):
    folder_path = f"{bank_name} {Constants.RECEIPTS} {month} {year}"
    ensure_directory_exists(folder_path)
    return folder_path


def create_named_subfolder(full_name, abbreviated_month, year):
    folder_path = f"{full_name} {abbreviated_month} {year}"
    ensure_directory_exists(folder_path)
    return folder_path


def move_folder_if_exists(source, destination):
    if os.path.exists(source):
        shutil.move(source, destination)


def setup_bank_folders(abbreviation, bank_receipts_folder, abbreviated_month, year, has_orbit=False):
    # Create subfolders
    credit_receipts_folder = create_named_subfolder(f"{abbreviation} {Constants.CREDIT} {Constants.RECEIPT}", abbreviated_month, year)
    debit_receipts_folder = create_named_subfolder(f"{abbreviation} {Constants.DEBIT} {Constants.RECEIPT}", abbreviated_month, year)
    
    # Transactions
    credit_app_trans = create_named_subfolder(f"{abbreviation} {Constants.CREDIT} {Constants.APP} {Constants.TRANSACTION}", abbreviated_month, year)
    credit_card_trans = create_named_subfolder(f"{abbreviation} {Constants.CREDIT} {Constants.CARD} {Constants.TRANSACTION}", abbreviated_month, year)
    credit_cash_trans = create_named_subfolder(f"{abbreviation} {Constants.CREDIT} {Constants.CASH} {Constants.TRANSACTION}", abbreviated_month, year)
    
    debit_app_trans = create_named_subfolder(f"{abbreviation} {Constants.DEBIT} {Constants.APP} {Constants.TRANSACTION}", abbreviated_month, year)
    debit_card_trans = create_named_subfolder(f"{abbreviation} {Constants.DEBIT} {Constants.CARD} {Constants.TRANSACTION}", abbreviated_month, year)
    debit_cash_trans = create_named_subfolder(f"{abbreviation} {Constants.DEBIT} {Constants.CASH} {Constants.TRANSACTION}", abbreviated_month, year)
    
    # E-Statements
    credit_card_estmt = create_named_subfolder(f"{abbreviation} {Constants.CREDIT} {Constants.CARD} {Constants.E_STATEMENT}", abbreviated_month, year)
    debit_card_estmt = create_named_subfolder(f"{abbreviation} {Constants.DEBIT} {Constants.CARD} {Constants.E_STATEMENT}", abbreviated_month, year)
    
    # Orbit
    orbit_stmt = None
    if has_orbit:
        orbit_stmt = create_named_subfolder(f"{abbreviation} {Constants.ORBIT} {Constants.STATEMENT}", abbreviated_month, year)
    
    # Move Transactions
    move_folder_if_exists(credit_app_trans, credit_receipts_folder)
    move_folder_if_exists(credit_card_trans, credit_receipts_folder)
    move_folder_if_exists(credit_cash_trans, credit_receipts_folder)
    
    move_folder_if_exists(debit_app_trans, debit_receipts_folder)
    move_folder_if_exists(debit_card_trans, debit_receipts_folder)
    move_folder_if_exists(debit_cash_trans, debit_receipts_folder)
    
    # Move to bank folder
    move_folder_if_exists(credit_card_estmt, bank_receipts_folder)
    move_folder_if_exists(credit_receipts_folder, bank_receipts_folder)
    move_folder_if_exists(debit_card_estmt, bank_receipts_folder)
    move_folder_if_exists(debit_receipts_folder, bank_receipts_folder)
    
    if has_orbit and orbit_stmt:
        move_folder_if_exists(orbit_stmt, bank_receipts_folder)


def generate_monthly_budget_folders(year):
    months = [Constants.JANUARY, Constants.FEBRUARY, Constants.MARCH, Constants.APRIL, Constants.MAY, Constants.JUNE, Constants.JULY, Constants.AUGUST, Constants.SEPTEMBER, Constants.OCTOBER,
              Constants.NOVEMBER, Constants.DECEMBER]

    dest_folder = f"{Constants.RECEIPTS} {year}"
    print(f"\n{Constants.CREATING} {Constants.RECEIPTS} {year} {Constants.FOLDER}")
    ensure_directory_exists(dest_folder)

    for i, month in enumerate(months, start=1):
        abbreviated_month = month[:3]

        # Format the index as a two-digit number
        folder_number = str(i).zfill(2)

        # Creating Monthly Receipts Folder
        monthReceiptsFolder = f"{folder_number}_{Constants.RECEIPTS} {month} {year}"
        print(f"\n\n{Constants.MONTH} {Constants.RECEIPT} {Constants.FOLDER} {Constants.NAME}:", monthReceiptsFolder)
        ensure_directory_exists(monthReceiptsFolder)

        # Creating Market Receipts Folder
        marketReceiptsFolder = f"{Constants.MARKET} {Constants.RECEIPTS} {month} {year}"
        ensure_directory_exists(marketReceiptsFolder)

        # Creating Gym Receipts Folder
        gymReceiptsFolder = f"{Constants.GYM} {Constants.RECEIPTS} {month} {year}"
        ensure_directory_exists(gymReceiptsFolder)

        # Creating Account Receipts Folder
        accountReceiptsFolder = f"{Constants.ACCOUNT} {Constants.RECEIPTS} {month} {year}"
        ensure_directory_exists(accountReceiptsFolder)

        # Creating All Banks Folder
        alliedBankReceiptsFolder = create_bank_receipts_folder(Constants.ALLIED_BANK, month, year)
        bankAlfalahReceiptsFolder = create_bank_receipts_folder(Constants.BANK_ALFALAH, month, year)
        easyPaissaReceiptsFolder = create_bank_receipts_folder(Constants.EASY_PAISSA, month, year)
        firstPayReceiptsFolder = create_bank_receipts_folder(Constants.FIRST_PAY, month, year)
        jazzCashReceiptsFolder = create_bank_receipts_folder(Constants.JAZZ_CASH, month, year)
        mashreqReceiptsFolder = create_bank_receipts_folder(Constants.MASHREQ_BANK, month, year)
        meezanBankReceiptsFolder = create_bank_receipts_folder(Constants.MEEZAN_BANK, month, year)
        nayaPayReceiptsFolder = create_bank_receipts_folder(Constants.NAYA_PAY, month, year)
        sadaPayReceiptsFolder = create_bank_receipts_folder(Constants.SADA_PAY, month, year)
        standardCharteredBankReceiptsFolder = create_bank_receipts_folder(Constants.STANDARD_CHARTERED_BANK, month,
                                                                          year)
        uPaisaReceiptsFolder = create_bank_receipts_folder(Constants.U_PAISA, month, year)
        zindgiReceiptsFolder = create_bank_receipts_folder(Constants.ZINDIGI, month, year)
        raqamiReceiptsFolder = create_bank_receipts_folder(Constants.RAQAMI, month, year)
        tradingReceiptsFolder = create_bank_receipts_folder(Constants.TRADING, month, year)

        # Setup Bank Folders
        setup_bank_folders(Constants.ALLIED_BANK_ABBREVIATION, alliedBankReceiptsFolder, abbreviated_month, year)
        setup_bank_folders(Constants.BANK_ALFALAH_ABBREVIATION, bankAlfalahReceiptsFolder, abbreviated_month, year, has_orbit=True)
        setup_bank_folders(Constants.EASY_PAISSA_ABBREVIATION, easyPaissaReceiptsFolder, abbreviated_month, year)
        setup_bank_folders(Constants.FIRST_PAY_ABBREVIATION, firstPayReceiptsFolder, abbreviated_month, year)
        setup_bank_folders(Constants.JAZZ_CASH_ABBREVIATION, jazzCashReceiptsFolder, abbreviated_month, year)
        setup_bank_folders(Constants.MASHREQ_BANK_ABBREVIATION, mashreqReceiptsFolder, abbreviated_month, year)
        setup_bank_folders(Constants.MEEZAN_BANK_ABBREVIATION, meezanBankReceiptsFolder, abbreviated_month, year)
        setup_bank_folders(Constants.NAYA_PAY_ABBREVIATION, nayaPayReceiptsFolder, abbreviated_month, year)
        setup_bank_folders(Constants.SADA_PAY_ABBREVIATION, sadaPayReceiptsFolder, abbreviated_month, year)
        setup_bank_folders(Constants.STANDARD_CHARTERED_BANK_ABBREVIATION, standardCharteredBankReceiptsFolder, abbreviated_month, year)
        setup_bank_folders(Constants.U_PAISA_ABBREVIATION, uPaisaReceiptsFolder, abbreviated_month, year)
        setup_bank_folders(Constants.ZINDIGI_ABBREVIATION, zindgiReceiptsFolder, abbreviated_month, year)
        setup_bank_folders(Constants.RAQAMI_ABBREVIATION, raqamiReceiptsFolder, abbreviated_month, year)


        # Creating Trading Receipt Folder
        cDCReceiptFolder = create_named_subfolder(f"{Constants.CDC} {Constants.RECEIPT}", abbreviated_month, year)
        cGTReceiptFolder = create_named_subfolder(f"{Constants.CGT} {Constants.RECEIPT}", abbreviated_month, year)
        kTradeReceiptFolder = create_named_subfolder(f"{Constants.KTRADE} {Constants.RECEIPT}", abbreviated_month, year)

        # Creating KTrade Receipt Folder
        kTradeDividendStatementFolder = create_named_subfolder(f"{Constants.KTRADE} {Constants.DIVIDEND} {Constants.STATEMENT}", abbreviated_month, year)
        kTradeEStatementFolder = create_named_subfolder(f"{Constants.KTRADE} {Constants.E_STATEMENT}", abbreviated_month, year)
        kTradeTradeConfirmationFolder = create_named_subfolder(f"{Constants.KTRADE} {Constants.TRADE} {Constants.CONFIRMATION}", abbreviated_month, year)









        # Moving kTrade Dividend Statement & kTrade E Statement & KTrade Trade Confirmation into kTrade Receipts Folder
        move_folder_if_exists(kTradeDividendStatementFolder, kTradeReceiptFolder)
        move_folder_if_exists(kTradeEStatementFolder, kTradeReceiptFolder)
        move_folder_if_exists(kTradeTradeConfirmationFolder, kTradeReceiptFolder)

        # Moving kTrade Receipts & CGT Receipts & CDC Receipts into Trading Receipts Folder
        move_folder_if_exists(kTradeReceiptFolder, tradingReceiptsFolder)
        move_folder_if_exists(cGTReceiptFolder, tradingReceiptsFolder)
        move_folder_if_exists(cDCReceiptFolder, tradingReceiptsFolder)


        # Moving All Bank Folders into Account Receipts Folder
        move_folder_if_exists(alliedBankReceiptsFolder, accountReceiptsFolder)
        move_folder_if_exists(bankAlfalahReceiptsFolder, accountReceiptsFolder)
        move_folder_if_exists(easyPaissaReceiptsFolder, accountReceiptsFolder)
        move_folder_if_exists(firstPayReceiptsFolder, accountReceiptsFolder)
        move_folder_if_exists(jazzCashReceiptsFolder, accountReceiptsFolder)
        move_folder_if_exists(mashreqReceiptsFolder, accountReceiptsFolder)
        move_folder_if_exists(meezanBankReceiptsFolder, accountReceiptsFolder)
        move_folder_if_exists(nayaPayReceiptsFolder, accountReceiptsFolder)
        move_folder_if_exists(sadaPayReceiptsFolder, accountReceiptsFolder)
        move_folder_if_exists(standardCharteredBankReceiptsFolder, accountReceiptsFolder)
        move_folder_if_exists(uPaisaReceiptsFolder, accountReceiptsFolder)
        move_folder_if_exists(zindgiReceiptsFolder, accountReceiptsFolder)
        move_folder_if_exists(raqamiReceiptsFolder, accountReceiptsFolder)
        move_folder_if_exists(tradingReceiptsFolder, accountReceiptsFolder)

        # Moving Gym Receipts Folder into Market Receipts Folder
        move_folder_if_exists(gymReceiptsFolder, marketReceiptsFolder)

        print(
            f"{Constants.MOVE} {accountReceiptsFolder} {Constants.FOLDER} {Constants.IN} {monthReceiptsFolder} {Constants.FOLDER}")
        move_folder_if_exists(accountReceiptsFolder, monthReceiptsFolder)

        print(
                f"{Constants.MOVE} {marketReceiptsFolder} {Constants.FOLDER} {Constants.IN} {monthReceiptsFolder} {Constants.FOLDER}")
        move_folder_if_exists(marketReceiptsFolder, monthReceiptsFolder)

        print(
            f"{Constants.MOVE} {monthReceiptsFolder} {Constants.FOLDER} {Constants.IN} {dest_folder} {Constants.FOLDER}\n")
        move_folder_if_exists(monthReceiptsFolder, dest_folder)

    return dest_folder
