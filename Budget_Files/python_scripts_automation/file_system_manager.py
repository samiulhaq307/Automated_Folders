import os
import shutil
import logging
from python_scripts_automation.Constants import Constants

logger = logging.getLogger(__name__)

class FileSystemManager:
    @staticmethod
    def ensure_directory_exists(folder_path):
        if not os.path.exists(folder_path):
            logger.info(f"{Constants.CREATING} {Constants.FOLDER}: {folder_path}")
            os.makedirs(folder_path)
        else:
            logger.debug(f"{Constants.FOLDER} {Constants.ALREADY} {Constants.EXISTS}: {folder_path}")

    @staticmethod
    def move_folder_if_exists(source, destination, log_message=None):
        if os.path.exists(source):
            if log_message is not False:
                logger.info(log_message or f"{Constants.MOVE} {source} {Constants.IN} {destination}")
            shutil.move(source, destination)
        else:
            logger.debug(f"{Constants.SOURCE} {Constants.NOT} {Constants.FOUND}, {Constants.SKIPPING} {Constants.MOVE}: {source}")
