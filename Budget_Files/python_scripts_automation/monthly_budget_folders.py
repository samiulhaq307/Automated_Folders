import os
import shutil


def generate_monthly_budget_folders(year):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]

    dest_folder = f"Receipts {year}"
    print(f"Creating Receipts {year} Folder")
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    receipts = f"Receipts"
    receipt = f"Receipt"
    market = f"Market"
    gym = f"Gym"
    account = f"Account"
    alliedBank = f"Allied Bank"
    bankAlfalah = f"Bank Alfalah"
    easyPaissa = f"EasyPaissa"
    fasset = f"Fasset"
    HBLMicrofinance = "HBL Microfinance"
    jazzCash = f"JazzCash"
    mashreqBank = f"Mashreq Bank"
    meezanBank = f"Meezan Bank"
    nayaPay = f"NayaPay"
    payoneer = "Payoneer"
    pakQatarFinance = "Pak Qatar Finance"
    raqami = f"Raqami"
    sadaPay = f"SadaPay"
    standardCharteredBank = f"Standard Chartered Bank"
    uPaisa = f"UPaisa"
    zindgi = f"Zindgi"
    trading = f"Trading"

    for i, month in enumerate(months, start=1):
        abbreviated_month = month[:3]

        # Format the index as a two-digit number
        folder_number = str(i).zfill(2)

        # Creating Monthly Receipts Folder
        monthReceiptsFolder = f"{folder_number}_{receipts} {month} {year}"
        print(f"Month {receipts} Folder Path:", monthReceiptsFolder)
        if not os.path.exists(monthReceiptsFolder):
            os.makedirs(monthReceiptsFolder)


        # Creating Market Receipts Folder
        marketReceiptsFolder = f"Market Receipts {month} {year}"
        if not os.path.exists(marketReceiptsFolder):
            os.makedirs(marketReceiptsFolder)

        # Creating Gym Receipts Folder
        gymReceiptsFolder = f"Gym Receipts {month} {year}"
        if not os.path.exists(gymReceiptsFolder):
            os.makedirs(gymReceiptsFolder)

        # Creating Account Receipts Folder
        accountReceiptsFolder = f"Account Receipts {month} {year}"
        if not os.path.exists(accountReceiptsFolder):
            os.makedirs(accountReceiptsFolder)

        # Creating All Banks Folder
        alliedBankReceiptsFolder = f"Allied Bank Receipts {month} {year}"
        if not os.path.exists(alliedBankReceiptsFolder):
            os.makedirs(alliedBankReceiptsFolder)

        bankAlfalahReceiptsFolder = f"Bank Alfalah Receipts {month} {year}"
        if not os.path.exists(bankAlfalahReceiptsFolder):
            os.makedirs(bankAlfalahReceiptsFolder)

        easyPaissaReceiptsFolder = f"EasyPaissa Receipts {month} {year}"
        if not os.path.exists(easyPaissaReceiptsFolder):
            os.makedirs(easyPaissaReceiptsFolder)

        firstPayReceiptsFolder = f"FirstPay Receipts {month} {year}"
        if not os.path.exists(firstPayReceiptsFolder):
            os.makedirs(firstPayReceiptsFolder)

        jazzCashReceiptsFolder = f"JazzCash Receipts {month} {year}"
        if not os.path.exists(jazzCashReceiptsFolder):
            os.makedirs(jazzCashReceiptsFolder)

        mashreqReceiptsFolder = f"Mashreq Receipts {month} {year}"
        if not os.path.exists(mashreqReceiptsFolder):
            os.makedirs(mashreqReceiptsFolder)

        meezanBankReceiptsFolder = f"Meezan Bank Receipts {month} {year}"
        if not os.path.exists(meezanBankReceiptsFolder):
            os.makedirs(meezanBankReceiptsFolder)

        nayaPayReceiptsFolder = f"NayaPay Receipts {month} {year}"
        if not os.path.exists(nayaPayReceiptsFolder):
            os.makedirs(nayaPayReceiptsFolder)

        sadaPayReceiptsFolder = f"SadaPay Receipts {month} {year}"
        if not os.path.exists(sadaPayReceiptsFolder):
            os.makedirs(sadaPayReceiptsFolder)

        standardCharteredBankReceiptsFolder = f"Standard Chartered Bank Receipts {month} {year}"
        if not os.path.exists(standardCharteredBankReceiptsFolder):
            os.makedirs(standardCharteredBankReceiptsFolder)

        uPaisaReceiptsFolder = f"UPaisa Receipts {month} {year}"
        if not os.path.exists(uPaisaReceiptsFolder):
            os.makedirs(uPaisaReceiptsFolder)

        zindigiReceiptsFolder = f"Zindigi Receipts {month} {year}"
        if not os.path.exists(zindigiReceiptsFolder):
            os.makedirs(zindigiReceiptsFolder)

        tradingReceiptsFolder = f"Trading Receipts {month} {year}"
        if not os.path.exists(tradingReceiptsFolder):
            os.makedirs(tradingReceiptsFolder)


        # Creating Allied Bank Receipt Folders
        aBCreditCardEStatementFolder = f"AB Credit Card E Statement {abbreviated_month} {year}"
        if not os.path.exists(aBCreditCardEStatementFolder):
            os.makedirs(aBCreditCardEStatementFolder)

        aBCreditReceiptFolder = f"AB Credit Receipt {abbreviated_month} {year}"
        if not os.path.exists(aBCreditReceiptFolder):
            os.makedirs(aBCreditReceiptFolder)

        aBDebitCardEStatementFolder = f"AB Debit Card E Statement {abbreviated_month} {year}"
        if not os.path.exists(aBDebitCardEStatementFolder):
            os.makedirs(aBDebitCardEStatementFolder)

        aBDebitReceiptFolder = f"AB Debit Receipt {abbreviated_month} {year}"
        if not os.path.exists(aBDebitReceiptFolder):
            os.makedirs(aBDebitReceiptFolder)

        # Creating Allied Bank Credit Receipts Folder
        aBCreditAppTransactionFolder = f"AB Credit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(aBCreditAppTransactionFolder):
            os.makedirs(aBCreditAppTransactionFolder)

        aBCreditCardTransactionFolder = f"AB Credit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(aBCreditCardTransactionFolder):
            os.makedirs(aBCreditCardTransactionFolder)

        aBCreditCashTransactionFolder = f"AB Credit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(aBCreditCashTransactionFolder):
            os.makedirs(aBCreditCashTransactionFolder)

        # Creating Allied Bank Debit Receipts Folder
        aBDebitAppTransactionFolder = f"AB Debit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(aBDebitAppTransactionFolder):
            os.makedirs(aBDebitAppTransactionFolder)

        aBDebitCardTransactionFolder = f"AB Debit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(aBDebitCardTransactionFolder):
            os.makedirs(aBDebitCardTransactionFolder)

        aBDebitCashTransactionFolder = f"AB Debit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(aBDebitCashTransactionFolder):
            os.makedirs(aBDebitCashTransactionFolder)

        # Creating Bank Alfalah Receipt Folders
        bACreditCardEStatementFolder = f"BA Credit Card E Statement {abbreviated_month} {year}"
        if not os.path.exists(bACreditCardEStatementFolder):
            os.makedirs(bACreditCardEStatementFolder)

        bACreditReceiptFolder = f"BA Credit Receipt {abbreviated_month} {year}"
        if not os.path.exists(bACreditReceiptFolder):
            os.makedirs(bACreditReceiptFolder)

        bADebitCardEStatementFolder = f"BA Debit Card E Statement {abbreviated_month} {year}"
        if not os.path.exists(bADebitCardEStatementFolder):
            os.makedirs(bADebitCardEStatementFolder)

        bADebitReceiptFolder = f"BA Debit Receipt {abbreviated_month} {year}"
        if not os.path.exists(bADebitReceiptFolder):
            os.makedirs(bADebitReceiptFolder)

        bAOrbitStatementFolder = f"BA Orbit Statement {abbreviated_month} {year}"
        if not os.path.exists(bAOrbitStatementFolder):
            os.makedirs(bAOrbitStatementFolder)

        # Creating Bank Alfalah Credit Receipts Folder
        bACreditAppTransactionFolder = f"BA Credit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(bACreditAppTransactionFolder):
            os.makedirs(bACreditAppTransactionFolder)

        bACreditCardTransactionFolder = f"BA Credit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(bACreditCardTransactionFolder):
            os.makedirs(bACreditCardTransactionFolder)

        bACreditCashTransactionFolder = f"BA Credit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(bACreditCashTransactionFolder):
            os.makedirs(bACreditCashTransactionFolder)

        # Creating Bank Alfalah Debit Receipts Folder
        bADebitAppTransactionFolder = f"BA Debit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(bADebitAppTransactionFolder):
            os.makedirs(bADebitAppTransactionFolder)

        bADebitCardTransactionFolder = f"BA Debit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(bADebitCardTransactionFolder):
            os.makedirs(bADebitCardTransactionFolder)

        bADebitCashTransactionFolder = f"BA Debit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(bADebitCashTransactionFolder):
            os.makedirs(bADebitCashTransactionFolder)


        # Creating EasyPaissa Receipt Folder
        ePCreditReceiptFolder = f"EP Credit Receipt {abbreviated_month} {year}"
        if not os.path.exists(ePCreditReceiptFolder):
            os.makedirs(ePCreditReceiptFolder)

        ePDebitReceiptFolder = f"EP Debit Receipt {abbreviated_month} {year}"
        if not os.path.exists(ePDebitReceiptFolder):
            os.makedirs(ePDebitReceiptFolder)


        # Creating EasyPaissa Credit Receipts Folder
        ePCreditAppTransactionFolder = f"EP Credit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(ePCreditAppTransactionFolder):
            os.makedirs(ePCreditAppTransactionFolder)

        ePCreditCardTransactionFolder = f"EP Credit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(ePCreditCardTransactionFolder):
            os.makedirs(ePCreditCardTransactionFolder)

        ePCreditCashTransactionFolder = f"EP Credit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(ePCreditCashTransactionFolder):
            os.makedirs(ePCreditCashTransactionFolder)

        # Creating EasyPaissa Debit Receipts Folder
        ePDebitAppTransactionFolder = f"EP Debit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(ePDebitAppTransactionFolder):
            os.makedirs(ePDebitAppTransactionFolder)

        ePDebitCardTransactionFolder = f"EP Debit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(ePDebitCardTransactionFolder):
            os.makedirs(ePDebitCardTransactionFolder)

        ePDebitCashTransactionFolder = f"EP Debit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(ePDebitCashTransactionFolder):
            os.makedirs(ePDebitCashTransactionFolder)

        # Creating FirstPay Receipt Folder
        fPCreditReceiptFolder = f"FP Credit Receipt {abbreviated_month} {year}"
        if not os.path.exists(fPCreditReceiptFolder):
            os.makedirs(fPCreditReceiptFolder)

        fPDebitReceiptFolder = f"FP Debit Receipt {abbreviated_month} {year}"
        if not os.path.exists(fPDebitReceiptFolder):
            os.makedirs(fPDebitReceiptFolder)

        # Creating FirstPay Credit Receipts Folder
        fPCreditAppTransactionFolder = f"FP Credit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(fPCreditAppTransactionFolder):
            os.makedirs(fPCreditAppTransactionFolder)

        fPCreditCardTransactionFolder = f"FP Credit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(fPCreditCardTransactionFolder):
            os.makedirs(fPCreditCardTransactionFolder)

        fPCreditCashTransactionFolder = f"FP Credit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(fPCreditCashTransactionFolder):
            os.makedirs(fPCreditCashTransactionFolder)

        # Creating FirstPay Debit Receipts Folder
        fPDebitAppTransactionFolder = f"FP Debit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(fPDebitAppTransactionFolder):
            os.makedirs(fPDebitAppTransactionFolder)

        fPDebitCardTransactionFolder = f"FP Debit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(fPDebitCardTransactionFolder):
            os.makedirs(fPDebitCardTransactionFolder)

        fPDebitCashTransactionFolder = f"FP Debit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(fPDebitCashTransactionFolder):
            os.makedirs(fPDebitCashTransactionFolder)


        # Creating JazzCash Receipt Folder
        jCCreditReceiptFolder = f"JC Credit Receipt {abbreviated_month} {year}"
        if not os.path.exists(jCCreditReceiptFolder):
            os.makedirs(jCCreditReceiptFolder)

        jCDebitReceiptFolder = f"JC Debit Receipt {abbreviated_month} {year}"
        if not os.path.exists(jCDebitReceiptFolder):
            os.makedirs(jCDebitReceiptFolder)

        # Creating JazzCash Credit Receipts Folder
        jCCreditAppTransactionFolder = f"JC Credit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(jCCreditAppTransactionFolder):
            os.makedirs(jCCreditAppTransactionFolder)

        jCCreditCardTransactionFolder = f"JC Credit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(jCCreditCardTransactionFolder):
            os.makedirs(jCCreditCardTransactionFolder)

        jCCreditCashTransactionFolder = f"JC Credit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(jCCreditCashTransactionFolder):
            os.makedirs(jCCreditCashTransactionFolder)

        # Creating JazzCash Debit Receipts Folder
        jCDebitAppTransactionFolder = f"JC Debit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(jCDebitAppTransactionFolder):
            os.makedirs(jCDebitAppTransactionFolder)

        jCDebitCardTransactionFolder = f"JC Debit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(jCDebitCardTransactionFolder):
            os.makedirs(jCDebitCardTransactionFolder)

        jCDebitCashTransactionFolder = f"JC Debit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(jCDebitCashTransactionFolder):
            os.makedirs(jCDebitCashTransactionFolder)

        # Creating Mashreq Receipt Folder
        mQCreditReceiptFolder = f"MQ Credit Receipt {abbreviated_month} {year}"
        if not os.path.exists(mQCreditReceiptFolder):
            os.makedirs(mQCreditReceiptFolder)

        mQDebitReceiptFolder = f"MQ Debit Receipt {abbreviated_month} {year}"
        if not os.path.exists(mQDebitReceiptFolder):
            os.makedirs(mQDebitReceiptFolder)

        # Creating Mashreq Credit Receipts Folder
        mQCreditAppTransactionFolder = f"MQ Credit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(mQCreditAppTransactionFolder):
            os.makedirs(mQCreditAppTransactionFolder)

        mQCreditCardTransactionFolder = f"MQ Credit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(mQCreditCardTransactionFolder):
            os.makedirs(mQCreditCardTransactionFolder)

        mQCreditCashTransactionFolder = f"MQ Credit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(mQCreditCashTransactionFolder):
            os.makedirs(mQCreditCashTransactionFolder)

        # Creating Mashreq Debit Receipts Folder
        mQDebitAppTransactionFolder = f"MQ Debit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(mQDebitAppTransactionFolder):
            os.makedirs(mQDebitAppTransactionFolder)

        mQDebitCardTransactionFolder = f"MQ Debit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(mQDebitCardTransactionFolder):
            os.makedirs(mQDebitCardTransactionFolder)

        mQDebitCashTransactionFolder = f"MQ Debit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(mQDebitCashTransactionFolder):
            os.makedirs(mQDebitCashTransactionFolder)


        # Creating Meezan Bank Receipt Folders
        mBCreditCardEStatementFolder = f"MB Credit Card E Statement {abbreviated_month} {year}"
        if not os.path.exists(mBCreditCardEStatementFolder):
            os.makedirs(mBCreditCardEStatementFolder)

        mBCreditReceiptFolder = f"MB Credit Receipt {abbreviated_month} {year}"
        if not os.path.exists(mBCreditReceiptFolder):
            os.makedirs(mBCreditReceiptFolder)

        mBDebitCardEStatementFolder = f"MB Debit Card E Statement {abbreviated_month} {year}"
        if not os.path.exists(mBDebitCardEStatementFolder):
            os.makedirs(mBDebitCardEStatementFolder)

        mBDebitReceiptFolder = f"MB Debit Receipt {abbreviated_month} {year}"
        if not os.path.exists(mBDebitReceiptFolder):
            os.makedirs(mBDebitReceiptFolder)

        # Creating Meezan Bank Credit Receipts Folder
        mBCreditAppTransactionFolder = f"MB Credit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(mBCreditAppTransactionFolder):
            os.makedirs(mBCreditAppTransactionFolder)

        mBCreditCardTransactionFolder = f"MB Credit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(mBCreditCardTransactionFolder):
            os.makedirs(mBCreditCardTransactionFolder)

        mBCreditCashTransactionFolder = f"MB Credit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(mBCreditCashTransactionFolder):
            os.makedirs(mBCreditCashTransactionFolder)

        # Creating Meezan Bank Debit Receipts Folder
        mBDebitAppTransactionFolder = f"MB Debit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(mBDebitAppTransactionFolder):
            os.makedirs(mBDebitAppTransactionFolder)

        mBDebitCardTransactionFolder = f"MB Debit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(mBDebitCardTransactionFolder):
            os.makedirs(mBDebitCardTransactionFolder)

        mBDebitCashTransactionFolder = f"MB Debit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(mBDebitCashTransactionFolder):
            os.makedirs(mBDebitCashTransactionFolder)


        # Creating NayaPay Receipt Folder
        nPCreditReceiptFolder = f"NP Credit Receipt {abbreviated_month} {year}"
        if not os.path.exists(nPCreditReceiptFolder):
            os.makedirs(nPCreditReceiptFolder)

        nPDebitReceiptFolder = f"NP Debit Receipt {abbreviated_month} {year}"
        if not os.path.exists(nPDebitReceiptFolder):
            os.makedirs(nPDebitReceiptFolder)

        # Creating NayaPay Credit Receipts Folder
        nPCreditAppTransactionFolder = f"NP Credit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(nPCreditAppTransactionFolder):
            os.makedirs(nPCreditAppTransactionFolder)

        nPCreditCardTransactionFolder = f"NP Credit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(nPCreditCardTransactionFolder):
            os.makedirs(nPCreditCardTransactionFolder)

        nPCreditCashTransactionFolder = f"NP Credit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(nPCreditCashTransactionFolder):
            os.makedirs(nPCreditCashTransactionFolder)

        # Creating NayaPay Debit Receipts Folder
        nPDebitAppTransactionFolder = f"NP Debit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(nPDebitAppTransactionFolder):
            os.makedirs(nPDebitAppTransactionFolder)

        nPDebitCardTransactionFolder = f"NP Debit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(nPDebitCardTransactionFolder):
            os.makedirs(nPDebitCardTransactionFolder)

        nPDebitCashTransactionFolder = f"NP Debit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(nPDebitCashTransactionFolder):
            os.makedirs(nPDebitCashTransactionFolder)


        # Creating SadaPay Receipt Folder
        sPCreditReceiptFolder = f"SP Credit Receipt {abbreviated_month} {year}"
        if not os.path.exists(sPCreditReceiptFolder):
            os.makedirs(sPCreditReceiptFolder)

        sPDebitReceiptFolder = f"SP Debit Receipt {abbreviated_month} {year}"
        if not os.path.exists(sPDebitReceiptFolder):
            os.makedirs(sPDebitReceiptFolder)

        # Creating SadaPay Credit Receipts Folder
        sPCreditAppTransactionFolder = f"SP Credit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(sPCreditAppTransactionFolder):
            os.makedirs(sPCreditAppTransactionFolder)

        sPCreditCardTransactionFolder = f"SP Credit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(sPCreditCardTransactionFolder):
            os.makedirs(sPCreditCardTransactionFolder)

        sPCreditCashTransactionFolder = f"SP Credit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(sPCreditCashTransactionFolder):
            os.makedirs(sPCreditCashTransactionFolder)

        # Creating SadaPay Debit Receipts Folder
        sPDebitAppTransactionFolder = f"SP Debit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(sPDebitAppTransactionFolder):
            os.makedirs(sPDebitAppTransactionFolder)

        sPDebitCardTransactionFolder = f"SP Debit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(sPDebitCardTransactionFolder):
            os.makedirs(sPDebitCardTransactionFolder)

        sPDebitCashTransactionFolder = f"SP Debit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(sPDebitCashTransactionFolder):
            os.makedirs(sPDebitCashTransactionFolder)


        # Creating Standard Chartered Bank Receipt Folders
        sCBCreditCardEStatementFolder = f"SCB Credit Card E Statement {abbreviated_month} {year}"
        if not os.path.exists(sCBCreditCardEStatementFolder):
            os.makedirs(sCBCreditCardEStatementFolder)

        sCBCreditReceiptFolder = f"SCB Credit Receipt {abbreviated_month} {year}"
        if not os.path.exists(sCBCreditReceiptFolder):
            os.makedirs(sCBCreditReceiptFolder)

        sCBDebitCardEStatementFolder = f"SCB Debit Card E Statement {abbreviated_month} {year}"
        if not os.path.exists(sCBDebitCardEStatementFolder):
            os.makedirs(sCBDebitCardEStatementFolder)

        sCBDebitReceiptFolder = f"SCB Debit Receipt {abbreviated_month} {year}"
        if not os.path.exists(sCBDebitReceiptFolder):
            os.makedirs(sCBDebitReceiptFolder)

        # Creating Standard Chartered Bank Credit Receipts Folder
        sCBCreditAppTransactionFolder = f"SCB Credit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(sCBCreditAppTransactionFolder):
            os.makedirs(sCBCreditAppTransactionFolder)

        sCBCreditCardTransactionFolder = f"SCB Credit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(sCBCreditCardTransactionFolder):
            os.makedirs(sCBCreditCardTransactionFolder)

        sCBCreditCashTransactionFolder = f"SCB Credit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(sCBCreditCashTransactionFolder):
            os.makedirs(sCBCreditCashTransactionFolder)

        # Creating Standard Chartered Bank Debit Receipts Folder
        sCBDebitAppTransactionFolder = f"SCB Debit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(sCBDebitAppTransactionFolder):
            os.makedirs(sCBDebitAppTransactionFolder)

        sCBDebitCardTransactionFolder = f"SCB Debit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(sCBDebitCardTransactionFolder):
            os.makedirs(sCBDebitCardTransactionFolder)

        sCBDebitCashTransactionFolder = f"SCB Debit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(sCBDebitCashTransactionFolder):
            os.makedirs(sCBDebitCashTransactionFolder)


        # Creating Upaisa Receipt Folder
        uPCreditReceiptFolder = f"UP Credit Receipt {abbreviated_month} {year}"
        if not os.path.exists(uPCreditReceiptFolder):
            os.makedirs(uPCreditReceiptFolder)

        uPDebitReceiptFolder = f"UP Debit Receipt {abbreviated_month} {year}"
        if not os.path.exists(uPDebitReceiptFolder):
            os.makedirs(uPDebitReceiptFolder)

        # Creating Upaisa Credit Receipts Folder
        uPCreditAppTransactionFolder = f"UP Credit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(uPCreditAppTransactionFolder):
            os.makedirs(uPCreditAppTransactionFolder)

        uPCreditCardTransactionFolder = f"UP Credit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(uPCreditCardTransactionFolder):
            os.makedirs(uPCreditCardTransactionFolder)

        uPCreditCashTransactionFolder = f"UP Credit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(uPCreditCashTransactionFolder):
            os.makedirs(uPCreditCashTransactionFolder)

        # Creating Upaisa Debit Receipts Folder
        uPDebitAppTransactionFolder = f"UP Debit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(uPDebitAppTransactionFolder):
            os.makedirs(uPDebitAppTransactionFolder)

        uPDebitCardTransactionFolder = f"UP Debit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(uPDebitCardTransactionFolder):
            os.makedirs(uPDebitCardTransactionFolder)

        uPDebitCashTransactionFolder = f"UP Debit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(uPDebitCashTransactionFolder):
            os.makedirs(uPDebitCashTransactionFolder)

        # Creating Zindigi Receipt Folder
        zICreditReceiptFolder = f"ZI Credit Receipt {abbreviated_month} {year}"
        if not os.path.exists(zICreditReceiptFolder):
            os.makedirs(zICreditReceiptFolder)

        zIDebitReceiptFolder = f"ZI Debit Receipt {abbreviated_month} {year}"
        if not os.path.exists(zIDebitReceiptFolder):
            os.makedirs(zIDebitReceiptFolder)

        # Creating Zindigi Credit Receipts Folder
        zICreditAppTransactionFolder = f"ZI Credit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(zICreditAppTransactionFolder):
            os.makedirs(zICreditAppTransactionFolder)

        zICreditCardTransactionFolder = f"ZI Credit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(zICreditCardTransactionFolder):
            os.makedirs(zICreditCardTransactionFolder)

        zICreditCashTransactionFolder = f"ZI Credit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(zICreditCashTransactionFolder):
            os.makedirs(zICreditCashTransactionFolder)

        # Creating Zindigi Debit Receipts Folder
        zIDebitAppTransactionFolder = f"ZI Debit App Transaction {abbreviated_month} {year}"
        if not os.path.exists(zIDebitAppTransactionFolder):
            os.makedirs(zIDebitAppTransactionFolder)

        zIDebitCardTransactionFolder = f"ZI Debit Card Transaction {abbreviated_month} {year}"
        if not os.path.exists(zIDebitCardTransactionFolder):
            os.makedirs(zIDebitCardTransactionFolder)

        zIDebitCashTransactionFolder = f"ZI Debit Cash Transaction {abbreviated_month} {year}"
        if not os.path.exists(zIDebitCashTransactionFolder):
            os.makedirs(zIDebitCashTransactionFolder)


        # Creating Trading Receipt Folder
        cDCReceiptFolder = f"CDC Receipt {abbreviated_month} {year}"
        if not os.path.exists(cDCReceiptFolder):
            os.makedirs(cDCReceiptFolder)

        cGTReceiptFolder = f"CGT Receipt {abbreviated_month} {year}"
        if not os.path.exists(cGTReceiptFolder):
            os.makedirs(cGTReceiptFolder)

        kTradeReceiptFolder = f"KTrade Receipt {abbreviated_month} {year}"
        if not os.path.exists(kTradeReceiptFolder):
            os.makedirs(kTradeReceiptFolder)

        # Creating KTrade Dividend Statement
        kTradeDividendStatementFolder = f"KTrade Dividend Statement {abbreviated_month} {year}"
        if not os.path.exists(kTradeDividendStatementFolder):
            os.makedirs(kTradeDividendStatementFolder)

        # Creating KTrade E Statement Folder
        kTradeEStatementFolder = f"KTrade E Statement {abbreviated_month} {year}"
        if not os.path.exists(kTradeEStatementFolder):
            os.makedirs(kTradeEStatementFolder)

        # Creating KTrade Trade Confirmation Folder
        kTradeTradeConfirmationFolder = f"KTrade Trade Confirmation {abbreviated_month} {year}"
        if not os.path.exists(kTradeTradeConfirmationFolder):
            os.makedirs(kTradeTradeConfirmationFolder)


        # Moving Allied Bank Credit Receipts into Allied Bank Credit Receipts Folder
        if os.path.exists(aBCreditAppTransactionFolder):
            shutil.move(aBCreditAppTransactionFolder, aBCreditReceiptFolder)

        if os.path.exists(aBCreditCardTransactionFolder):
            shutil.move(aBCreditCardTransactionFolder, aBCreditReceiptFolder)

        if os.path.exists(aBCreditCashTransactionFolder):
            shutil.move(aBCreditCashTransactionFolder, aBCreditReceiptFolder)

        # Moving Allied Bank Debit Receipts into Allied Bank Debit Receipts Folder
        if os.path.exists(aBDebitAppTransactionFolder):
            shutil.move(aBDebitAppTransactionFolder, aBDebitReceiptFolder)

        if os.path.exists(aBDebitCardTransactionFolder):
            shutil.move(aBDebitCardTransactionFolder, aBDebitReceiptFolder)

        if os.path.exists(aBDebitCashTransactionFolder):
            shutil.move(aBDebitCashTransactionFolder, aBDebitReceiptFolder)

        # Moving Allied Bank Receipts into Allied Bank Folder
        if os.path.exists(aBCreditCardEStatementFolder):
            shutil.move(aBCreditCardEStatementFolder, alliedBankReceiptsFolder)
        if os.path.exists(aBCreditReceiptFolder):
            shutil.move(aBCreditReceiptFolder, alliedBankReceiptsFolder)
        if os.path.exists(aBDebitCardEStatementFolder):
            shutil.move(aBDebitCardEStatementFolder, alliedBankReceiptsFolder)
        if os.path.exists(aBDebitReceiptFolder):
            shutil.move(aBDebitReceiptFolder, alliedBankReceiptsFolder)


        # Moving Bank Alfalah Credit Receipts into Bank Alfalah Credit Receipts Folder
        if os.path.exists(bACreditAppTransactionFolder):
            shutil.move(bACreditAppTransactionFolder, bACreditReceiptFolder)

        if os.path.exists(bACreditCardTransactionFolder):
            shutil.move(bACreditCardTransactionFolder, bACreditReceiptFolder)

        if os.path.exists(bACreditCashTransactionFolder):
            shutil.move(bACreditCashTransactionFolder, bACreditReceiptFolder)

        # Moving Bank Alfalah Debit Receipts into Bank Alfalah Debit Receipts Folder
        if os.path.exists(bADebitAppTransactionFolder):
            shutil.move(bADebitAppTransactionFolder, bADebitReceiptFolder)

        if os.path.exists(bADebitCardTransactionFolder):
            shutil.move(bADebitCardTransactionFolder, bADebitReceiptFolder)

        if os.path.exists(bADebitCashTransactionFolder):
            shutil.move(bADebitCashTransactionFolder, bADebitReceiptFolder)

        # Moving Bank Alfalah Receipts into Bank Alfalah Folder
        if os.path.exists(bACreditCardEStatementFolder):
            shutil.move(bACreditCardEStatementFolder, bankAlfalahReceiptsFolder)
        if os.path.exists(bACreditReceiptFolder):
            shutil.move(bACreditReceiptFolder, bankAlfalahReceiptsFolder)
        if os.path.exists(bADebitCardEStatementFolder):
            shutil.move(bADebitCardEStatementFolder, bankAlfalahReceiptsFolder)
        if os.path.exists(bADebitReceiptFolder):
            shutil.move(bADebitReceiptFolder, bankAlfalahReceiptsFolder)
        if os.path.exists(bAOrbitStatementFolder):
            shutil.move(bAOrbitStatementFolder, bankAlfalahReceiptsFolder)


        # Moving EasyPaissa Credit Receipts into EasyPaissa Credit Receipts Folder
        if os.path.exists(ePCreditAppTransactionFolder):
            shutil.move(ePCreditAppTransactionFolder, ePCreditReceiptFolder)

        if os.path.exists(ePCreditCardTransactionFolder):
            shutil.move(ePCreditCardTransactionFolder, ePCreditReceiptFolder)

        if os.path.exists(ePCreditCashTransactionFolder):
            shutil.move(ePCreditCashTransactionFolder, ePCreditReceiptFolder)

        # Moving EasyPaissa Debit Receipts into EasyPaissa Debit Receipts Folder
        if os.path.exists(ePDebitAppTransactionFolder):
            shutil.move(ePDebitAppTransactionFolder, ePDebitReceiptFolder)

        if os.path.exists(ePDebitCardTransactionFolder):
            shutil.move(ePDebitCardTransactionFolder, ePDebitReceiptFolder)

        if os.path.exists(ePDebitCashTransactionFolder):
            shutil.move(ePDebitCashTransactionFolder, ePDebitReceiptFolder)

        # Moving EasyPaissa Receipts into EasyPaissa Folder
        if os.path.exists(ePCreditReceiptFolder):
            shutil.move(ePCreditReceiptFolder, easyPaissaReceiptsFolder)

        if os.path.exists(ePDebitReceiptFolder):
            shutil.move(ePDebitReceiptFolder, easyPaissaReceiptsFolder)

        # Moving FirstPay Credit Receipts into FirstPay Credit Receipts Folder
        if os.path.exists(fPCreditAppTransactionFolder):
            shutil.move(fPCreditAppTransactionFolder, fPCreditReceiptFolder)

        if os.path.exists(fPCreditCardTransactionFolder):
            shutil.move(fPCreditCardTransactionFolder, fPCreditReceiptFolder)

        if os.path.exists(fPCreditCashTransactionFolder):
            shutil.move(fPCreditCashTransactionFolder, fPCreditReceiptFolder)

        # Moving FirstPay Debit Receipts into FirstPay Debit Receipts Folder
        if os.path.exists(fPDebitAppTransactionFolder):
            shutil.move(fPDebitAppTransactionFolder, fPDebitReceiptFolder)

        if os.path.exists(fPDebitCardTransactionFolder):
            shutil.move(fPDebitCardTransactionFolder, fPDebitReceiptFolder)

        if os.path.exists(fPDebitCashTransactionFolder):
            shutil.move(fPDebitCashTransactionFolder, fPDebitReceiptFolder)

        # Moving FirstPay Receipts into FirstPay Folder
        if os.path.exists(fPCreditReceiptFolder):
            shutil.move(fPCreditReceiptFolder, firstPayReceiptsFolder)

        if os.path.exists(fPDebitReceiptFolder):
            shutil.move(fPDebitReceiptFolder, firstPayReceiptsFolder)


        # Moving JazzCash Credit Receipts into JazzCash Credit Receipts Folder
        if os.path.exists(jCCreditAppTransactionFolder):
            shutil.move(jCCreditAppTransactionFolder, jCCreditReceiptFolder)

        if os.path.exists(jCCreditCardTransactionFolder):
            shutil.move(jCCreditCardTransactionFolder, jCCreditReceiptFolder)

        if os.path.exists(jCCreditCashTransactionFolder):
            shutil.move(jCCreditCashTransactionFolder, jCCreditReceiptFolder)

        # Moving JazzCash Debit Receipts into JazzCash Debit Receipts Folder
        if os.path.exists(jCDebitAppTransactionFolder):
            shutil.move(jCDebitAppTransactionFolder, jCDebitReceiptFolder)

        if os.path.exists(jCDebitCardTransactionFolder):
            shutil.move(jCDebitCardTransactionFolder, jCDebitReceiptFolder)

        if os.path.exists(jCDebitCashTransactionFolder):
            shutil.move(jCDebitCashTransactionFolder, jCDebitReceiptFolder)

        # Moving JazzCash Receipts into JazzCash Folder
        if os.path.exists(jCCreditReceiptFolder):
            shutil.move(jCCreditReceiptFolder, jazzCashReceiptsFolder)

        if os.path.exists(jCDebitReceiptFolder):
            shutil.move(jCDebitReceiptFolder, jazzCashReceiptsFolder)

        # Moving Mashreq Credit Receipts into Mashreq Credit Receipts Folder
        if os.path.exists(mQCreditAppTransactionFolder):
            shutil.move(mQCreditAppTransactionFolder, mQCreditReceiptFolder)

        if os.path.exists(mQCreditCardTransactionFolder):
            shutil.move(mQCreditCardTransactionFolder, mQCreditReceiptFolder)

        if os.path.exists(mQCreditCashTransactionFolder):
            shutil.move(mQCreditCashTransactionFolder, mQCreditReceiptFolder)

        # Moving Mashreq Debit Receipts into Mashreq Debit Receipts Folder
        if os.path.exists(mQDebitAppTransactionFolder):
            shutil.move(mQDebitAppTransactionFolder, mQDebitReceiptFolder)

        if os.path.exists(mQDebitCardTransactionFolder):
            shutil.move(mQDebitCardTransactionFolder, mQDebitReceiptFolder)

        if os.path.exists(mQDebitCashTransactionFolder):
            shutil.move(mQDebitCashTransactionFolder, mQDebitReceiptFolder)

        # Moving Mashreq Receipts into Mashreq Folder
        if os.path.exists(mQCreditReceiptFolder):
            shutil.move(mQCreditReceiptFolder, mashreqReceiptsFolder)

        if os.path.exists(mQDebitReceiptFolder):
            shutil.move(mQDebitReceiptFolder, mashreqReceiptsFolder)


        # Moving Meezan Bank Credit Receipts into Meezan Bank Credit Receipts Folder
        if os.path.exists(mBCreditAppTransactionFolder):
            shutil.move(mBCreditAppTransactionFolder, mBCreditReceiptFolder)

        if os.path.exists(mBCreditCardTransactionFolder):
            shutil.move(mBCreditCardTransactionFolder, mBCreditReceiptFolder)

        if os.path.exists(mBCreditCashTransactionFolder):
            shutil.move(mBCreditCashTransactionFolder, mBCreditReceiptFolder)

        # Moving Meezan Bank Debit Receipts into Meezan Bank Debit Receipts Folder
        if os.path.exists(mBDebitAppTransactionFolder):
            shutil.move(mBDebitAppTransactionFolder, mBDebitReceiptFolder)

        if os.path.exists(mBDebitCardTransactionFolder):
            shutil.move(mBDebitCardTransactionFolder, mBDebitReceiptFolder)

        if os.path.exists(mBDebitCashTransactionFolder):
            shutil.move(mBDebitCashTransactionFolder, mBDebitReceiptFolder)

        # Moving Meezan Bank Receipts into Meezan Bank Folder
        if os.path.exists(mBCreditCardEStatementFolder):
            shutil.move(mBCreditCardEStatementFolder, meezanBankReceiptsFolder)
        if os.path.exists(mBCreditReceiptFolder):
            shutil.move(mBCreditReceiptFolder, meezanBankReceiptsFolder)
        if os.path.exists(mBDebitCardEStatementFolder):
            shutil.move(mBDebitCardEStatementFolder, meezanBankReceiptsFolder)
        if os.path.exists(mBDebitReceiptFolder):
            shutil.move(mBDebitReceiptFolder, meezanBankReceiptsFolder)


        # Moving NayaPay Credit Receipts into NayaPay Credit Receipts Folder
        if os.path.exists(nPCreditAppTransactionFolder):
            shutil.move(nPCreditAppTransactionFolder, nPCreditReceiptFolder)

        if os.path.exists(nPCreditCardTransactionFolder):
            shutil.move(nPCreditCardTransactionFolder, nPCreditReceiptFolder)

        if os.path.exists(nPCreditCashTransactionFolder):
            shutil.move(nPCreditCashTransactionFolder, nPCreditReceiptFolder)

        # Moving NayaPay Debit Receipts into NayaPay Debit Receipts Folder
        if os.path.exists(nPDebitAppTransactionFolder):
            shutil.move(nPDebitAppTransactionFolder, nPDebitReceiptFolder)

        if os.path.exists(nPDebitCardTransactionFolder):
            shutil.move(nPDebitCardTransactionFolder, nPDebitReceiptFolder)

        if os.path.exists(nPDebitCashTransactionFolder):
            shutil.move(nPDebitCashTransactionFolder, nPDebitReceiptFolder)

        # Moving NayaPay Receipts into NayaPay Folder
        if os.path.exists(nPCreditReceiptFolder):
            shutil.move(nPCreditReceiptFolder, nayaPayReceiptsFolder)

        if os.path.exists(nPDebitReceiptFolder):
            shutil.move(nPDebitReceiptFolder, nayaPayReceiptsFolder)


        # Moving SadaPay Credit Receipts into SadaPay Credit Receipts Folder
        if os.path.exists(sPCreditAppTransactionFolder):
            shutil.move(sPCreditAppTransactionFolder, sPCreditReceiptFolder)

        if os.path.exists(sPCreditCardTransactionFolder):
            shutil.move(sPCreditCardTransactionFolder, sPCreditReceiptFolder)

        if os.path.exists(sPCreditCashTransactionFolder):
            shutil.move(sPCreditCashTransactionFolder, sPCreditReceiptFolder)

        # Moving SadaPay Debit Receipts into SadaPay Debit Receipts Folder
        if os.path.exists(sPDebitAppTransactionFolder):
            shutil.move(sPDebitAppTransactionFolder, sPDebitReceiptFolder)

        if os.path.exists(sPDebitCardTransactionFolder):
            shutil.move(sPDebitCardTransactionFolder, sPDebitReceiptFolder)

        if os.path.exists(sPDebitCashTransactionFolder):
            shutil.move(sPDebitCashTransactionFolder, sPDebitReceiptFolder)

        # Moving SadaPay Receipts into SadaPay Folder
        if os.path.exists(sPCreditReceiptFolder):
            shutil.move(sPCreditReceiptFolder, sadaPayReceiptsFolder)

        if os.path.exists(sPDebitReceiptFolder):
            shutil.move(sPDebitReceiptFolder, sadaPayReceiptsFolder)


        # Moving Standard Chartered Bank Credit Receipts into Standard Chartered Bank Credit Receipts Folder
        if os.path.exists(sCBCreditAppTransactionFolder):
            shutil.move(sCBCreditAppTransactionFolder, sCBCreditReceiptFolder)

        if os.path.exists(sCBCreditCardTransactionFolder):
            shutil.move(sCBCreditCardTransactionFolder, sCBCreditReceiptFolder)

        if os.path.exists(sCBCreditCashTransactionFolder):
            shutil.move(sCBCreditCashTransactionFolder, sCBCreditReceiptFolder)

        # Moving Standard Chartered Bank Debit Receipts into Standard Chartered Bank Debit Receipts Folder
        if os.path.exists(sCBDebitAppTransactionFolder):
            shutil.move(sCBDebitAppTransactionFolder, sCBDebitReceiptFolder)

        if os.path.exists(sCBDebitCardTransactionFolder):
            shutil.move(sCBDebitCardTransactionFolder, sCBDebitReceiptFolder)

        if os.path.exists(sCBDebitCashTransactionFolder):
            shutil.move(sCBDebitCashTransactionFolder, sCBDebitReceiptFolder)

        # Moving Standard Chartered Bank Receipts into Standard Chartered Bank Folder
        if os.path.exists(sCBCreditCardEStatementFolder):
            shutil.move(sCBCreditCardEStatementFolder, standardCharteredBankReceiptsFolder)
        if os.path.exists(sCBCreditReceiptFolder):
            shutil.move(sCBCreditReceiptFolder, standardCharteredBankReceiptsFolder)
        if os.path.exists(sCBDebitCardEStatementFolder):
            shutil.move(sCBDebitCardEStatementFolder, standardCharteredBankReceiptsFolder)
        if os.path.exists(sCBDebitReceiptFolder):
            shutil.move(sCBDebitReceiptFolder, standardCharteredBankReceiptsFolder)


        # Moving Upaisa Credit Receipts into Upaisa Credit Receipts Folder
        if os.path.exists(uPCreditAppTransactionFolder):
            shutil.move(uPCreditAppTransactionFolder, uPCreditReceiptFolder)

        if os.path.exists(uPCreditCardTransactionFolder):
            shutil.move(uPCreditCardTransactionFolder, uPCreditReceiptFolder)

        if os.path.exists(uPCreditCashTransactionFolder):
            shutil.move(uPCreditCashTransactionFolder, uPCreditReceiptFolder)

        # Moving Upaisa Debit Receipts into Upaisa Debit Receipts Folder
        if os.path.exists(uPDebitAppTransactionFolder):
            shutil.move(uPDebitAppTransactionFolder, uPDebitReceiptFolder)

        if os.path.exists(uPDebitCardTransactionFolder):
            shutil.move(uPDebitCardTransactionFolder, uPDebitReceiptFolder)

        if os.path.exists(uPDebitCashTransactionFolder):
            shutil.move(uPDebitCashTransactionFolder, uPDebitReceiptFolder)

        # Moving Upaisa Receipts into Upaisa Folder
        if os.path.exists(uPCreditReceiptFolder):
            shutil.move(uPCreditReceiptFolder, uPaisaReceiptsFolder)

        if os.path.exists(uPDebitReceiptFolder):
            shutil.move(uPDebitReceiptFolder, uPaisaReceiptsFolder)


        # Moving Zindigi Credit Receipts into Zindigi Credit Receipts Folder
        if os.path.exists(zICreditAppTransactionFolder):
            shutil.move(zICreditAppTransactionFolder, zICreditReceiptFolder)

        if os.path.exists(zICreditCardTransactionFolder):
            shutil.move(zICreditCardTransactionFolder, zICreditReceiptFolder)

        if os.path.exists(zICreditCashTransactionFolder):
            shutil.move(zICreditCashTransactionFolder, zICreditReceiptFolder)

        # Moving Zindigi Debit Receipts into Zindigi Debit Receipts Folder
        if os.path.exists(zIDebitAppTransactionFolder):
            shutil.move(zIDebitAppTransactionFolder, zIDebitReceiptFolder)

        if os.path.exists(zIDebitCardTransactionFolder):
            shutil.move(zIDebitCardTransactionFolder, zIDebitReceiptFolder)

        if os.path.exists(zIDebitCashTransactionFolder):
            shutil.move(zIDebitCashTransactionFolder, zIDebitReceiptFolder)

        # Moving Zindigi Receipts into Zindigi Folder
        if os.path.exists(zICreditReceiptFolder):
            shutil.move(zICreditReceiptFolder, zindigiReceiptsFolder)

        if os.path.exists(zIDebitReceiptFolder):
            shutil.move(zIDebitReceiptFolder, zindigiReceiptsFolder)


        # Moving kTrade Dividend Statement & kTrade E Statement & KTrade Trade Confirmation into kTrade Receipts Folder
        if os.path.exists(kTradeDividendStatementFolder):
            shutil.move(kTradeDividendStatementFolder, kTradeReceiptFolder)

        if os.path.exists(kTradeEStatementFolder):
            shutil.move(kTradeEStatementFolder, kTradeReceiptFolder)

        if os.path.exists(kTradeTradeConfirmationFolder):
            shutil.move(kTradeTradeConfirmationFolder, kTradeReceiptFolder)

        # Moving kTrade Receipts & CGT Receipts & CDC Receipts into Trading Receipts Folder
        if os.path.exists(kTradeReceiptFolder):
            shutil.move(kTradeReceiptFolder, tradingReceiptsFolder)

        if os.path.exists(cGTReceiptFolder):
            shutil.move(cGTReceiptFolder, tradingReceiptsFolder)

        if os.path.exists(cDCReceiptFolder):
            shutil.move(cDCReceiptFolder, tradingReceiptsFolder)



        # Moving All Bank Folders into Account Receipts Folder
        if os.path.exists(alliedBankReceiptsFolder):
            shutil.move(alliedBankReceiptsFolder, accountReceiptsFolder)
        if os.path.exists(bankAlfalahReceiptsFolder):
            shutil.move(bankAlfalahReceiptsFolder, accountReceiptsFolder)
        if os.path.exists(easyPaissaReceiptsFolder):
            shutil.move(easyPaissaReceiptsFolder, accountReceiptsFolder)
        if os.path.exists(firstPayReceiptsFolder):
            shutil.move(firstPayReceiptsFolder, accountReceiptsFolder)
        if os.path.exists(jazzCashReceiptsFolder):
            shutil.move(jazzCashReceiptsFolder, accountReceiptsFolder)
        if os.path.exists(mashreqReceiptsFolder):
            shutil.move(mashreqReceiptsFolder, accountReceiptsFolder)
        if os.path.exists(meezanBankReceiptsFolder):
            shutil.move(meezanBankReceiptsFolder, accountReceiptsFolder)
        if os.path.exists(nayaPayReceiptsFolder):
            shutil.move(nayaPayReceiptsFolder, accountReceiptsFolder)
        if os.path.exists(sadaPayReceiptsFolder):
            shutil.move(sadaPayReceiptsFolder, accountReceiptsFolder)
        if os.path.exists(standardCharteredBankReceiptsFolder):
            shutil.move(standardCharteredBankReceiptsFolder, accountReceiptsFolder)
        if os.path.exists(uPaisaReceiptsFolder):
            shutil.move(uPaisaReceiptsFolder, accountReceiptsFolder)
        if os.path.exists(zindigiReceiptsFolder):
            shutil.move(zindigiReceiptsFolder, accountReceiptsFolder)
        if os.path.exists(tradingReceiptsFolder):
            shutil.move(tradingReceiptsFolder, accountReceiptsFolder)


        # Moving Gym Receipts Folder into Market Receipts Folder
        if os.path.exists(gymReceiptsFolder):
            shutil.move(gymReceiptsFolder, marketReceiptsFolder)

        if os.path.exists(accountReceiptsFolder):
            print(f"Move {accountReceiptsFolder} Folder in {monthReceiptsFolder} Folder")
            shutil.move(accountReceiptsFolder, monthReceiptsFolder)
        if os.path.exists(marketReceiptsFolder):
            print(f"Move {marketReceiptsFolder} Folder in {monthReceiptsFolder} Folder")
            shutil.move(marketReceiptsFolder, monthReceiptsFolder)

        if os.path.exists(monthReceiptsFolder):
            print(f"Move {monthReceiptsFolder} Folder in {dest_folder} Folder\n")
            shutil.move(monthReceiptsFolder, dest_folder)

    return dest_folder

