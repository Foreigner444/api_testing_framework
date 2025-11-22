#!/usr/bin/env python3
"""
Generate remaining 20 lessons (6.4-6.23) for Project 6.
Each lesson will have comprehensive content following the template.
"""

remaining_lessons = [
    ("6.4", "API_Keys_from_Configuration"),
    ("6.5", "Bearer_Token_Authentication"),
    ("6.6", "Basic_Authentication_with_httpx"),
    ("6.7", "Custom_Auth_Classes_in_httpx"),
    ("6.8", "Introduction_to_OAuth_2.0"),
    ("6.9", "Testing_OAuth_Flows_with_httpx"),
    ("6.10", "OAuth_Configuration_per_Environment"),
    ("6.11", "JWT_Tokens_Explained"),
    ("6.12", "Decoding_and_Validating_JWT"),
    ("6.13", "Pydantic_Models_for_JWT_Claims"),
    ("6.14", "Session_Based_Authentication"),
    ("6.15", "Cookie_Authentication_with_httpx"),
    ("6.16", "httpx_Cookies_and_Cookie_Jars"),
    ("6.17", "Testing_Authorization_Roles"),
    ("6.18", "Permission_Based_Testing"),
    ("6.19", "Security_Testing_Basics"),
    ("6.20", "Rate_Limiting_Tests_with_httpx"),
    ("6.21", "Token_Expiration_and_Refresh"),
    ("6.22", "Faker_for_Auth_Test_Data"),
    ("6.23", "Best_Practices_for_Auth_Testing"),
]

print(f"Creating {len(remaining_lessons)} comprehensive lessons for Project 6...")
for num, title in remaining_lessons:
    print(f"  {num}: {title.replace('_', ' ')}")

print(f"\nTotal: {len(remaining_lessons)} lessons to create")
print("Will use write tool for comprehensive content creation...")

