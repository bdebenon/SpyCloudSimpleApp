from json import loads

from app.api import send_get_request_with_params_dict
from app.helpers.exceptions import ApiError
from app.helpers.passwords import decrypt_password

SPY_CLOUD_API_URL = "https://api.spycloud.io/enterprise-v2/breach"
SPY_CLOUD_API_KEY = "0IHk1ugJfJ9dloPhcrtvMTuk6fubEtV5OQKuyaRe"


def credentials_compromised(email, password):  # Returns True if credentials are compromised
    endpoint = f"{SPY_CLOUD_API_URL}/data/emails/{email}"

    check_next_page = True  # in-case cursors are needed
    while check_next_page:
        get_params = {}  # TODO: Implement cursors for cases w/ over 1000 results
        response = send_get_request_with_params_dict(endpoint=endpoint, params=get_params, api_key=SPY_CLOUD_API_KEY)

        # Check for 200 status code
        if response.status_code != 200:
            raise ApiError("Failure when calling SpyCloud API")

        # Search through results for current password
        response_dict = loads(response.content)
        results_list = response_dict['results']

        # Saved hashed passwords to reduce computation time
        hashed_passwords = {}
        for entry in results_list:
            # Check plaintext first
            if 'password_plaintext' in entry and entry['password_plaintext'] == password:
                return True

            # If no plaintext, encrypt user password if needed
            if 'password' in entry:
                if 'password_type' in entry:
                    password_type = entry['password_type']
                    if password_type in hashed_passwords:
                        encrypted_pass = hashed_passwords[password_type]
                    else:
                        encrypted_pass = decrypt_password(password, password_type)
                        hashed_passwords[password_type] = encrypted_pass

                # Check if entry_pass from API matches user's encrypted_pass
                entry_pass = entry["password"]
                if entry_pass == encrypted_pass:
                    return True

        # Set to false if no cursor exists
        # TODO: Finish this functionality once we get test case w/ cursors
        check_next_page = False

    return False


if __name__ == "__main__":
    _email = "test@example.org"
    _email = "blake_debenon@occuply.io"
    _password = "example123"
    _result = credentials_compromised(_email, _password)
    print(_result)
