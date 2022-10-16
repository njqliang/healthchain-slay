import rsa



def get_keys():
    public_key, private_key = rsa.newkeys(512)

    return public_key.save_pkcs1().hex(), private_key.save_pkcs1().hex()

def add_to_chain(text, pubkey):
    blockchainfile = open("blockchain.txt", "a")

    encMessage = rsa.encrypt(text.encode(), rsa.PublicKey.load_pkcs1(bytes.fromhex(pubkey))).hex()

    blockchainfile.write(encMessage+"\n")

    blockchainfile.close()    

def read_chain(privkey):
    messages = ""

    with open("blockchain.txt", "r") as f:
        for line in f:
            try:
                messages += rsa.decrypt(line, rsa.PrivateKey.load_pkcs1(bytes.fromhex(privkey))).decode()
            except:
                continue
    
    return messages
