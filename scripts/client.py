import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
from dotenv import load_dotenv

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

load_dotenv("../")

# Configure HTTP basic authorization: Basic
configuration = openapi_client.Configuration(
    username = os.getenv("USERNAME"),
    password = os.getenv("PASSWORD")
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApiApi(api_client)

    try:
        api_instance.api_list()
    except ApiException as e:
        print("Exception when calling ApiApi->api_list: %s\n" % e)