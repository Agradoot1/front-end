from app import create_app
app = create_app()

if __name__ == '__main__':
    app.app_context().push()
    from app.database import db
    db.create_all()
    app.run(debug=True)
