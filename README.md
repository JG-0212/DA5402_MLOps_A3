Methodology
- A new script my_server.py loads the model and initiates the server.
- The script contains a post method 'predict' which takes in data as base64 encoded string, decodes it and predicts the digit according to the model
- The prediction is returned to the client as a JSON object with key 'Digit'
- In the app.py script, the predict function is overridden by a custom predict fucntion which sends a post request to the URL
- The image is a Pillow object, which is not JSON serializable.
- After research, the image is converted to byte-data and then base64 encoded and transferred.
- The URL and the port exposed is set up in the configuration file.
- A dockerfile is created, but unable to verify it's working condition due to absence of docker-supported GUI in WSL natively.
- If the dockerfile doesn't work, please set up the environment using the requirements.txt
