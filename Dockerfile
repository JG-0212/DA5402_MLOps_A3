FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt 
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container (Optional, only for web apps)
EXPOSE 7000

# Run app.py when the container launches
CMD ["sh", "-c", "python ./my_server.py & python ./app.py"]