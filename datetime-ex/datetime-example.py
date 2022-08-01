import datetime as dt

last_years_date = (dt.datetime.utcnow.date() - dt.timedelta(days=365)).strftime('%Y-%m-%d')  # NOQA:E501
