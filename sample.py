import base64

def base64_encrypt(data):
    encoded_bytes = base64.b64encode(data.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

def base64_decrypt(encoded_data):
    decoded_bytes = base64.b64decode(encoded_data.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

# Example usage:
input_data = input("Enter the data to decrypt: ")
decrypted_data = base64_decrypt(input_data)
print("Decrypted data:", decrypted_data)
