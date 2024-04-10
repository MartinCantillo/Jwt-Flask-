# Token Generator API

This repository contains a project for an API to generate and verify JWT (JSON Web Tokens) using Python and Flask.

## Project Description

The project consists of two main endpoints:

1. `/`: This endpoint generates a new JWT token using provided user credentials. The generated token is returned as a response.
2. `/verificaciontoken`: This endpoint verifies the validity of a provided JWT token in the authorization header of the request. It returns a message indicating whether the token is valid or not.

## Requirements

The project is developed in Python and Flask. Make sure you have Python installed on your system. Additionally, the project requires the installation of the PyJWT library in version 2.8.0.

You can install the dependencies using the provided `requirements.txt` file by running the following command:

```
pip install -r requirements.txt
```

## Usage

1. Clone the repository to your local machine.
2. Install the dependencies using the above command.
3. Run the `app.py` file to start the Flask server.
4. Access the `/` and `/verificaciontoken` endpoints using an HTTP client (e.g., Postman) to generate tokens and verify their validity, respectively.

## Configuration

The project uses a secret key for encoding and decoding JWT tokens. Make sure to modify the secret key in the `app.py` file as needed for your production environment.

## Contribution

If you'd like to contribute to the project, feel free to submit a pull request. Any improvements, suggestions, or bug reports are welcome.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
