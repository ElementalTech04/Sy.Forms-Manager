import re


class ValidationUtils:
    @staticmethod
    def is_valid_email(email):
        """
        Validate an email address.
        """
        if not email:
            return False
        # Regular expression for validating an Email
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def is_valid_password(password):
        """
        Validate a password.
        """
        if not password:
            return False
        # Password must be at least 8 characters long, contain at least one uppercase letter,
        # one lowercase letter, one digit, and one special character.
        if len(password) < 8:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char in '!@#$%^&*()-_=+{}[]|:;"/?.>,<`~' for char in password):
            return False
        return True

    @staticmethod
    def is_valid_username(username):
        """
        Validate a username.
        """
        if not username:
            return False
        # Username must be between 3 and 20 characters long and can contain only letters, numbers, underscores, and hyphens.
        username_regex = r'^[a-zA-Z0-9_-]{3,20}$'
        return re.match(username_regex, username) is not None

    @staticmethod
    async def field_exists_in_database(pool, table, column, value):
        """
        Check if a value exists in a specific column of a table in the database.
        """
        async with pool.acquire() as connection:
            query = f"SELECT EXISTS(SELECT 1 FROM {table} WHERE {column} = $1)"
            exists = await connection.fetchval(query, value)
            return exists

    @staticmethod
    def check_http_header(header_value, expected_value):
        """
        Check if the HTTP header value matches the expected value.
        """
        return header_value == expected_value
