from http.server import HTTPServer
from router import StudentRouter
from database.connection import init_database

def run_server():

    server = HTTPServer(("", 8000), StudentRouter)
    print(f" Server running at http://localhost:{8000}")
    server.serve_forever()

    if __name__ == "__main__":
        run_server()