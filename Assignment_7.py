import re

# Text containing different types of email addresses
message = """
Welcome to our college portal.

For any queries, email us:
admin@university.com
rahul_2026@gmail.com
contact@department.org
wrongmail@domain
info@college.ac.in

Have a nice day!
"""

# Pattern used to identify valid email addresses
pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

# Extract email addresses from the given message
found_emails = re.findall(pattern, message)

# Print the extracted email addresses
print("Valid email addresses:")

for address in found_emails:
    print("-", address)

print("\nTotal valid emails:", len(found_emails))

#coments
Output:

Valid email addresses:
- admin@university.com
- rahul_2026@gmail.com
- contact@department.org
- info@college.ac.in

Total valid emails: 4