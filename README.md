# 📁 Budget Folder Automation

A little Python script that does the one thing nobody enjoys doing manually every month: building out a *huge* folder structure to organize bank receipts, e-statements, trading slips, and tax documents.

If you've ever sat there creating "Allied Bank Credit Receipt Jan 2026," "Allied Bank Debit Receipt Jan 2026," "Allied Bank Credit Card Transaction Jan 2026"... and then realized you have 13 banks and 12 months to go — yeah, this is for you. Run one script, get a full year's worth of perfectly nested folders, ready for you to drop your receipts into.

## What it actually does

Give it a year (or a few), and it builds:

- A top-level `Records/Records {year}` folder
- 12 monthly folders inside (`01_Receipts January 2026`, `02_Receipts February 2026`, etc.)
- Inside each month: **Account Receipts** and **Market Receipts** folders
- Inside Account Receipts: a folder for every bank/wallet you use (Allied Bank, Bank Alfalah, EasyPaisa, JazzCash, Meezan Bank, NayaPay, SadaPay, Standard Chartered, UPaisa, Zindigi, Raqami, First Pay, Mashreq) — each split into Credit/Debit Receipts, with App/Card/Cash transaction subfolders and e-statement folders
- A **Trading** folder for KTrade (dividends, e-statements, trade confirmations) plus CDC and CGT receipts
- Inside Market Receipts: a Gym Receipts folder, because apparently gym memberships count as "market" expenses in this system 🤷

It's basically a giant, opinionated filing cabinet that builds itself.

## Project structure

```
.
├── main.py                      # Entry point — asks for years, runs everything
├── Constants.py                 # Every string label, bank name & abbreviation lives here
├── file_system_manager.py       # Low-level folder create/move helpers
├── budget_folder_manager.py     # Builds out the per-bank folder hierarchy
└── monthly_budget_folders.py    # Orchestrates all 12 months for a given year
```

| File | Responsibility |
|---|---|
| `main.py` | Runs your test suite, asks which year(s) you want, wipes any existing folder for that year, then kicks off the build. |
| `monthly_budget_folders.py` | Loops over the 12 months and builds the full monthly structure (banks, trading, market, gym). |
| `budget_folder_manager.py` | The `BudgetFolderManager` class — handles the repetitive "credit/debit/app/card/cash/e-statement" subfolder pattern per bank. |
| `file_system_manager.py` | Dumb-simple, safe wrappers around `os.makedirs` and `shutil.move` that won't blow up if a folder already exists or is missing. |
| `Constants.py` | No magic strings anywhere — every folder label, bank name, and abbreviation is defined once here. |

## Prerequisites

- Python 3.8+
- Nothing else. No `pip install` needed — it's pure standard library (`os`, `shutil`, `unittest`, `logging`).

## Installation

```bash
git clone <your-repo-url>
cd <repo-folder>
```

That's it. No virtual environment, no dependencies, no drama.

## Usage

```bash
python main.py
```

It'll first run your test suite (found in a `tests/` folder — make sure that exists, or this will fail at step one). Then it'll ask:

```
Enter the years you want to generate folders for (separated by comma, e.g. 2025, 2026):
```

Type something like:

```
2025, 2026
```

...and walk away. When it's done, you'll have:

```
Records/
├── Records 2025/
│   └── Receipts 2025/
│       ├── 01_Receipts January 2025/
│       ├── 02_Receipts February 2025/
│       └── ...
└── Records 2026/
    └── Receipts 2026/
        └── ...
```

And one month, zoomed in, looks roughly like:

```
01_Receipts January 2026/
├── Account Receipts January 2026/
│   ├── Allied Bank Receipts January 2026/
│   │   ├── AB Credit Receipt Jan 2026/
│   │   └── AB Debit Receipt Jan 2026/
│   ├── Bank Alfalah Receipts January 2026/
│   │   ├── BA Credit Receipt Jan 2026/
│   │   ├── BA Debit Receipt Jan 2026/
│   │   └── BA Orbit Statement Jan 2026/   ← only Bank Alfalah gets this one
│   ├── JazzCash Receipts January 2026/
│   ├── ... (every other bank/wallet) ...
│   └── Trading Receipts January 2026/
│       ├── KTrade Receipt Jan 2026/
│       ├── CGT Receipt Jan 2026/
│       └── CDC Receipt Jan 2026/
└── Market Receipts January 2026/
    └── Gym Receipts January 2026/
```

## ⚠️ Heads up before you run it

If a `Records/Records {year}` folder **already exists**, `main.py` deletes it (`shutil.rmtree`) before rebuilding. No confirmation prompt, no recycle bin, no undo. If you've already dropped a bunch of receipts into last year's folders, **back them up first** — this script doesn't ask twice.

## Customizing it for your own banks

Everything lives in `Constants.py`, so adding a new bank or wallet is copy-paste-and-rename:

1. Add the full name, e.g. `Constants.MY_NEW_BANK = "My New Bank"`
2. Add an abbreviation, e.g. `Constants.MY_NEW_BANK_ABBREVIATION = "MNB"`
3. In `monthly_budget_folders.py`, add a `manager.create_bank_receipts_folder(...)` call and a matching `manager.setup_bank_folders(...)` call, same pattern as the existing banks.
4. If it needs a special folder type (like Bank Alfalah's "Orbit Statement"), pass `has_orbit=True` or extend `setup_bank_folders` with your own flag.

No need to touch the core logic in `budget_folder_manager.py` unless you're adding a genuinely new *category* of subfolder.

## Testing

`main.py` automatically discovers and runs everything in a `tests/` directory before doing any folder work, and exits if anything fails — so you don't accidentally build a broken structure. Add your test cases there using standard `unittest` conventions.

## Why this exists

Because manually creating ~300+ folders every year for receipts, e-statements, and trading slips is the kind of task that makes you question your life choices. This script questions them for you, then fixes the problem in about two seconds.

## License

Add whatever license you'd like here (MIT is a solid default if you're not sure).