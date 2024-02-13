"""
Follow below link to get started:
https://coddy.tech/courses/email_validator_using_python/introduction
"""


# Coddy Email Validator 1/8
"""
Welcome Page
"""


# Coddy Email Validator 2/8
"""
# '@' symbol

def validate(s):
    if s.count('@') == 1:
        return True
    return False
"""


# Coddy Email Validator 3/8
"""
# Recipient name

def validate(s):
    if s.count('@') == 1:
        idx_at = s.index("@")
    special = ['.', '_']
    recipient = s[:idx_at]
    if len(recipient) <= 24 and len(recipient) >= 3 and recipient[0] not in special and recipient[-1] not in special:
        for i in recipient:
            if not (i.isalpha() or i.isdigit() or i in special):
                return False
        return True
    return False
"""


# Coddy Email Validator 4/8
"""
# Domain name

import re 

def validate(email):

  if email.count('@') != 1:
    return False

  user, domain = email.split('@')

  if not (3 <= len(user) <= 12):
    return False

  if not re.match(r'[A-Za-z0-9.-]+', user):
    return False

  domain_name = domain.split('.')[0]

  if not (3 <= len(domain_name) <= 12):
    return False

  if not re.match(r'[A-Za-z0-9.-]+', domain_name):
    return False

  return True

print(validate('bobby@a+.tech'))
"""


# Coddy Email Validator 5/8
"""
# Top-level domain

import re

email_regex = r'\b[A-Za-z0-9._%+-]{3,12}@[A-Za-z0-9-]{3,12}\.[A-Z|a-z]{2,4}\b'
allowed_tlds = ['com', 'tech', 'org', 'net']

def validate(email):
    if not re.fullmatch(email_regex, email):
        return False

    at_index = email.index("@")
    domain = email[at_index+1:]

    if len(domain) > 15:
        return False

    domain_parts = domain.split(".")
    if len(domain_parts) != 2:
        return False

    recipient, top_level_domain = domain_parts

    if not (3 <= len(recipient) <= 12):
        return False

    if not re.fullmatch(r'[A-Za-z0-9-]+', recipient):
        return False

    if len(top_level_domain) > 4: 
        return False
    if top_level_domain not in allowed_tlds:
        return False

    return True
"""


# Coddy Email Validator 6/8
"""
# Call validate

import re

email_regex = r'\b[A-Za-z0-9._%+-]{3,12}@[A-Za-z0-9-]{3,12}\.[A-Z|a-z]{2,4}\b'
allowed_tlds = ['com', 'tech', 'org', 'net']

def validate(email):
    if not re.fullmatch(email_regex, email):
        return False

    at_index = email.index("@")
    domain = email[at_index+1:]

    if len(domain) > 15:
        return False

    domain_parts = domain.split(".")
    if len(domain_parts) != 2:
        return False

    recipient, top_level_domain = domain_parts

    if not (3 <= len(recipient) <= 12):
        return False

    if not re.fullmatch(r'[A-Za-z0-9-]+', recipient):
        return False

    if len(top_level_domain) > 4: 
        return False
    if top_level_domain not in allowed_tlds:
        return False

    return True


if __name__ == "__main__":
    # write code here
    email = input()
    print(validate(email))
"""


# Coddy Email Validator 7/8
"""
# Last additions

import re

email_regex = r'\b[A-Za-z0-9._%+-]{3,12}@[A-Za-z0-9-]{3,12}\.[A-Z|a-z]{2,4}\b'
allowed_tlds = ['com', 'tech', 'org', 'net']

def validate(email):
    if not re.fullmatch(email_regex, email):
        return "Email is invalid"

    at_index = email.index("@")
    domain = email[at_index+1:]

    if len(domain) > 15:
        return "Email is invalid"

    domain_parts = domain.split(".")
    if len(domain_parts) != 2:
        return "Email is invalid"

    recipient, top_level_domain = domain_parts

    if not (3 <= len(recipient) <= 12):
        return "Email is invalid"

    if not re.fullmatch(r'[A-Za-z0-9-]+', recipient):
        return "Email is invalid"

    if len(top_level_domain) > 4: 
        return "Email is invalid"
    if top_level_domain not in allowed_tlds:
        return "Email is invalid"

    return "Email is valid"


if __name__ == "__main__":
    # write code here
    print("Enter email:")
    email = input()
    print(validate(email))
"""


# Coddy Email Validator 8/8
"""
Final words
"""


"""
This can act as a solid outline for your own email validator program, as the folks at coddy have quite made an easier constrained version of the problem. Tweak things here and there to get a more rigid validator.
"""