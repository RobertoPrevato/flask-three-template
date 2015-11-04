from app import setup_app

app = setup_app()
if __name__ == "__main__":
    """Run the application"""
    app.run(host=app.config.get("HOST"), port=app.config.get("PORT"))
