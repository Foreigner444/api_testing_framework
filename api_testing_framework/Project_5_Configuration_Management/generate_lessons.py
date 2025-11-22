#!/usr/bin/env python3
"""
Generate all remaining Project 5 lessons with complete content.
This creates production-ready lesson files following the curriculum structure.
"""

from pathlib import Path
from typing import Dict, List

def generate_lesson_content(number: str, title: str, concept_data: Dict) -> str:
    """Generate full lesson content following the template structure."""
    
    clean_title = title.replace("_", " ")
    
    content = f"""# Lesson {number}: {clean_title}

## A. Concept Overview

### What & Why
{concept_data['what_why']}

### Analogy
{concept_data['analogy']}

---

## B. Code Implementation

{concept_data['code_section']}

---

## C. Connect & Apply

### How to Test It

{concept_data['testing']}

### Expected Result

{concept_data['expected_result']}

---

## D. Common Stumbling Blocks

{concept_data['stumbling_blocks']}

---

## 🎯 Key Takeaways

{concept_data['key_takeaways']}

---

## What's Next?

{concept_data['whats_next']}

**Ready to continue?** 🚀
"""
    return content

# For now, just list what needs to be created
lessons_to_create = [
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

print("Lessons to create:")
for num, title in lessons_to_create:
    print(f"  {num}_{title}.md")
print(f"\nTotal: {len(lessons_to_create)} lessons")

