# main.py
import streamlit as st
from datetime import datetime
from gui.main_dashboard import launch
from app.admin_utils import init_logger, backup_data

def main():
    """Entry point for the Music School Management System application."""
    
    # Initialize the logger as the very first step.
    init_logger("data/msms.log")

    # Perform a data backup before starting the application session.
    backup_success = backup_data("data/msms.json", "data/backups")
    if backup_success:
        print("Data backup successful!")
    else:
        print("Data backup failed. Check logs for details.")

    # Launch the GUI dashboard
    st.set_page_config(layout="wide", page_title="Music School Management System")

    # Sidebar Button for Manual Backup
    st.sidebar.title("Admin Tools")
    if st.sidebar.button("Backup Data Now", key="siderbar_backup"):
        success = backup_data("data/msms.json", "data/backups")
        if success:
            st.sidebar.success("Data backup completed successfully!")
        else:
            st.sidebar.error("Data backup failed. Check logs for details.")
            
    # Launch the main dashboard
    launch()
    st.sidebar.caption(f"Last backup: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Run the application
if __name__ == "__main__":
    main()