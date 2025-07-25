from app import create_app

app = create_app()

if __name__ == "__main__":
    # Use debug mode for development, if needed
    app.run(port=8080, debug=True)
