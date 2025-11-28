# adds headers used by browsers (CORS) so frontend JS can call the backend

def add_cors_headers(handler):
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Access-Control-Allow-Method", "GET, POST,PUT, DELETE, OPTIONS")
    handler.send_header("Access-Conrol-Allow-Headers", "Content-Type")