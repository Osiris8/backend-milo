# Milo – Fullstack AI Assistant (Backend)

**Milo** is a robust backend for a fullstack AI assistant application, built with **Flask**, **JWT Authentication**, **Python**, and **Neon Database**. It integrates with **Groq Cloud** and **Mistral** AI models to power intelligent interactions, with API testing facilitated by **Postman**. This repository contains the backend logic, including authentication, routing, and AI model integration.

**Frontend Repository**: [https://github.com/Osiris8/frontend-milo](https://github.com/Osiris8/frontend-milo)

---

## Features

- Lightweight and scalable API built with **Flask**.
- Secure user authentication using **JWT**.
- Reliable data storage with **Neon Database**.
- AI-powered endpoints powered by **Groq Cloud** and **Mistral** APIs.
- Easy API testing with **Postman** collections.

---

## Getting Started

Follow these steps to set up and run the backend locally.

### 1. Prerequisites

Ensure you have the following installed:

- **Python** (3.8 or higher)
- **pip** (Python package manager)
- **Git**
- **Postman** (optional, for API testing)
- A **Neon Database** account ([neon.tech](https://neon.tech))
- API keys for **Groq Cloud** and **Mistral**

### 2. Clone the Repository

```bash
git https://github.com/Osiris8/backend-milo
cd milo-backend
```

### 3. Create a Virtual Environment

Set up a Python virtual environment to isolate dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root to store sensitive configuration:

```bash
touch .env  # On Windows: echo. > .env
```

Open the `.env` file and add the following environment variables, replacing placeholders with your actual values:

```bash
DATABASE_URI="YOUR_DATABASE_URI"
JWT_SECRET_KEY="YOUR_JWT_SECRET_KEY"
JWT_EXPIRE_HOURS=2
MISTRAL_API_KEY="YOUR_MISTRAL_API_KEY"
GROQ_API_KEY="YOUR_GROQ_API_KEY"
```

#### How to Obtain Environment Variables:

- **DATABASE_URI**: Get this from your Neon Database dashboard (e.g., `postgresql://user:password@host:port/dbname`).
- **JWT_SECRET_KEY**: Replace by your personnal key.
- **JWT_EXPIRE_HOURS**: Set to `2` (default) or adjust as needed.
- **MISTRAL_API_KEY**: Obtain from your Mistral account ([console.mistral.ai](https://console.mistral.ai)).
- **GROQ_API_KEY**: Obtain from your Groq Cloud account ([console.groq.com/home](https://console.groq.com/home)).

### 6. Run the Backend

Start the Flask development server:

```bash
flask --app app run
```

The backend will run on `http://localhost:5000`. You can verify it’s working using Postman or a browser.

---

## Testing with Postman

To test the API endpoints, use **Postman** to send requests to the backend. Below are the key endpoints for authentication, AI prompt handling, and prompt management. For local testing, use `http://localhost:5000`. For the deployed backend, use `https://backend-milo.onrender.com`.

### Authentication Endpoints

1. **Register a User**

   - **Method**: POST
   - **URL**: `http://localhost:5000/api/auth/register`
   - **Body** (JSON):
     ```json
     {
       "username": "your_username",
       "password": "your_password"
     }
     ```
   - **Response**: Returns a success message or error if the username exists.

2. **Login**

   - **Method**: POST
   - **URL**: `https://backend-milo.onrender.com/api/auth/login`
   - **Body** (JSON):
     ```json
     {
       "username": "your_username",
       "password": "your_password"
     }
     ```
   - **Response**: Returns a JWT token. Save this token for authenticated requests.

3. **Logout**
   - **Method**: POST
   - **URL**: `http://localhost:5000/api/auth/logout`
   - **Headers**: `Authorization: Bearer <your_jwt_token>`
   - **Response**: Confirms logout and invalidates the token.

### AI Prompt Endpoints

1. **Send Prompt with Mistral**

   - **Method**: POST
   - **URL**: `https://backend-milo.onrender.com/api/mistral/prompt`
   - **Headers**: `Authorization: Bearer <your_jwt_token>`
   - **Body** (JSON):
     ```json
     {
       "prompt": "Your prompt text here"
     }
     ```
   - **Response**: Returns the Mistral AI response.

2. **Send Prompt with Groq (Gemma Model)**

   - **Method**: POST
   - **URL**: `https://backend-milo.onrender.com/api/groqai/prompt`
   - **Headers**: `Authorization: Bearer <your_jwt_token>`
   - **Body** (JSON):

     ```json
     {
       "prompt": "Your prompt text here"
     }
     ```

   - **Response**: Returns the Groq AI response using the Gemma model.

### Prompt Management Endpoints

1. **Retrieve All Prompts**

   - **Method**: GET
   - **URL**: `https://backend-milo.onrender.com/api/mistral/prompt`
   - **Headers**: `Authorization: Bearer <your_jwt_token>`
   - **Response**: Returns a list of all stored prompts.

2. **Update Prompt (Mistral)**

   - **Method**: PUT
   - **URL**: `https://backend-milo.onrender.com/api/mistral/prompt/id`
   - **Headers**: `Authorization: Bearer <your_jwt_token>`
   - **Body** (JSON):
     ```json
     {
       "prompt": "Updated prompt text"
     }
     ```
   - **Response**: Confirms the prompt with ID 15 is updated.

3. **Update Prompt (Groq Cloud)**

   - **Method**: PUT
   - **URL**: `https://backend-milo.onrender.com/api/groqai/prompt/id`
   - **Headers**: `Authorization: Bearer <your_jwt_token>`
   - **Body** (JSON):
     ```json
     {
       "prompt": "Updated prompt text"
     }
     ```
   - **Response**: Confirms the prompt with ID 16 is updated.

4. **Delete Prompt**
   - **Method**: DELETE
   - **URL**: `https://backend-milo.onrender.com/api/mistral/prompt/id`
   - **Headers**: `Authorization: Bearer <your_jwt_token>`
   - **Response**: Confirms the prompt with ID 16 is deleted.

### Notes

- Ensure the backend is running locally (`http://localhost:5000`) or use the deployed URL (`https://backend-milo.onrender.com`).
- For authenticated endpoints, include the JWT token in the `Authorization` header as `Bearer <token>`.
- If a Postman collection is available in the repository, import it for pre-configured requests.

## Tech Stack

- **Framework**: Flask
- **Authentication**: JWT (Flask-JWT-Extended)
- **Database**: Neon Database (PostgreSQL)
- **API Testing**: Postman
- **Language**: Python
- **AI Integration**: Groq Cloud, Mistral APIs
- **Tools**: python-dotenv, psycopg2-binary

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

---

## Contact

Have questions or suggestions? Connect on [X](https://x.com/migan_osiris).

---

**Star this repo if you find it useful!**
