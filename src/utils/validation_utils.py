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
    def
