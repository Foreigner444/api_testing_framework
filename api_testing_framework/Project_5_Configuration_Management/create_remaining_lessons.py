#!/usr/bin/env python3
"""Generate remaining lesson files for Project 5"""

from pathlib import Path

# Define all remaining lessons (5.7 through 5.36)
lessons = [
    ("5.7", "Loading_Environment_Variables"),
    ("5.8", "Environment_Specific_env_Files"),
    ("5.9", "env_local_dev_staging_prod"),
    ("5.10", "gitignore_for_Secret_Management"),
    ("5.11", "Introduction_to_pydantic_settings"),
    ("5.12", "BaseSettings_Configuration_Class"),
    ("5.13", "Automatic_env_Loading"),
    ("5.14", "Field_Validation_in_Settings"),
    ("5.15", "Nested_Settings_Models"),
    ("5.16", "Settings_with_Multiple_Sources"),
    ("5.17", "YAML_Configuration_Files"),
    ("5.18", "JSON_Configuration_Files"),
    ("5.19", "TOML_Configuration_Files"),
    ("5.20", "Combining_YAML_and_env"),
    ("5.21", "Environment_Variable_Precedence"),
    ("5.22", "Dynamic_Configuration_Loading"),
    ("5.23", "Configuration_Validation_on_Startup"),
    ("5.24", "Creating_Config_Fixtures"),
    ("5.25", "Environment_Switching_in_Tests"),
    ("5.26", "httpx_Client_Configuration_per_Environment"),
    ("5.27", "Base_URL_Configuration"),
    ("5.28", "Timeout_Configuration_per_Environment"),
    ("5.29", "Authentication_Configuration"),
    ("5.30", "Secrets_and_API_Keys_Management"),
    ("5.31", "Database_Connection_Strings"),
    ("5.32", "Feature_Flags_and_Toggles"),
    ("5.33", "Configuration_for_CI_CD"),
    ("5.34", "Docker_Environment_Variables"),
    ("5.35", "Configuration_Testing_Strategies"),
    ("5.36", "Best_Practices_for_Configuration"),
]

for number, title in lessons:
    filename = f"{number}_{title}.md"
    print(f"{filename}")

print(f"\nTotal: {len(lessons)} lessons")
