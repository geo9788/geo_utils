from azureml.core import Workspace, Dataset

# get workspace
ws = Workspace.get(subscription_id='', resource_group='', name='')

# get dataset
df = Dataset.get_by_name(ws, 'name', version='latest').to_pandas_dataframe()
