# SQL-Agent

SQL-Agent is a project designed to facilitate SQL operations through a Model Context Protocol architecture. It allows users to interact with a server to execute SQL queries and manage database schemas efficiently.

## Features

- **MODEL CONTEXT PROTOCOL Architecture**: Separates the client interface from the server logic to enhance modularity and scalability.
- **Schema Management**: Provides tools to define and manage database schemas.
- **Service-Oriented Design**: Encapsulates functionalities into services for better code organization and maintenance.

## Project Structure

The project comprises the following key components:

- **agent-frontend/**: Contains the frontend code, primarily developed in JavaScript, CSS, and HTML, enabling user interaction.
- **client.py**: Implements the client-side application in Python, handling user inputs and communicating with the server.
- **server.py**: Serves as the server-side application in Python, processing client requests and interacting with the database.
- **schema.py**: Manages database schema definitions and migrations.
- **services.py**: Contains various service modules that encapsulate specific functionalities of the application.

## Technologies Used

- **Frontend**: JavaScript, CSS, HTML, ReactJs
- **Backend**: Python,FastAPI, MCP

  <img width="1430" alt="Screenshot 2025-03-20 at 3 06 37 PM" src="https://github.com/user-attachments/assets/b3bd8322-7ebb-4f05-93a5-fdceaed52ef2" />


## Getting Started

To set up the SQL-Agent project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/karthikzzzzzzz/SQL-Agent.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd SQL-Agent
   ```

3. **Install Dependencies**:
   - For Python components, ensure you have Python installed and use `pip` to install necessary packages.
   - For frontend components, ensure you have a compatible environment to serve static files.

4. **Run the Frontend**:
   ```bash
   cd agent-frontend
   npm install
   npm run dev
   ```

5. **Run the Client**:
   ```bash
   uvicorn client:app --reload
   ```



