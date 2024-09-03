import os
from pprint import pprint
import requests

import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

CLIENT_ID = os.getenv("FLORIDAY_CLIENT_ID")
CLIENT_SECRET = os.getenv("FLORIDAY_CLIENT_SECRET")
API_KEY = os.getenv("FLORIDAY_API_KEY")
AUTH_URL = os.getenv("FLORIDAY_AUTH_URL")
BASE_URL = os.getenv("FLORIDAY_BASE_URL")

payload = {
    "grant_type": "client_credentials",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "scope": "role:app catalog:read sales-order:write organization:read supply:read supply:write sales-order:read delivery-conditions:read fulfillment:write fulfillment:read",
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
}


def get_access_token():
    response = requests.request("POST", AUTH_URL, headers=headers, data=payload)
    response.raise_for_status()
    return response.json().get("access_token")


if __name__ == "__main__":
    access_token = get_access_token()
    print(access_token)
    # Configure API key authorization: JWT Token
    configuration = swagger_client.Configuration()
    configuration.api_key["Authorization"] = access_token
    configuration.api_key_prefix["Authorization"] = "Bearer"
    configuration = swagger_client.Configuration()
    configuration.api_key["X-Api-Key"] = API_KEY

    # create an instance of the API class
    api_instance = swagger_client.AdditionalServicesApi(
        swagger_client.ApiClient(configuration)
    )
    additional_service_id = "38400000-8cf0-11bd-b23e-10b96e4ef00d"  # str |

    try:
        # catalog:read - Returns an additional service.
        api_response = api_instance.get_additional_service_by_id(additional_service_id)
        pprint(api_response)
    except ApiException as e:
        print(
            "Exception when calling AdditionalServicesApi->get_additional_service_by_id: %s\n"
            % e
        )
