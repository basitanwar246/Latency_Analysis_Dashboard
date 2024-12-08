import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote
from datetime import datetime, timedelta
import logging

# Set up logging
log_file = "latency_dashboard.log"
debug_file = r"C:\Users\user_name\dashboard\fetched_data.txt"  # Update this to a writable location
logging.basicConfig(
    filename=log_file,
    filemode="a",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")

# Global DataFrame to cache the fetched data
global_cached_data = pd.DataFrame()

# Database connection using SQLAlchemy
def get_database_connection():
    try:
        user = "your_username" # Replace with your UserName
        password = quote("your_password_with_special_characters")
        host = "1.2.0.0" # Replace with your IP
        port = "3306" 
        database = "your_database"
        engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
        logging.info("Database connection established")
        return engine
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")
        raise
