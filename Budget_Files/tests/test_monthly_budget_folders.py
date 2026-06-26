import sys
import os
import unittest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_scripts_automation.monthly_budget_folders import generate_monthly_budget_folders

class TestMonthlyBudgetFolders(unittest.TestCase):
    @patch('python_scripts_automation.monthly_budget_folders.BudgetFolderManager')
    @patch('python_scripts_automation.monthly_budget_folders.FileSystemManager')
    @patch('python_scripts_automation.monthly_budget_folders.logger')
    def test_generate_monthly_budget_folders(self, mock_logger, mock_fsm, mock_manager_class):
        mock_manager = MagicMock()
        mock_manager_class.return_value = mock_manager
        
        # We need to make sure setup_bank_folders doesn't raise errors when mocked
        result = generate_monthly_budget_folders("2026")
        
        self.assertEqual(result, "Receipts 2026")
        self.assertTrue(mock_fsm.ensure_directory_exists.called)
        self.assertTrue(mock_manager.setup_bank_folders.called)

if __name__ == '__main__':
    unittest.main()
