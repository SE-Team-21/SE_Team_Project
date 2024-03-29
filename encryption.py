import hashlib
import dill
import json
from cryptography.fernet import Fernet

# SHA-256 PASSWORD ENCRYPTION
def Encrypt_S(text):
    return hashlib.sha256(text.encode()).hexdigest()
# print((Encrypt_S('abcd')))


# AES-256 DATA ENCRYPTION
def load_key():
        try:
            with open("key.pkl","rb") as fr:
                key = dill.load(fr)
                return key
                
        except:
            with open('key.pkl', 'wb') as f:
                key = Fernet.generate_key()
                dill.dump(key, f)
                return key
            
# print(load_key())

def Encrypt_A(text):
    f = Fernet(load_key())
    serialized_data = json.dumps(text).encode('utf-8')
    encrypted_data = f.encrypt(serialized_data)
    return encrypted_data

def Decrypt_A(encrypted_data):
    f = Fernet(load_key())
    decrypted_data = f.decrypt(encrypted_data)
    decrypted_data = json.loads(decrypted_data.decode('utf-8'))
    return decrypted_data

#print(Decrypt_A(Encrypt_A({"Type": "pw", "Password": Encrypt_S('123')})))