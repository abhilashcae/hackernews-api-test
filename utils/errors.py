class Errors:
    """
    Contains methods having error message strings.
    Created this class to shorten long line of code in which these error messages are invoked.
    """

    @staticmethod
    def invalid_response_code(response, url, expected_response_code):
        return f'\n\n Got invalid response code {response.status_code} \n\n Response content: {response.content} \n\n For url: {url} \n\n Expected response code: {expected_response_code}'
