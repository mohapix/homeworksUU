class CleanUp(object):

    class Cancel(Exception):
        pass

    def __init__(self, f_cleanup):
        self.f_cleanup = f_cleanup

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):

        cancelled = exception_type and issubclass(exception_type, self.__class__.Cancel)

        if not cancelled:
            self.f_cleanup()

        return not exception_type or cancelled

    def cancel(self):
        raise self.__class__.Cancel


def cleanup():
    print("Doing housekeeping")


x = 3

with CleanUp(cleanup) as manager:
    if x == 1:
        pass
    elif x == 2:
        pass
    else:
        manager.cancel()
