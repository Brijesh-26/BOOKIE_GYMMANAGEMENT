# BOOKIE_GYMMANAGEMENT

JWT Tokens
1. Obtain JWT Token
Endpoint: /token/
Method: POST
Description: Obtain a JSON Web Token (JWT) for authentication.
Request Body:
username (string): The username of the user.
password (string): The password of the user.
Response:
access (string): JWT access token.
refresh (string): JWT refresh token.
2. Refresh JWT Token
Endpoint: /token/refresh/
Method: POST
Description: Refresh the JWT access token using the refresh token.
Request Body:
refresh (string): The refresh token.
Response:
access (string): New JWT access token.
Gyms
3. List Gyms
Endpoint: /gyms/
Method: GET
Description: Retrieve a list of all gyms.
Response:
List of gyms with details.
4. Gym Detail
Endpoint: /gyms/<int:pk>/
Method: GET
Description: Retrieve details of a specific gym.
Parameters:
pk (integer): Gym ID.
Response:
Gym details.
Trainers
5. List Trainers
Endpoint: /trainers/
Method: GET
Description: Retrieve a list of all trainers.
Response:
List of trainers with details.
6. Trainer Detail
Endpoint: /trainers/<int:pk>/
Method: GET
Description: Retrieve details of a specific trainer.
Parameters:
pk (integer): Trainer ID.
Response:
Trainer details.
Clients
7. List Clients
Endpoint: /clients/
Method: GET
Description: Retrieve a list of all clients.
Response:
List of clients with details.
8. Client Detail
Endpoint: /clients/<int:pk>/
Method: GET
Description: Retrieve details of a specific client.
Parameters:
pk (integer): Client ID.
Response:
Client details.
Workout Sessions
9. List Workout Sessions
Endpoint: /workouts/
Method: GET
Description: Retrieve a list of all workout sessions.
Response:
List of workout sessions with details.
10. Workout Session Detail
Endpoint: /workouts/<int:pk>/
Method: GET
Description: Retrieve details of a specific workout session.
Parameters:
pk (integer): Workout session ID.
Response:
Workout session details.
