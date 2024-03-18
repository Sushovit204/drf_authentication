## API Documentation for Django Authentication using JWT

### API ENDPOINTS

#### `POST /api/register/`

- **Description:** Register a user.
- **Parameters:**
  - name - Character Field(required)
  - email - Email Field(required)
  - password - Character Field(required)
- **Returns:** Successfully registered user.

#### `POST /api/login/`

- **Description:** Logs a user.
- **Parameters:**
  - email - Email Field(required)
  - password - Character Field(required)
- **Returns:** Successfully logs in a user if authenticated and generated JWT.

#### `GET /api/user/`

- **Description:** Shows currently logged in user.
- **Parameters:** Not needed
- **Returns:** Shows User details if Logged In.

#### `POST /api/logout/`

- **Description:** Logs out the currently logged in user.
- **Parameters:**
- **Returns:** Successfully logs out a user if is currently logged In.

## API USE GUIDE

To use the Entity Controller API, follow the instructions below:

1. **Have Python Installed:** Ensure python 3 is installed in your system

2. **Clone the Project:** Clone the project or copy all the content of the project

3. **Setup the  Virtual Environment:** Create and setup python virtual environmnet
    - Create a virtual environmnet using `py3 -m venv venv`. 
    - Activate virtual environment using `Source venv/Scripts/activate`.

4. **Install Dependencies:** Install the project dependencies using `pip install -r requirements.txt`

5. **Setup Environment Variables:** Create a .env file and setup the environment variables as described in the .env.example file.

6. **Migration:** After the setting up the environmnet variables and migrate database models using `python manage.py migrate` command and your database is set.

7. **API Endpoints:**
   - Utilize the provided endpoints to interact with the API data.
   - You can register a user, log in using email and password, retrieve currently logged in user detail  and logout

8. **Request Format:**
   - For POST and provide the required data in the request body in the specified format.


By following these steps, you can effectively utilize the Entity Controller API in your application.
h criteria, gender, date range, and countries.
