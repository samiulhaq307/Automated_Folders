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
        print(f"\n\n{Constants.MONTH} {Constants.RECEIPT} {Constants.FOLDER} {Constants.NAME}:", monthReceiptsFolder)
        monthReceiptsFolder = f"{folder_number}_{Constants.RECEIPTS} {month} {year}"
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
        tradingReceiptsFolder = create_bank_receipts_folder(Constants.TRADING, month, year)

        # Creating Allied Bank Receipt Folders
        aBCreditCardEStatementFolder = create_named_subfolder("AB Credit Card E Statement", abbreviated_month, year)
        aBCreditReceiptFolder = create_named_subfolder("AB Credit Receipt", abbreviated_month, year)
        aBDebitCardEStatementFolder = create_named_subfolder("AB Debit Card E Statement", abbreviated_month, year)
        aBDebitReceiptFolder = create_named_subfolder("AB Debit Receipt", abbreviated_month, year)

        # Creating Allied Bank Credit Receipts Folder
        aBCreditAppTransactionFolder = create_named_subfolder("AB Credit App Transaction", abbreviated_month, year)
        aBCreditCardTransactionFolder = create_named_subfolder("AB Credit Card Transaction", abbreviated_month, year)
        aBCreditCashTransactionFolder = create_named_subfolder("AB Credit Cash Transaction", abbreviated_month, year)

        # Creating Allied Bank Debit Receipts Folder
        aBDebitAppTransactionFolder = create_named_subfolder("AB Debit App Transaction", abbreviated_month, year)
        aBDebitCardTransactionFolder = create_named_subfolder("AB Debit Card Transaction", abbreviated_month, year)
        aBDebitCashTransactionFolder = create_named_subfolder("AB Debit Cash Transaction", abbreviated_month, year)


        # Creating Bank Alfalah Receipt Folders
        bACreditCardEStatementFolder = create_named_subfolder("BA Credit Card E Statement", abbreviated_month, year)
        bACreditReceiptFolder = create_named_subfolder("BA Credit Receipt", abbreviated_month, year)
        bADebitCardEStatementFolder = create_named_subfolder("BA Debit Card E Statement", abbreviated_month, year)
        bADebitReceiptFolder = create_named_subfolder("BA Debit Receipt", abbreviated_month, year)
        bAOrbitStatementFolder = create_named_subfolder("BA Orbit Statement", abbreviated_month, year)

        # Creating Bank Alfalah Credit Receipts Folder
        bACreditAppTransactionFolder = create_named_subfolder("BA Credit App Transaction", abbreviated_month, year)
        bACreditCardTransactionFolder = create_named_subfolder("BA Credit Card Transaction", abbreviated_month, year)
        bACreditCashTransactionFolder = create_named_subfolder("BA Credit Cash Transaction", abbreviated_month, year)

        # Creating Bank Alfalah Debit Receipts Folder
        bADebitAppTransactionFolder = create_named_subfolder("BA Debit App Transaction", abbreviated_month, year)
        bADebitCardTransactionFolder = create_named_subfolder("BA Debit Card Transaction", abbreviated_month, year)
        bADebitCashTransactionFolder = create_named_subfolder("BA Debit Cash Transaction", abbreviated_month, year)


        # Creating EasyPaissa Receipt Folder
        ePCreditReceiptFolder = create_named_subfolder("EP Credit Receipt", abbreviated_month, year)
        ePDebitReceiptFolder = create_named_subfolder("EP Debit Receipt", abbreviated_month, year)

        # Creating EasyPaissa Credit Receipts Folder
        ePCreditAppTransactionFolder = create_named_subfolder("EP Credit App Transaction", abbreviated_month, year)
        ePCreditCardTransactionFolder = create_named_subfolder("EP Credit Card Transaction", abbreviated_month, year)
        ePCreditCashTransactionFolder = create_named_subfolder("EP Credit Cash Transaction", abbreviated_month, year)

        # Creating EasyPaissa Debit Receipts Folder
        ePDebitAppTransactionFolder = create_named_subfolder("EP Debit App Transaction", abbreviated_month, year)
        ePDebitCardTransactionFolder = create_named_subfolder("EP Debit Card Transaction", abbreviated_month, year)
        ePDebitCashTransactionFolder = create_named_subfolder("EP Debit Cash Transaction", abbreviated_month, year)


        # Creating FirstPay Receipt Folder
        fPCreditReceiptFolder = create_named_subfolder("FP Credit Receipt", abbreviated_month, year)
        fPDebitReceiptFolder = create_named_subfolder("FP Debit Receipt", abbreviated_month, year)

        # Creating FirstPay Credit Receipts Folder
        fPCreditAppTransactionFolder = create_named_subfolder("FP Credit App Transaction", abbreviated_month, year)
        fPCreditCardTransactionFolder = create_named_subfolder("FP Credit Card Transaction", abbreviated_month, year)
        fPCreditCashTransactionFolder = create_named_subfolder("FP Credit Cash Transaction", abbreviated_month, year)

        # Creating FirstPay Debit Receipts Folder
        fPDebitAppTransactionFolder = create_named_subfolder("FP Debit App Transaction", abbreviated_month, year)
        fPDebitCardTransactionFolder = create_named_subfolder("FP Debit Card Transaction", abbreviated_month, year)
        fPDebitCashTransactionFolder = create_named_subfolder("FP Debit Cash Transaction", abbreviated_month, year)


        # Creating JazzCash Receipt Folder
        jCCreditReceiptFolder = create_named_subfolder("JC Credit Receipt", abbreviated_month, year)
        jCDebitReceiptFolder = create_named_subfolder("JC Debit Receipt", abbreviated_month, year)

        # Creating JazzCash Credit Receipts Folder
        jCCreditAppTransactionFolder = create_named_subfolder("JC Credit App Transaction", abbreviated_month, year)
        jCCreditCardTransactionFolder = create_named_subfolder("JC Credit Card Transaction", abbreviated_month, year)
        jCCreditCashTransactionFolder = create_named_subfolder("JC Credit Cash Transaction", abbreviated_month, year)

        # Creating JazzCash Debit Receipts Folder
        jCDebitAppTransactionFolder = create_named_subfolder("JC Debit App Transaction", abbreviated_month, year)
        jCDebitCardTransactionFolder = create_named_subfolder("JC Debit Card Transaction", abbreviated_month, year)
        jCDebitCashTransactionFolder = create_named_subfolder("JC Debit Cash Transaction", abbreviated_month, year)


        # Creating Mashreq Receipt Folder
        mQCreditReceiptFolder = create_named_subfolder("MQ Credit Receipt", abbreviated_month, year)
        mQDebitReceiptFolder = create_named_subfolder("MQ Debit Receipt", abbreviated_month, year)

        # Creating Mashreq Credit Receipts Folder
        mQCreditAppTransactionFolder = create_named_subfolder("MQ Credit App Transaction", abbreviated_month, year)
        mQCreditCardTransactionFolder = create_named_subfolder("MQ Credit Card Transaction", abbreviated_month, year)
        mQCreditCashTransactionFolder = create_named_subfolder("MQ Credit Cash Transaction", abbreviated_month, year)

        # Creating Mashreq Debit Receipts Folder
        mQDebitAppTransactionFolder = create_named_subfolder("MQ Debit App Transaction", abbreviated_month, year)
        mQDebitCardTransactionFolder = create_named_subfolder("MQ Debit Card Transaction", abbreviated_month, year)
        mQDebitCashTransactionFolder = create_named_subfolder("MQ Debit Cash Transaction", abbreviated_month, year)


        # Creating Meezan Bank Receipt Folder
        mBCreditCardEStatementFolder = create_named_subfolder("MB Credit Card E Statement", abbreviated_month, year)
        mBCreditReceiptFolder = create_named_subfolder("MB Credit Receipt", abbreviated_month, year)
        mBDebitCardEStatementFolder = create_named_subfolder("MB Debit Card E Statement", abbreviated_month, year)
        mBDebitReceiptFolder = create_named_subfolder("MB Debit Receipt", abbreviated_month, year)

        # Creating Meezan Bank Credit Receipts Folder
        mBCreditAppTransactionFolder = create_named_subfolder("MB Credit App Transaction", abbreviated_month, year)
        mBCreditCardTransactionFolder = create_named_subfolder("MB Credit Card Transaction", abbreviated_month, year)
        mBCreditCashTransactionFolder = create_named_subfolder("MB Credit Cash Transaction", abbreviated_month, year)

        # Creating Meezan Bank Debit Receipts Folder
        mBDebitAppTransactionFolder = create_named_subfolder("MB Debit App Transaction", abbreviated_month, year)
        mBDebitCardTransactionFolder = create_named_subfolder("MB Debit Card Transaction", abbreviated_month, year)
        mBDebitCashTransactionFolder = create_named_subfolder("MB Debit Cash Transaction", abbreviated_month, year)


        # Creating NayaPay Receipt Folder
        nPCreditReceiptFolder = create_named_subfolder("NP Credit Receipt", abbreviated_month, year)
        nPDebitReceiptFolder = create_named_subfolder("NP Debit Receipt", abbreviated_month, year)

        # Creating NayaPay Credit Receipts Folder
        nPCreditAppTransactionFolder = create_named_subfolder("NP Credit App Transaction", abbreviated_month, year)
        nPCreditCardTransactionFolder = create_named_subfolder("NP Credit Card Transaction", abbreviated_month, year)
        nPCreditCashTransactionFolder = create_named_subfolder("NP Credit Cash Transaction", abbreviated_month, year)

        # Creating NayaPay Debit Receipts Folder
        nPDebitAppTransactionFolder = create_named_subfolder("NP Debit App Transaction", abbreviated_month, year)
        nPDebitCardTransactionFolder = create_named_subfolder("NP Debit Card Transaction", abbreviated_month, year)
        nPDebitCashTransactionFolder = create_named_subfolder("NP Debit Cash Transaction", abbreviated_month, year)


        # Creating SadaPay Receipt Folder
        sPCreditReceiptFolder = create_named_subfolder("SP Credit Receipt", abbreviated_month, year)
        sPDebitReceiptFolder = create_named_subfolder("SP Debit Receipt", abbreviated_month, year)

        # Creating SadaPay Credit Receipts Folder
        sPCreditAppTransactionFolder = create_named_subfolder("SP Credit App Transaction", abbreviated_month, year)
        sPCreditCardTransactionFolder = create_named_subfolder("SP Credit Card Transaction", abbreviated_month, year)
        sPCreditCashTransactionFolder = create_named_subfolder("SP Credit Cash Transaction", abbreviated_month, year)

        # Creating SadaPay Debit Receipts Folder
        sPDebitAppTransactionFolder = create_named_subfolder("SP Debit App Transaction", abbreviated_month, year)
        sPDebitCardTransactionFolder = create_named_subfolder("SP Debit Card Transaction", abbreviated_month, year)
        sPDebitCashTransactionFolder = create_named_subfolder("SP Debit Cash Transaction", abbreviated_month, year)


        # Creating Standard Chartered Bank Receipt Folders
        sCBCreditCardEStatementFolder = create_named_subfolder("SCB Credit Card E Statement", abbreviated_month, year)
        sCBCreditReceiptFolder = create_named_subfolder("SCB Credit Receipt", abbreviated_month, year)
        sCBDebitCardEStatementFolder = create_named_subfolder("SCB Debit Card E Statement", abbreviated_month, year)
        sCBDebitReceiptFolder = create_named_subfolder("SCB Debit Receipt", abbreviated_month, year)

        # Creating Standard Chartered Bank Credit Receipts Folder
        sCBCreditAppTransactionFolder = create_named_subfolder("SCB Credit App Transaction", abbreviated_month, year)
        sCBCreditCardTransactionFolder = create_named_subfolder("SCB Credit Card Transaction", abbreviated_month, year)
        sCBCreditCashTransactionFolder = create_named_subfolder("SCB Credit Cash Transaction", abbreviated_month, year)

        # Creating Standard Chartered Bank Debit Receipts Folder
        sCBDebitAppTransactionFolder = create_named_subfolder("SCB Debit App Transaction", abbreviated_month, year)
        sCBDebitCardTransactionFolder = create_named_subfolder("SCB Debit Card Transaction", abbreviated_month, year)
        sCBDebitCashTransactionFolder = create_named_subfolder("SCB Debit Cash Transaction", abbreviated_month, year)


        # Creating Upaisa Receipt Folder
        uPCreditReceiptFolder = create_named_subfolder("UP Credit Receipt", abbreviated_month, year)
        uPDebitReceiptFolder = create_named_subfolder("UP Debit Receipt", abbreviated_month, year)

        # Creating Upaisa Credit Receipts Folder
        uPCreditAppTransactionFolder = create_named_subfolder("UP Credit App Transaction", abbreviated_month, year)
        uPCreditCardTransactionFolder = create_named_subfolder("UP Credit Card Transaction", abbreviated_month, year)
        uPCreditCashTransactionFolder = create_named_subfolder("UP Credit Cash Transaction", abbreviated_month, year)

        # Creating Upaisa Debit Receipts Folder
        uPDebitAppTransactionFolder = create_named_subfolder("UP Debit App Transaction", abbreviated_month, year)
        uPDebitCardTransactionFolder = create_named_subfolder("UP Debit Card Transaction", abbreviated_month, year)
        uPDebitCashTransactionFolder = create_named_subfolder("UP Debit Cash Transaction", abbreviated_month, year)


        # Creating Zindigi Receipt Folder
        zICreditReceiptFolder = create_named_subfolder("ZI Credit Receipt", abbreviated_month, year)
        zIDebitReceiptFolder = create_named_subfolder("ZI Debit Receipt", abbreviated_month, year)

        # Creating Zindigi Credit Receipts Folder
        zICreditAppTransactionFolder = create_named_subfolder("ZI Credit App Transaction", abbreviated_month, year)
        zICreditCardTransactionFolder = create_named_subfolder("ZI Credit Card Transaction", abbreviated_month, year)
        zICreditCashTransactionFolder = create_named_subfolder("ZI Credit Cash Transaction", abbreviated_month, year)

        # Creating Zindigi Debit Receipts Folder
        zIDebitAppTransactionFolder = create_named_subfolder("ZI Debit App Transaction", abbreviated_month, year)
        zIDebitCardTransactionFolder = create_named_subfolder("ZI Debit Card Transaction", abbreviated_month, year)
        zIDebitCashTransactionFolder = create_named_subfolder("ZI Debit Cash Transaction", abbreviated_month, year)


        # Creating Trading Receipt Folder
        cDCReceiptFolder = create_named_subfolder("CDC Receipt", abbreviated_month, year)
        cGTReceiptFolder = create_named_subfolder("CGT Receipt", abbreviated_month, year)
        kTradeReceiptFolder = create_named_subfolder("KTrade Receipt", abbreviated_month, year)

        # Creating KTrade Receipt Folder
        kTradeDividendStatementFolder = create_named_subfolder("KTrade Dividend Statement", abbreviated_month, year)
        kTradeEStatementFolder = create_named_subfolder("KTrade E Statement", abbreviated_month, year)
        kTradeTradeConfirmationFolder = create_named_subfolder("KTrade Trade Confirmation", abbreviated_month, year)


        # Moving Allied Bank Credit Receipts into Allied Bank Credit Receipts Folder
        move_folder_if_exists(aBCreditAppTransactionFolder, aBCreditReceiptFolder)
        move_folder_if_exists(aBCreditCardTransactionFolder, aBCreditReceiptFolder)
        move_folder_if_exists(aBCreditCashTransactionFolder, aBCreditReceiptFolder)

        # Moving Allied Bank Debit Receipts into Allied Bank Debit Receipts Folder
        move_folder_if_exists(aBDebitAppTransactionFolder, aBDebitReceiptFolder)
        move_folder_if_exists(aBDebitCardTransactionFolder, aBDebitReceiptFolder)
        move_folder_if_exists(aBDebitCashTransactionFolder, aBDebitReceiptFolder)

        # Moving Allied Bank Receipts into Allied Bank Folder
        move_folder_if_exists(aBCreditCardEStatementFolder, alliedBankReceiptsFolder)
        move_folder_if_exists(aBCreditReceiptFolder, alliedBankReceiptsFolder)
        move_folder_if_exists(aBDebitCardEStatementFolder, alliedBankReceiptsFolder)
        move_folder_if_exists(aBDebitReceiptFolder, alliedBankReceiptsFolder)

        # Moving Bank Alfalah Credit Receipts into Bank Alfalah Credit Receipts Folder
        move_folder_if_exists(bACreditAppTransactionFolder, bACreditReceiptFolder)
        move_folder_if_exists(bACreditCardTransactionFolder, bACreditReceiptFolder)
        move_folder_if_exists(bACreditCashTransactionFolder, bACreditReceiptFolder)

        # Moving Bank Alfalah Debit Receipts into Bank Alfalah Debit Receipts Folder
        move_folder_if_exists(bADebitAppTransactionFolder, bADebitReceiptFolder)
        move_folder_if_exists(bADebitCardTransactionFolder, bADebitReceiptFolder)
        move_folder_if_exists(bADebitCashTransactionFolder, bADebitReceiptFolder)

        # Moving Bank Alfalah Receipts into Bank Alfalah Folder
        move_folder_if_exists(bACreditCardEStatementFolder, bankAlfalahReceiptsFolder)
        move_folder_if_exists(bACreditReceiptFolder, bankAlfalahReceiptsFolder)
        move_folder_if_exists(bADebitCardEStatementFolder, bankAlfalahReceiptsFolder)
        move_folder_if_exists(bADebitReceiptFolder, bankAlfalahReceiptsFolder)
        move_folder_if_exists(bAOrbitStatementFolder, bankAlfalahReceiptsFolder)

        # Moving EasyPaissa Credit Receipts into EasyPaissa Credit Receipts Folder
        move_folder_if_exists(ePCreditAppTransactionFolder, ePCreditReceiptFolder)
        move_folder_if_exists(ePCreditCardTransactionFolder, ePCreditReceiptFolder)
        move_folder_if_exists(ePCreditCashTransactionFolder, ePCreditReceiptFolder)

        # Moving EasyPaissa Debit Receipts into EasyPaissa Debit Receipts Folder
        move_folder_if_exists(ePDebitAppTransactionFolder, ePDebitReceiptFolder)
        move_folder_if_exists(ePDebitCardTransactionFolder, ePDebitReceiptFolder)
        move_folder_if_exists(ePDebitCashTransactionFolder, ePDebitReceiptFolder)

        # Moving EasyPaissa Receipts into EasyPaissa Folder
        move_folder_if_exists(ePCreditReceiptFolder, easyPaissaReceiptsFolder)
        move_folder_if_exists(ePDebitReceiptFolder, easyPaissaReceiptsFolder)

        # Moving FirstPay Credit Receipts into FirstPay Credit Receipts Folder
        move_folder_if_exists(fPCreditAppTransactionFolder, fPCreditReceiptFolder)
        move_folder_if_exists(fPCreditCardTransactionFolder, fPCreditReceiptFolder)
        move_folder_if_exists(fPCreditCashTransactionFolder, fPCreditReceiptFolder)

        # Moving FirstPay Debit Receipts into FirstPay Debit Receipts Folder
        move_folder_if_exists(fPDebitAppTransactionFolder, fPDebitReceiptFolder)
        move_folder_if_exists(fPDebitCardTransactionFolder, fPDebitReceiptFolder)
        move_folder_if_exists(fPDebitCashTransactionFolder, fPDebitReceiptFolder)

        # Moving FirstPay Receipts into FirstPay Folder
        move_folder_if_exists(fPCreditReceiptFolder, firstPayReceiptsFolder)
        move_folder_if_exists(fPDebitReceiptFolder, firstPayReceiptsFolder)

        # Moving JazzCash Credit Receipts into JazzCash Credit Receipts Folder
        move_folder_if_exists(jCCreditAppTransactionFolder, jCCreditReceiptFolder)
        move_folder_if_exists(jCCreditCardTransactionFolder, jCCreditReceiptFolder)
        move_folder_if_exists(jCCreditCashTransactionFolder, jCCreditReceiptFolder)

        # Moving JazzCash Debit Receipts into JazzCash Debit Receipts Folder
        move_folder_if_exists(jCDebitAppTransactionFolder, jCDebitReceiptFolder)
        move_folder_if_exists(jCDebitCardTransactionFolder, jCDebitReceiptFolder)
        move_folder_if_exists(jCDebitCashTransactionFolder, jCDebitReceiptFolder)

        # Moving JazzCash Receipts into JazzCash Folder
        move_folder_if_exists(jCCreditReceiptFolder, jazzCashReceiptsFolder)
        move_folder_if_exists(jCDebitReceiptFolder, jazzCashReceiptsFolder)

        # Moving Mashreq Credit Receipts into Mashreq Credit Receipts Folder
        move_folder_if_exists(mQCreditAppTransactionFolder, mQCreditReceiptFolder)
        move_folder_if_exists(mQCreditCardTransactionFolder, mQCreditReceiptFolder)
        move_folder_if_exists(mQCreditCashTransactionFolder, mQCreditReceiptFolder)

        # Moving Mashreq Debit Receipts into Mashreq Debit Receipts Folder
        move_folder_if_exists(mQDebitAppTransactionFolder, mQDebitReceiptFolder)
        move_folder_if_exists(mQDebitCardTransactionFolder, mQDebitReceiptFolder)
        move_folder_if_exists(mQDebitCashTransactionFolder, mQDebitReceiptFolder)

        # Moving Mashreq Receipts into Mashreq Folder
        move_folder_if_exists(mQCreditReceiptFolder, mashreqReceiptsFolder)
        move_folder_if_exists(mQDebitReceiptFolder, mashreqReceiptsFolder)

        # Moving Meezan Bank Credit Receipts into Meezan Bank Credit Receipts Folder
        move_folder_if_exists(mBCreditAppTransactionFolder, mBCreditReceiptFolder)
        move_folder_if_exists(mBCreditCardTransactionFolder, mBCreditReceiptFolder)
        move_folder_if_exists(mBCreditCashTransactionFolder, mBCreditReceiptFolder)

        # Moving Meezan Bank Debit Receipts into Meezan Bank Debit Receipts Folder
        move_folder_if_exists(mBDebitAppTransactionFolder, mBDebitReceiptFolder)
        move_folder_if_exists(mBDebitCardTransactionFolder, mBDebitReceiptFolder)
        move_folder_if_exists(mBDebitCashTransactionFolder, mBDebitReceiptFolder)

        # Moving Meezan Bank Receipts into Meezan Bank Folder
        move_folder_if_exists(mBCreditCardEStatementFolder, meezanBankReceiptsFolder)
        move_folder_if_exists(mBCreditReceiptFolder, meezanBankReceiptsFolder)
        move_folder_if_exists(mBDebitCardEStatementFolder, meezanBankReceiptsFolder)
        move_folder_if_exists(mBDebitReceiptFolder, meezanBankReceiptsFolder)

        # Moving NayaPay Credit Receipts into NayaPay Credit Receipts Folder
        move_folder_if_exists(nPCreditAppTransactionFolder, nPCreditReceiptFolder)
        move_folder_if_exists(nPCreditCardTransactionFolder, nPCreditReceiptFolder)
        move_folder_if_exists(nPCreditCashTransactionFolder, nPCreditReceiptFolder)

        # Moving NayaPay Debit Receipts into NayaPay Debit Receipts Folder
        move_folder_if_exists(nPDebitAppTransactionFolder, nPDebitReceiptFolder)
        move_folder_if_exists(nPDebitCardTransactionFolder, nPDebitReceiptFolder)
        move_folder_if_exists(nPDebitCashTransactionFolder, nPDebitReceiptFolder)

        # Moving NayaPay Receipts into NayaPay Folder
        move_folder_if_exists(nPCreditReceiptFolder, nayaPayReceiptsFolder)
        move_folder_if_exists(nPDebitReceiptFolder, nayaPayReceiptsFolder)

        # Moving SadaPay Credit Receipts into SadaPay Credit Receipts Folder
        move_folder_if_exists(sPCreditAppTransactionFolder, sPCreditReceiptFolder)
        move_folder_if_exists(sPCreditCardTransactionFolder, sPCreditReceiptFolder)
        move_folder_if_exists(sPCreditCashTransactionFolder, sPCreditReceiptFolder)

        # Moving SadaPay Debit Receipts into SadaPay Debit Receipts Folder
        move_folder_if_exists(sPDebitAppTransactionFolder, sPDebitReceiptFolder)
        move_folder_if_exists(sPDebitCardTransactionFolder, sPDebitReceiptFolder)
        move_folder_if_exists(sPDebitCashTransactionFolder, sPDebitReceiptFolder)

        # Moving SadaPay Receipts into SadaPay Folder
        move_folder_if_exists(sPCreditReceiptFolder, sadaPayReceiptsFolder)
        move_folder_if_exists(sPDebitReceiptFolder, sadaPayReceiptsFolder)

        # Moving Standard Chartered Bank Credit Receipts into Standard Chartered Bank Credit Receipts Folder
        move_folder_if_exists(sCBCreditAppTransactionFolder, sCBCreditReceiptFolder)
        move_folder_if_exists(sCBCreditCardTransactionFolder, sCBCreditReceiptFolder)
        move_folder_if_exists(sCBCreditCashTransactionFolder, sCBCreditReceiptFolder)

        # Moving Standard Chartered Bank Debit Receipts into Standard Chartered Bank Debit Receipts Folder
        move_folder_if_exists(sCBDebitAppTransactionFolder, sCBDebitReceiptFolder)
        move_folder_if_exists(sCBDebitCardTransactionFolder, sCBDebitReceiptFolder)
        move_folder_if_exists(sCBDebitCashTransactionFolder, sCBDebitReceiptFolder)

        # Moving Standard Chartered Bank Receipts into Standard Chartered Bank Folder
        move_folder_if_exists(sCBCreditCardEStatementFolder, standardCharteredBankReceiptsFolder)
        move_folder_if_exists(sCBCreditReceiptFolder, standardCharteredBankReceiptsFolder)
        move_folder_if_exists(sCBDebitCardEStatementFolder, standardCharteredBankReceiptsFolder)
        move_folder_if_exists(sCBDebitReceiptFolder, standardCharteredBankReceiptsFolder)

        # Moving Upaisa Credit Receipts into Upaisa Credit Receipts Folder
        move_folder_if_exists(uPCreditAppTransactionFolder, uPCreditReceiptFolder)
        move_folder_if_exists(uPCreditCardTransactionFolder, uPCreditReceiptFolder)
        move_folder_if_exists(uPCreditCashTransactionFolder, uPCreditReceiptFolder)

        # Moving Upaisa Debit Receipts into Upaisa Debit Receipts Folder
        move_folder_if_exists(uPDebitAppTransactionFolder, uPDebitReceiptFolder)
        move_folder_if_exists(uPDebitCardTransactionFolder, uPDebitReceiptFolder)
        move_folder_if_exists(uPDebitCashTransactionFolder, uPDebitReceiptFolder)

        # Moving Upaisa Receipts into Upaisa Folder
        move_folder_if_exists(uPCreditReceiptFolder, uPaisaReceiptsFolder)
        move_folder_if_exists(uPDebitReceiptFolder, uPaisaReceiptsFolder)

        # Moving Zindigi Credit Receipts into Zindigi Credit Receipts Folder
        move_folder_if_exists(zICreditAppTransactionFolder, zICreditReceiptFolder)
        move_folder_if_exists(zICreditCardTransactionFolder, zICreditReceiptFolder)
        move_folder_if_exists(zICreditCashTransactionFolder, zICreditReceiptFolder)

        # Moving Zindigi Debit Receipts into Zindigi Debit Receipts Folder
        move_folder_if_exists(zIDebitAppTransactionFolder, zIDebitReceiptFolder)
        move_folder_if_exists(zIDebitCardTransactionFolder, zIDebitReceiptFolder)
        move_folder_if_exists(zIDebitCashTransactionFolder, zIDebitReceiptFolder)

        # Moving Zindigi Receipts into Zindigi Folder
        move_folder_if_exists(zICreditReceiptFolder, zindgiReceiptsFolder)
        move_folder_if_exists(zIDebitReceiptFolder, zindgiReceiptsFolder)

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
