# Backend API

A simple Flask application to manage invoices through an API

- **[`app.py`](https://github.com/10thcode/invoice/blob/development/backend/app.py)**: The main entry point of the Flask application. Initializes the app, database, and registers the blueprints.


- **[`db.py`](https://github.com/10thcode/invoice/blob/development/backend/db.py)**: Contains the database initialization logic.

- **[`requirements.txt`](https://github.com/10thcode/invoice/blob/development/backend/requirement.txt)**: Lists of all the dependencies required by the project.

- **[`auth.py`](https://github.com/10thcode/invoice/blob/development/backend/auth.py)**: Defines a decorator to protect private api enpoints.

- **[`validator.py`](https://github.com/10thcode/invoice/blob/development/backend/validator.py)**: Contiains the Auth0 JWT bearer token validation logic.

- **[`api/`](https://github.com/10thcode/invoice/tree/development/backend/api)**: Contains versioned API routes.

## Setup
### Prerequisites

- [Python 3.x](https://www.python.org/)
- [MongoDB Atlas Database](https://www.mongodb.com/products/platform/atlas-database)
- [Auth0 API](https://auth0.com/docs/get-started/auth0-overview/set-up-apis)

### Installation

1. Clone the repository:
   ```bash
   git clone git@github.com:10thcode/invoice.git
   cd invoice/backend
   ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create an environment variables containing your MongoDB Atlas Database Cluster URI, Auth0 Tenant Domain and Auth0 API Application Identifier:
    ```bash
    export MONGO_URI=<your_mongodb_uri>
    export AUTH0_DOMAIN=<your_auth0_tenant_domain>
    export AUTH0_API_IDENTIFIER=<your_auth0_api_identifier>
    ```

### Running the Application

1. Start the Flask application:
    ```bash
    flask run
    ```

2. The application will run on http://127.0.0.1:5000/

## API Endpoints

### Version 1 (v1)

#### Get All Invoices
- URL: `/api/v1/invoices/`
- Method: `GET`
- Success Response:
    - Code: 200
    - Content: `[{...invoice1}, {...invoice2}, ...]`

#### Create a New Invoice
- URL: `/api/v1/invoices/`
- Method: `POST`
- Data Params: `{"field1": "value1", "field2": "value2", ...}`
- Success Response:
    - Code: 201
    - Content: `{"id": "new_invoice_id"}`

#### Get an Invoice by ID
- URL: /api/v1/invoices/<id>
- Method: GET
- Success Response:
    - Code: 200
    - Content: `{...invoice}`

#### Update an Invoice by ID
- URL: `/api/v1/invoices/<id>`
- Method: `PUT`
- Data Params: `{"field1": "value1", "field2": "value2", ...}`
- Success Response:
    - Code: 200
    - Content: `{"status": "success"}`

#### Delete an Invoice by ID
- URL: `/api/v1/invoices/<id>`
- Method: `DELETE`
- Success Response:
    - Code: 200
    - Content: `{"status": "success"}`

## Contributing
1. Fork the repository.

2. Create a new branch: `git checkout -b feature-branch-name`.

3. Make your changes and commit them: `git commit -m 'Add some feature'`.

4. Push to the branch: `git push origin feature-branch-name`.

5. Submit a pull request.
