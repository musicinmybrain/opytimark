import opytimark.utils.logging as l

logger = l.get_logger(__name__)


class Error(Exception):
    """A generic Error class derived from Exception.

    Essentially, it gets the class and message and logs the error to the logger.

    """

    def __init__(self, cls, msg):
        """Initialization method.

        Args:
            cls (str): Class identifier.
            msg (str): Message to be logged.
        """

        # Logs the error in a formatted way
        logger.error(f'{cls}: {msg}.')


class SizeError(Error):
    """A SizeError class for logging errors related to wrong length or size of variables.

    """

    def __init__(self, error):
        """Initialization method.

        Args:
            error (str): Error message to be logged.

        """

        # Override its parent class with class name and error message
        super(SizeError, self).__init__('SizeError', error)