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
