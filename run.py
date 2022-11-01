from app import db, create_app

def create_db(app):
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app = create_app()
    create_db(app)
    app.run(host="0.0.0.0", port=5000)