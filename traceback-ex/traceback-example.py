import traceback

try:
    something_that_doesnt_work = True
except Exception:
    print(traceback.format_exc())
