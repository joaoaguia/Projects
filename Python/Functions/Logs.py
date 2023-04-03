#********************************************************
#Program:       Logs
#Description:   This code is a function that sets up a logger for a project. It takes in an optional parameter "project_name" which will be used as the name of the 
#               log file and the log directory. If project_name is not provided, the function uses the name of the current script as the project name. 
#               The function creates the log directory if it does not exist and sets up the logger to write log messages to a file in that directory. 
#               The log file name is in the format of "project_name_current_date.log" and the function also deletes log files older than 31 days. 
#               The function also defines the format of the log messages and sets the logger's level to "INFO". The function returns the logger object for the project.
#********************************************************

#Libraries

import os
import logging
from datetime import datetime, timedelta

def setup_logger(project_name=None):
    # Define the log directory
    log_dir = (os.path.expanduser("~/Documents/Python_Project_Files/Logs"))

    # If a project name is not provided, use the current script name
    if project_name is None:
        raise ValueError("The project_name parameter is required")

    # Create the project log directory if it does not exist
    project_log_dir = os.path.join(log_dir, project_name)
    if not os.path.exists(project_log_dir):
        os.makedirs(project_log_dir)

    # Define the log file name
    log_file = f"{project_name}_{datetime.now().strftime('%Y-%m-%d')}.log"
    log_file_path = os.path.join(project_log_dir, log_file)

    # Delete old log files (more than 31 days old)
    if os.path.exists(project_log_dir) and len(os.listdir(project_log_dir)) > 0:
        for file in os.listdir(project_log_dir):
            file_path = os.path.join(project_log_dir, file)
            if os.path.isfile(file_path):
                file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                if (datetime.now() - file_creation_time) > timedelta(days=31):
                    os.remove(file_path)
        
    # Configure the logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s:%(funcName)s - %(message)s')
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger