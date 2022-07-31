import socket
import unittest
import os


# Connectivity test on server
class test_Server_Connection(unittest.TestCase):

    # mock a server for testing
    def run_mock_server(self):
        server_host = "127.0.0.1"
        port = 5000
        timeout = 10
        send_msg = "Hello"
        self.mock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mock_server.settimeout(timeout)
        self.mock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.mock_server.bind((server_host, port))
        self.mock_server.listen(1)

    # test ping the server by ip
    def test_Server_Addr(self):
        server_host = "127.0.0.1"
        response = os.system("ping -n 1 " + server_host)
        self.assertEqual(response, 0, 'Server is unreachable')

    # validate the server port by a connection attempt
    def test_Server_Port(self):
        self.run_mock_server()
        server_host = "127.0.0.1"
        port = 5000
        timeout = 5
        mock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mock_client.settimeout(timeout)
        result = mock_client.connect_ex((server_host, port))
        mock_client.close()
        self.mock_server.close()
        self.assertEqual(result, 0, 'Server port is not connect')

    def test_Socket_Error(self):
        # Testing socket module exceptions
        def raise_error(*args, **kwargs):
            raise socket.error

        self.assertRaises(socket.error, raise_error,
                          "Error raising socket exception.")

    # Testing default timeout
    def test_Default_Timeout(self):

        # The default timeout is initially None
        self.assertEqual(socket.getdefaulttimeout(), None)
        mock_server = socket.socket()
        self.assertEqual(mock_server.gettimeout(), None)
        mock_server.close()

        # Set default timeout to 10s, and check if it matches
        socket.setdefaulttimeout(10)
        self.assertEqual(socket.getdefaulttimeout(), 10)
        mock_server = socket.socket()
        self.assertEqual(mock_server.gettimeout(), 10)
        mock_server.close()

        # Reset default timeout to None, and check if it matches
        socket.setdefaulttimeout(None)
        self.assertEqual(socket.getdefaulttimeout(), None)
        mock_server = socket.socket()
        self.assertEqual(mock_server.gettimeout(), None)
        mock_server.close()

        # Check that setting it to an invalid value raises ValueError
        self.assertRaises(ValueError, socket.setdefaulttimeout, -1)

        # Check that setting it to an invalid type raises TypeError
        self.assertRaises(TypeError, socket.setdefaulttimeout, "spam")


# Functionality test on server
class test_Server_function(unittest.TestCase):

    # this is to mock a server and verify the message send and receive are aligned
    def test_mock_server_response(self):
        server_host = "127.0.0.1"
        port = 5000
        timeout = 10
        send_msg = "Hello"
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
        # mock a server response when connected
        mock_conn, mock_addr = mock_server.accept()
        mock_conn.send(bytes(send_msg, "utf-8"))
        # trail receive response from server
        recv_msg = mock_client.recv(1024).decode("utf-8")
        # close socket after use
        mock_client.close()
        mock_server.close()
        self.assertEqual(send_msg, recv_msg, "The message received is not aligned")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
