import os
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """Специальный класс, который отвечает за обработку входящих запросов от клиентов."""

    def do_GET(self):
        """Метод для обработки входящих GET-запросов."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(root_dir, "contacts.html")

            with open(file_path, "r", encoding="utf-8") as file:
                content_html = file.read()
            self.wfile.write(bytes(content_html, "utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<h1>404 Not Found</h1>", "utf-8"))

    def do_POST(self):
        """Метод для обработки входящих POST-запросов."""
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        print(body.decode("utf-8"))

        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Сервер запущен http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Сервер остановлен!")
