from zipfile import ZipFile

file_name = 'test_zip.zip'

with ZipFile(file_name, 'r') as zip:
    with open('english.txt', 'r') as f:
        for password in f:
            password = password.strip('\n')
            try:
                zip.extractall(pwd=bytes(password, 'utf-8'))
                print("[+] Password Found: %s" % password)
                break;
            except:
                print("[!] Password Incorrect: %s" % password)