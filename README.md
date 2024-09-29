# Voyage Mate ✈️🏙️⛰️🏖️
This project is a Backend application built using Python, focusing on managing trips and inviting participants via email. It includes functionality for:
 - managing trip data
 -  sending invitations
 -  storing participant information

Below is a detailed explanation of how the project works, including setup instructions and usage
## ✨ Features 
- Create and menage trips
- Invite participants to trips usiing their email adresses
- Store and retrieve participant data associated with trips
- Basic REST API for interacting with backend

## 💻 Technologies
- **Python 3.8+**: The main programming language used
- **Flask**: Lightweight web framework for building REST APIs
- **SQLite**: The database for storing trip and participant data
- **SQLAlchemy**: ORM (Object Relational Mapper) for database interaction
- **Pytest**: Used for writing and running unit tests

<p align = "center"> <img src="https://skillicons.dev/icons?i=python,sqlite,flask,django&theme=dark" /></p>

## 🧰 Setup
### Prerequisites
- 🐍 Python 3.8 or higher installed on your machine
- SQLite database (default is set in the project)

### Instalation
  1. Clone the repository
     ```
     git clone https://github.com/carolfons/backend-python.git
     cd backend-python
     ```
  2. Create a virtual enviroment and activate it:
     ```
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
  3. Install the required dependencies:
     ```
     pip install -r requirements.txt

     ```
  4. Set up the database:
     ```
     flask db upgrade
     ```
### Running the Application
1. Start the Flask development server:
   ```
   flask run
   ```
2. The API will be available at `http://127.0.0.1:5000/`

     
## 🏗️ Project Structure
```
backend-python/
│
├── src/
│   ├── controllers/
│   │   └── participant_creator.py  # Handles participant invitations logic
│   ├── models/
│   │   ├── repositories/           # Database interaction layer
│   │   └── settings/               # Database configuration
│   ├── routes/
│   │   └── trips_routes.py         # API routes for trips and participants
│   └── tests/                      # Unit and integration tests
├── migrations/                     # Database migrations
├── app.py                          # Main application entry point
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## 🛠️API Endpoints
### 🔶 Create a Trip
- **URL**: `/trips`
- **Method**: POST
- **Request Body**:
  
  ```
  {
  "destination": "New York",
  "start_date": "2024-01-02",
  "end_date": "2024-01-07",
  "owner_name": "John Doe",
  "owner_email": "john.doe@example.com"
  }
  
  ```

- **Response**:

  ```
  
  {
    "message": "Trip created successfully",
    "trip_id": "some-uuid-here"
  }
  
  ```

### 🔶 Invite Participants
- **URL**: `/trips/<tripId>/invites`
- **Method**: POST
- **Request Body**:
  
  ```
   {
    "email": "participant@example.com"
   }
  ```

- **Request Body**:
  
  ```
   {
     "message": "Invitation sent successfully"
   }
  ```

### 🔶 Find Emails by Trip
- **URL**:`/trips/<tripId>/emails`
- **Method**: GET
- **Response**:
  ```
  [
    {
      "email": "participant@example.com"
    }
  ]
  ```

### 🔶 Find Trip by ID
- **URL**:`/trips/<tripId>`
- **Method**: GET
- **Response**:

    ```
    {
      "id": "some-uuid-here",
      "destination": "New York",
      "start_date": "2024-01-02",
      "end_date": "2024-01-07",
      "owner_name": "John Doe",
      "owner_email": "john.doe@example.com"
    }
    ``` 

## 🧪 Testing
The project uses `pytest` for unit testing. To run the tests:
1. Install test dependencies:
   ```
   pip install -r requirements-dev.txt
   ```
2. Run the tests:  ``` pytest ```

## 🫂 Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name:
`git checkout -b feature-description`
3. Commit your changes:
   `git commit -m "Add a new feature"`
4. Push to the branch:
   `git push origin feature-description`
5. Create a pull request to the `main` branch

---

### Developed by: @carolfons
- **Linkedin**: https://www.linkedin.com/in/carolinefons/
  
<p align = "center">🔷🔶🔷🔶</p>

