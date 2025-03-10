# Example Flask Dashboard Application

This is an example Flask dashboard application that organizes useful links into groups.

## Installation

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the requirements:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Generate initial database data:**
    ```sh
    flask --app dashboard init-db
    ```

## Running the App

1. **Set the environment variables:**
    ```sh
    export FLASK_APP=dashboard
    export FLASK_RUN_HOST=0.0.0.0
    ```

2. **Run the app:**
    ```sh
    flask run
    ```
    or
    ```sh
    flask --app dashboard run --debug
    ```

3. **Open the app in your browser:**
    ```
    http://127.0.0.1:5000
    ```
## Docker

1. **Build the Docker image:**
    ```sh
    docker build -t flask-dashboard .
    ```

2. **Run the Docker container:**
    ```sh
    docker run -p 5000:5000 flask-dashboard
    ```

3. **Open the app in your browser:**
    ```
    http://127.0.0.1:5000
    ```
