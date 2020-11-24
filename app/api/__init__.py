import requests


def send_get_request_with_params_dict(endpoint, params, api_key=None):
    # Build HTTP Url
    url = f'{endpoint}'

    # Create dict to be added to database
    params_dict = params

    # Need an API key?
    if api_key:
        headers = {"X-Api-Key": api_key}
    else:
        headers = {}

    # Sending get request and saving the response as response object
    response = requests.get(url=url, params=params_dict, headers=headers)

    return response
