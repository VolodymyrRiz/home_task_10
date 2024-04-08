import socket

def test_smtp_connection(host, port, timeout=10):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            print("Connection successful")
    except socket.error as e:
        print(f"Connection failed: {e}")

# Replace 'smtp.example.com' and 25 with your SMTP server's hostname and port
test_smtp_connection('smtp.meta.ua', 25)