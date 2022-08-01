import socket
import unittest
import threading
from os.path import exists as file_exists
from src.client import serialize


class test_Client_connectivity(unittest.TestCase):

    def run_mock_server(self):
        # Run a server to listen for a connection and then close it
        mock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mock_server.bind((socket.gethostbyname(socket.gethostname()), 5050))
        mock_server.listen(0)
        mock_server.accept()
        mock_server.close()

    def test_client_connects_and_disconnects_to_server(self):
        # Start mock server in background thread
        server_thread = threading.Thread(target=self.run_mock_server)
        server_thread.start()

        # Test the clients basic connection and disconnection
        mock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mock_client.connect((socket.gethostbyname(socket.gethostname()), 5050))
        mock_client.close()

        # Ensure server thread ends
        server_thread.join()

    def test_send_data(self):
        server_host = socket.gethostbyname(socket.gethostname())
        port = 5050
        timeout = 10
        send_data = "This is client message"
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
        client_socket, addr = mock_server.accept()
        mock_client.send(bytes(send_data, "latin1"))
        recv_msg = client_socket.recv(1024).decode("latin1")
        mock_client.close()
        mock_server.close()
        self.assertEqual(send_data, recv_msg, "The message received is aligned")


class test_user_input_function(unittest.TestCase):

    def test_user_input_character(self):
        user_input = 'Y'
        choices = ['y', 'n']
        user_choice = user_input.lower()
        self.assertIn(user_choice, choices, 'Defined user character input not found')

    def test_user_input_number(self):
        user_input = '2'
        choices = ['1', '2', '3']
        user_choice = user_input.lower()
        self.assertIn(user_choice, choices, 'Defined user input number not found')


class test_check_file_function(unittest.TestCase):

    def test_check_file_type(self):
        """Check file exists and filetype is correct"""
        path = 'testing.txt'
        path_split = path.split(".")
        self.assertEqual(path_split[len(path_split) - 1], "txt", "Incorrect file type")

    def test_check_file_exist(self):
        path = 'testing.txt'
        self.assertTrue(file_exists(path))


class test_dictionary_enter(unittest.TestCase):

    def test_dictionary_input(self):
        value_amounts = "10"
        self.assertTrue(value_amounts.isnumeric())

    def test_dictionary_enter(self):
        test_dict_1 = {"Actor_first_name": "Johnny", "Actor_last_name": "Depp",
                       "Movie": "Caribbean"}
        test_dict_2 = {"Movie": "Caribbean", "Actor_last_name": "Depp",
                       "Actor_first_name": "Johnny"}
        self.assertDictEqual(test_dict_1, test_dict_2, "dictionary is aligned")


class test_serialize_data(unittest.TestCase):

    def test_serialize_method(self):
        s_type = 0
        default_dict = {}
        for i in range(2, 1):
            s_type += 1
            if s_type == 1:
                used_method = serialize(default_dict, s_type).method()
                self.assertEqual(used_method, 'pickle', 'Method not as same expect (pickle)')
            if s_type == 2:
                used_method = serialize(default_dict, s_type).method()
                self.assertEqual(used_method, 'json', 'Method not as same expect (json)')
            if s_type == 3:
                used_method = serialize(default_dict, s_type).method()
                self.assertEqual(used_method, "xml", "Method not as same expect (xml)")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
