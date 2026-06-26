import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Add Budget_Files to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from python_scripts_automation.file_system_manager import FileSystemManager

class TestFileSystemManager(unittest.TestCase):
    @patch('python_scripts_automation.file_system_manager.os.path.exists')
    @patch('python_scripts_automation.file_system_manager.os.makedirs')
    @patch('python_scripts_automation.file_system_manager.logger')
    def test_ensure_directory_exists_creates_dir(self, mock_logger, mock_makedirs, mock_exists):
        mock_exists.return_value = False
        FileSystemManager.ensure_directory_exists("test_folder")
        mock_makedirs.assert_called_once_with("test_folder")
        mock_logger.info.assert_called()

    @patch('python_scripts_automation.file_system_manager.os.path.exists')
    @patch('python_scripts_automation.file_system_manager.os.makedirs')
    @patch('python_scripts_automation.file_system_manager.logger')
    def test_ensure_directory_exists_skips_if_exists(self, mock_logger, mock_makedirs, mock_exists):
        mock_exists.return_value = True
        FileSystemManager.ensure_directory_exists("test_folder")
        mock_makedirs.assert_not_called()
        mock_logger.debug.assert_called()

    @patch('python_scripts_automation.file_system_manager.os.path.exists')
    @patch('python_scripts_automation.file_system_manager.shutil.move')
    @patch('python_scripts_automation.file_system_manager.logger')
    def test_move_folder_if_exists_moves(self, mock_logger, mock_move, mock_exists):
        mock_exists.return_value = True
        FileSystemManager.move_folder_if_exists("source", "dest")
        mock_move.assert_called_once_with("source", "dest")
        mock_logger.info.assert_called()

    @patch('python_scripts_automation.file_system_manager.os.path.exists')
    @patch('python_scripts_automation.file_system_manager.shutil.move')
    @patch('python_scripts_automation.file_system_manager.logger')
    def test_move_folder_if_exists_skips(self, mock_logger, mock_move, mock_exists):
        mock_exists.return_value = False
        FileSystemManager.move_folder_if_exists("source", "dest")
        mock_move.assert_not_called()
        mock_logger.debug.assert_called()

if __name__ == '__main__':
    unittest.main()
