from zipfile import ZipFile

file_name = 'test_zip.zip'

# Import zip file
with ZipFile(file_name, 'r') as zip:
    with open('english.txt', 'r') as f:
        # Read each password of the line and apply
        # it as a decryption password to our zip file 
        # with proper encoding. The process stops when we
        # find the correct password.
        for password in f:
            password = password.strip('\n')
            try:
                zip.extractall(pwd=bytes(password, 'utf-8'))
                print("[+] Password Found: %s" % password)
                break;
            except:
                print("[!] Password Incorrect: %s" % password)