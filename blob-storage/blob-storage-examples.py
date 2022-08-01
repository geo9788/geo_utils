from azure.storage.blob import BlobServiceClient
import pandas as pd
from io import StringIO

# connect to blob
bbs = BlobServiceClient.from_connection_string(conn_str='conn_str')

# list blobs
container_client = bbs.get_container_client('container')
blobs = container_client.list_blobs()

# blob push csv
df = pd.DataFrame(columns=['col1'])
dfout = df.to_csv(index=False, header=True, encoding='utf-8')
blob = bbs.get_blob_client('container', 'loc/blob_name')
blob.upload_blob(dfout, overwrite=True)

# blob download csv
blob = bbs.get_blob_client('container', 'loc/blob_name')
bbd = blob.download_blob().readall()
bbd_string = str(bbd, 'utf-8')
bbd_data = StringIO(bbd_string)
df = pd.read_csv(bbd_data)
