from flask import Flask, request
from azure.storage.blob import BlobServiceClient, BlobClient

app = Flask(__name__)

@app.route('/')
def list_files():
    # container_name = request.args.get('my-container')
    container_name = "<my-container-name>" #insert the name of the container whose filenames needs to be listed
    if container_name:
        try:
            files = list_files_in_container(container_name)
            return {'files': files}
        except Exception as e:
            return {'error': str(e)}, 500
    else:
        return {'error': 'Please provide a container name'}, 400

def list_files_in_container(container_name):
    connection_string = "<my-connection-string>" #insert the connection string of the storage account within which the container is located
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    files = []
    for blob in container_client.list_blobs():
        files.append(blob.name)
    return files

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0') #the flask app will run on port 5000
