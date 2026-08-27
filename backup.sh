#!/bin/bash

# Define the paths
DB_SOURCE="main_files/instance/fx_master.db"
BACKUP_DIR="backup"

# Check if the database exists
if [ -f "$DB_SOURCE" ]; then
    cp "$DB_SOURCE" "$BACKUP_DIR/fx_master_backup_$(date +%F_%H-%M-%S).db"
    echo "Backup completed successfully!"
else
    echo "Error: Database file not found at $DB_SOURCE"
fi
