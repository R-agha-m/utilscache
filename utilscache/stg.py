from os import environ


class Setting:
    _debug_mode = None
    _report = None
    _time_out = None
    _poll_frequency = None

    @property
    def DEBUG_MODE(self):
        if self._debug_mode is None:
            from utils_common.detect_boolean import detect_boolean
            self._debug_mode = detect_boolean(
                environ.get("DEBUG_MODE",
                            True))
        return self._debug_mode

    @property
    def report(self):
        if self._debug_mode is None:
            from utils_logging.get_or_create_logger import get_or_create_logger
            self._report = get_or_create_logger(
                destinations=("console",),
                level=10 if self.DEBUG_MODE else 20
            )
        return self._report

    @property
    def TIME_OUT(self):
        if self._time_out is None:
            self._time_out = 10
        return self._time_out

    @property
    def POLL_FREQUENCY(self):
        if self._poll_frequency is None:
            self._poll_frequency = 0.1
        return self._poll_frequency


STG = Setting()
report = STG.report

if __name__ == "__main__":
    print(STG.DEBUG_MODE)
    print(STG.report)
