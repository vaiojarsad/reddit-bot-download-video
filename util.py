import re
import string
import unicodedata


def create_valid_file_name(a_str: str):
    # Define a regex pattern for invalid characters in file names
    invalid_chars = r'[\/:*?"<>|\\\t\n\r\f\v]'

    # Replace invalid characters with underscore "_"
    valid_name = re.sub(invalid_chars, '_', a_str)

    # Remove leading and trailing whitespaces
    valid_name = valid_name.strip()

    # Remove consecutive underscores
    valid_name = re.sub(r'_+', '_', valid_name)

    # Remove control characters and non-printable characters
    valid_name = ''.join(c for c in valid_name if c in string.printable and not unicodedata.category(c).startswith('C'))

    # Return the resulting valid file name
    return valid_name
