import socket
import unittest
import threading


class test_Client_connectivity(unittest.TestCase):

    def run_mock_server(self):
        # Run a server to listen for a connection and then close it
        mock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mock_server.bind(('127.0.0.1', 5000))
        mock_server.listen(0)
        mock_server.accept()
        mock_server.close()

    def test_client_connects_and_disconnects_to_server(self):
        # Start fake server in background thread
        server_thread = threading.Thread(target=self.run_mock_server)
        server_thread.start()

        # Test the clients basic connection and disconnection
        mock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mock_client.connect(('127.0.0.1', 5000))
        mock_client.close()

        # Ensure server thread ends
        server_thread.join()

    def test_mock_server_response(self):
        server_host = "127.0.0.1"
        port = 5000
        timeout = 10
        send_msg = "Hello, this is server message"
        # mock a server
        mock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mock_server.settimeout(timeout)
        mock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mock_server.bind((server_host, port))
        mock_server.listen(5)
        # mock a client
        mock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mock_client.settimeout(timeout)
        mock_client.connect((server_host, port))
        # trial on send server response
        mock_conn, mock_addr = mock_server.accept()
        mock_conn.send(bytes(send_msg, "utf-8"))
        # trail on receive server response
        recv_msg = mock_client.recv(1024).decode("utf-8")
        mock_client.close()
        mock_server.close()
        self.assertEqual(send_msg, recv_msg, "The message received is aligned")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)