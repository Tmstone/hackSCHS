from config import app, db, func
import routes, admin_routes

if __name__ == "__main__":
    app.run(debug=True)