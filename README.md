# BudgetTracking

## Summary
This is a Python project to ingest bank and credit card statements into a database. From there data can be manipulated into reports to identify personal spending habits.


## Setup

The tech stack in use is Python with a MariaDB backend. You will need to supply your own DB instance. 

A local config.json file should be created within the project to match the format below. Include as many sources as required. Update the database connection information to match your setup

    {
        "sources": [
            {
                "name": "BANK",
                "folder": "sources/BANK",
                "file_pattern": "*.csv"
            },
            {
                "name": "CREDIT_CARD1",
                "folder": "sources/CREDIT_CARD1",
                "file_pattern": "*.csv"
            }
        ],
        "database": {
            "host": "DB_HOST",
            "port": DB_PORT,
            "database": "DB_NAME",
            "username": "USER_NAME",
            "password": "USER_PASSWORD"
        }
    }
