from app import APP as application


# application instance
app = application


# main server loop for wsgi
if __name__ == "__main__":
    app.run()
