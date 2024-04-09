import sys

sys.path.append('../afas_connector')
sys.path.append('..')

from afas_connector import AfasConnector, AfasFilter

# Get organizations from AFAS
status_code, data = AfasConnector().get('revent-organisaties', filters=[AfasFilter("Unieke_Hash", "[is leeg]", AfasFilter.IS_EMPTY)])

# Print the status code and the data
print(status_code)
print(data)