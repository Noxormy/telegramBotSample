import functools
import logging

logger = logging.getLogger("common")


def admins_only(func):
    """
        First argument should be chat_id in wrapped function
    """
    @functools.wraps(func)
    def wrapped_func(self, *args, **kwargs):
        chat_id = args[0]
        if chat_id in self.admins:
            return func(self, *args, **kwargs)
        else:
            logger.info(
                "You can't use function [{}] without admin rights, chat_id: [{}]".format(func.__name__, chat_id))
            return False

    return wrapped_func


def for_users_with_data(collection, default_data):
    """
        First argument should be chat_id in wrapped function
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapped_func(self, *args, **kwargs):
            chat_id = args[0]
            doc_ref = collection.document(str(chat_id))
            doc = doc_ref.get()
            if not doc.exists:
                doc_ref.set(default_data)

            return func(self, doc_ref, *args, **kwargs)
        return wrapped_func
    return decorator
