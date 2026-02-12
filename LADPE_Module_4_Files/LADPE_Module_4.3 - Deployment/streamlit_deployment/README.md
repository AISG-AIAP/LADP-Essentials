# Business Report Generator - Streamlit App

A streamlit web application that generates comprehensive business reports on any topic using AI agents via Flowise API.

## Features

- **Research Agent**: Searches for credible information and key findings
- **Analyst Agent**: Analyzes data and identifies business insights
- **Report Writing Agent**: Creates professional business reports
- **Export Options**: Save reports as Word documents or text files
- **User-Friendly Interface**: Clean and intuitive design

## Installation

### Option 1: Local Installation

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

### Option 2: Docker

#### Using Docker directly:

1. Build the Docker image:

```bash
docker build -t business-report-generator .
```

2. Run the container:

```bash
docker run -p 8501:8501 business-report-generator
```

3. Access the app at `http://localhost:8501`

#### Using Docker Compose:

1. Start the application:

```bash
docker-compose up -d
```

2. Access the app at `http://localhost:8501`

3. Stop the application:

```bash
docker-compose down
```

## Usage

1. Enter a topic in the text input field (e.g., "Autonomous Vehicles", "Renewable Energy", "Artificial Intelligence")

2. Click "Generate Report" and wait for the AI agents to process your request

3. View the formatted report and download it as:
   - **Word Document (.docx)** - professionally formatted
   - **Text File (.txt)** - plain text version

## How It Works

The app uses a multi-agent system that:

1. **Research Agent** - Searches for recent developments, statistics, and expert opinions
2. **Analyst Agent** - Analyzes the findings and identifies business implications
3. **Report Writing Agent** - Compiles everything into a structured business report

Each report includes:
- Executive Summary
- Key Findings
- Detailed Analysis
- Recommendations
- Sources

## API Configuration

The app is configured to use the Flowise API endpoint. If you need to change the API URL, modify the `API_URL` variable in `streamlit_app.py`:

```python
API_URL = "http://localhost:3000/api/v1/prediction/e2a3465a-21b2-41c0-a64f-957cd3bdfda2"
```

## Requirements

### Local Installation
- Python 3.8+
- streamlit
- requests
- python-docx

### Docker Deployment
- Docker 20.10+
- Docker Compose 1.29+ (optional, for docker-compose deployment)

## Notes

- Report generation may take 10-30 seconds depending on the topic complexity
- All reports are timestamped and include cited sources
- Reports are not saved automatically - use the download buttons to save them

