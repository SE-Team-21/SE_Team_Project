import hashlib
from Crypto.Cipher import AES
from secrets import token_bytes

# SHA-256 PASSWORD ENCRYPTION
pw = 'abcd'

def Encrypt(text): # 클라이언트에서 비밀번호를 암호화해서 서버에 전송
    return hashlib.sha256(text.encode()).hexdigest()

def Check(text):
    pw_hash = hashlib.sha256(pw.encode()) # 서버에 저장된 비밀번호와 비교해서
    return text == pw_hash.hexdigest() # 같으면 return True

# print(Encrypt(''))
# print(Check(Encrypt('abcd')))



# AES DATA ENCRYPTION
key = token_bytes(16)

def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False
    
nonce, ciphertext, tag = encrypt(input('Enter a message: '))
plaintext = decrypt(nonce, ciphertext, tag)
print(f'Cipher text: {ciphertext}')
if not plaintext:
    print('Message is corrupted')
else:
    print(f'Plain text: {plaintext}')