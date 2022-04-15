"""
This script allows to run flask server using gunicorn.
"""


from app import APP as application


# application instance
app = application


# main server loop for wsgi
if __name__ == "__main__":
    app.run()
