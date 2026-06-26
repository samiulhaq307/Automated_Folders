import sys
import os
import unittest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_scripts_automation.budget_folder_manager import BudgetFolderManager
from python_scripts_automation.Constants import Constants

class TestBudgetFolderManager(unittest.TestCase):
    def setUp(self):
        # Mocking logger to avoid issues during tests
        with patch('python_scripts_automation.budget_folder_manager.logger'):
            self.manager = BudgetFolderManager("2026")

    @patch('python_scripts_automation.budget_folder_manager.FileSystemManager')
    @patch('python_scripts_automation.budget_folder_manager.logger')
    def test_create_named_subfolder(self, mock_logger, mock_fsm):
        folder = BudgetFolderManager.create_named_subfolder("Test", "Jan", "2026")
        self.assertEqual(folder, "Test Jan 2026")
        mock_fsm.ensure_directory_exists.assert_called_with("Test Jan 2026")

    @patch('python_scripts_automation.budget_folder_manager.FileSystemManager')
    @patch('python_scripts_automation.budget_folder_manager.logger')
    def test_create_bank_receipts_folder(self, mock_logger, mock_fsm):
        folder = self.manager.create_bank_receipts_folder("Bank", "January")
        self.assertEqual(folder, f"Bank {Constants.RECEIPTS} January 2026")
        mock_fsm.ensure_directory_exists.assert_called()

    @patch('python_scripts_automation.budget_folder_manager.FileSystemManager')
    @patch('python_scripts_automation.budget_folder_manager.logger')
    def test_setup_bank_folders(self, mock_logger, mock_fsm):
        # We need to mock create_named_subfolder as well, but it's a static method on the class.
        # Patch it on the class.
        with patch('python_scripts_automation.budget_folder_manager.BudgetFolderManager.create_named_subfolder', return_value="dummy_path"):
            self.manager.setup_bank_folders("AB", "bank_receipts", "Jan")
            # Verify that FileSystemManager.move_folder_if_exists was called
            self.assertTrue(mock_fsm.move_folder_if_exists.called)

if __name__ == '__main__':
    unittest.main()
