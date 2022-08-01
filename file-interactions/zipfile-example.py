import zipfile

with zipfile.ZipFile('path/to/zipfile.zip', 'r') as zip_ref:
    zip_ref.extractall('location/to/extract/to')
