# CPU Specifications Database

A web application for managing and sharing HPC and datacenter CPU specifications. Provides a REST API and web interface for viewing, searching, and managing CPU data.

## Features

- **Public Web Interface**: Searchable, sortable table of CPU specifications
- **REST API**: Full CRUD operations with automatic documentation
- **CSV Import/Export**: Export to CSV/Excel formats
- **Database**: SQLite database with SQLAlchemy ORM

## Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/elokwentnie/hpc-cpu-specification-api.git
   cd hpc-cpu-specification-api
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Import initial data (optional)**
   ```bash
   python3 import_data.py
   ```

5. **Run the application**
   ```bash
   python3 app.py
   ```

6. **Access the application**
   - Web Interface: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Deployment on Render

### Prerequisites

- GitHub account
- Render account (free tier available)

### Steps

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create Web Service on Render**
   - Go to [render.com](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select your repository

3. **Configure Settings**
   - **Name**: `cpu-specifications-api`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free

4. **Set Environment Variables**
   - `ENVIRONMENT`: `production` (optional, defaults to production)

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (2-5 minutes)

### After Deployment

- **Public Interface**: `https://your-app.onrender.com/`
- **API Docs**: `https://your-app.onrender.com/docs`

## API Endpoints

### Public Endpoints

- `GET /` - Web interface
- `GET /api/cpus` - Get all CPUs (with pagination)
- `GET /api/cpus/{id}` - Get CPU by ID
- `GET /api/cpus/search?q=EPYC` - Search CPUs
- `GET /api/stats` - Get database statistics
- `GET /api/export/csv` - Export as CSV
- `GET /api/export/excel` - Export as Excel

### Protected Endpoints (Require Authentication)

- `POST /api/cpus` - Create new CPU
- `PUT /api/cpus/{id}` - Update CPU
- `DELETE /api/cpus/{id}` - Delete CPU

## Updating Data

To update the database, modify the CSV file in the repository and use the import script:

```bash
python3 import_data.py
```

## Project Structure

```
cpu-hpc-datacenters/
├── app.py                 # Main FastAPI application
├── database.py            # Database models and configuration
├── auth.py                # Authentication module
├── import_data.py         # Script to import CSV data
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment configuration
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── cpu_specifications.csv # Source data file
├── static/
│   └── index.html        # Public web interface
└── docs/                 # Additional documentation
```

## Security

- Write operations require authentication
- Tokens stored securely in environment variables
- JWT tokens with expiration

## Environment Variables

### Optional

- `ENVIRONMENT` - Set to `development` for dev mode, `production` for production
- `SECRET_KEY` - JWT secret key (auto-generated if not set)
- `PORT` - Server port (auto-set by Render)

## Database

The application uses SQLite database (`cpu_database.db`). The database file is created automatically on first run.

**Note**: On Render, the database persists between deployments. To reset, delete the database file or use the import with `clear_existing=true`.

## CSV Format

The CSV file should be semicolon-delimited with the following columns:

- CPU Model Name (required)
- Family
- CPU Model
- Cores
- Threads
- Max Turbo Frequency (GHz)
- L3 Cache (MB)
- TDP (W)
- Launch Year
- Max Memory (TB)

Decimal numbers use comma format (European): `3,7` instead of `3.7`

## License

This project is open source and available for use and modification.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
