import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>My DevOps CI/CD Project</title>
        <style>
          :root { color-scheme: light; font-family: system-ui, sans-serif; }
          body {
            align-items: center;
            background: linear-gradient(135deg, #eef2ff, #f8fafc);
            color: #172554;
            display: flex;
            justify-content: center;
            margin: 0;
            min-height: 100vh;
          }
          main {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 20px;
            box-shadow: 0 20px 50px #1e293b18;
            max-width: 560px;
            padding: 48px;
            text-align: center;
            width: calc(100% - 48px);
          }
          .status {
            background: #ecfdf5;
            border-radius: 999px;
            color: #047857;
            display: inline-block;
            font-size: 0.9rem;
            font-weight: 600;
            padding: 8px 14px;
          }
          h1 { font-size: clamp(2rem, 6vw, 3rem); margin: 24px 0 12px; }
          p { color: #475569; line-height: 1.7; }
          a { color: #4f46e5; }
        </style>
      </head>
      <body>
        <main>
          <span class="status">● Application is running</span>
          <h1>My DevOps CI/CD Project</h1>
          <p>Your Flask application is up and serving requests.</p>
          <p>Health check: <a href="/health">/health</a></p>
        </main>
      </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
