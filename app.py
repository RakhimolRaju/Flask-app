from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Flask DevOps App</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f8f9fa;
                    font-family: Arial, sans-serif;
                }
                h1 {
                    color: #2c3e50;
                    text-align: center;
                }
            </style>
        </head>
        <body>
            <h1>Hello....! This is a Flask app created by Rakhimol Raju</h1>
            <h2> This Flask app is running inside a Docker container on an AWS EC2 instance <h2>
            <h2>Deployed automatically using Azure DevOps CI/CD pipeline <h2> 
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
