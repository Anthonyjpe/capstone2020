"""
Errors for retrieving a docket using regulation.gov api
"""


class IncorrectApiKeyException(Exception):
    """
    Thrown exception for an incorrectly entered reg gov api key
    """


class ExceedCallLimitException(Exception):
    """
    Thrown exception for overuse of a reg gov api key
    """


class BadDocIDException(Exception):
    """
    Thrown exception for a docket id that does not exist
    """


class IncorrectIDPatternException(Exception):
    """
    Thrown exception for a incorrect docket id pattern
    """
