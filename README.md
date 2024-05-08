# Vendor Management API

This Django project provides an API for managing vendor profiles.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (3.x recommended)
- Django
- Django REST framework

### Installing

1. Clone the repository:

```
git clone https://github.com/yourusername/vendor-management-api.git
```

2. Navigate to the project directory:

```
cd vendor-management-api
```

3. Install project dependencies:

```
pip install -r requirements.txt
```

### Running the Server

1. Apply database migrations:

```
python manage.py migrate
```

2. Start the development server:

```
python manage.py runserver
```

The API will be accessible at http://127.0.0.1:8000/.

## API Endpoints

- `POST /api/vendors/`: Create a new vendor.
- `GET /api/vendors/`: List all vendors.
- `GET /api/vendors/{vendor_id}/`: Retrieve a specific vendor's details.
- `PUT /api/vendors/{vendor_id}/`: Update a vendor's details.
- `DELETE /api/vendors/{vendor_id}/`: Delete a vendor.

## Built With

- Django - The web framework used
- Django REST framework - Toolkit for building Web APIs
