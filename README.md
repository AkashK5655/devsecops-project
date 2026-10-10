# My DevOps CI/CD Project

A small Flask application used to learn GitHub, Jenkins, Docker, and AWS EC2.

## Run locally

From the project folder, create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Install Flask and start the application:

```bash
python -m pip install -r requirements.txt
python app.py
```

Open <http://localhost:5000> to see the homepage, or
<http://localhost:5000/health> to check the health endpoint. The health endpoint
returns `{"status":"healthy"}`. The application listens on port `5000` by
default; set the `PORT` environment variable to use another port.

## Run with Docker

Build the image and start a container:

```bash
docker build -t devsecops-flask-app .
docker run --rm -p 5000:5000 devsecops-flask-app
```

Then open <http://localhost:5000>. Press `Ctrl+C` to stop the container.

## Test

Run the included tests from the project folder:

```bash
python -m unittest discover -v
```

The Jenkins pipeline checks out the source, validates Python syntax, creates an
isolated virtual environment, installs requirements, runs the tests, and builds
the Docker image. It does not deploy the application.

## Access on AWS EC2

After the application is running on the EC2 instance, visit
<http://54.158.49.113:5000> or
<http://54.158.49.113:5000/health>. The process must be listening on the
instance, and its Flask server binds to `0.0.0.0` so requests can reach it.

For testing, the EC2 Security Group must allow inbound **TCP port 5000** from an
appropriate source. Prefer your current public IP (a `/32` source) or another
trusted network rather than opening the port to everyone. Remove or restrict
the rule when testing is finished. This example uses plain HTTP and is intended
for learning, not production use.
