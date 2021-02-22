from os import path, remove
from time import sleep
from cryptography.fernet import Fernet
import pyAesCrypt

print('=-'*13)
print('<*/*> FILE ENCRYPTOR <*/*>')
print('-='*13)

bufferSize = 64 * 1024
event = True

def op_status(msg):
    print('=-'*13)
    print(msg)
    print('-='*13)


while event is True:
    print('[1]- Encrypt File\n[2]- Decrypt File\n[3]- Exit')
    funct = int(input('>> '))

    if funct == 1:
        print('=-' * 8)
        fname = str(input('File Name?\n>>'))
        fexten = str(input('File Extension? [txt/rar/*etc]\n>>').lower())
        check_originfile = path.isfile('{}.{}'.format(fname, fexten))
        if check_originfile is False:
            op_status('>>ERROR: FILE NOT FOUNDED!')
            sleep(1.)
            break
        else:
            encodekey = str(Fernet.generate_key())
            file = open('key-{}.txt'.format(fname), 'w')
            file.write(encodekey)
            file.close()
            # print('KEY: {}'.format(encodekey))
            pyAesCrypt.encryptFile('{}.{}'.format(fname, fexten), "{}-encrypted".format(fname), encodekey, bufferSize)
            op_status('<><> FILE ENCRYPTED! <><>')
            print('\n')

    elif funct == 2:
        print('=-' * 8)
        fname = str(input('Encrypted File Name?\n>>'))
        keyfile = str(input('Key File Name?\n>>').lower())
        check_encryptedfile = path.isfile('{}-encrypted'.format(fname))
        if check_encryptedfile is False:
            op_status('>>ERROR: FILE NOT FOUNDED!')
            sleep(1.)
            break
        else:
            fexten = str(input('Convert encrypted file to? [txt/rar/*etc]\n>>').lower())
            file = open('{}.txt'.format(keyfile), 'r')
            encodekey = file.read()
            file.close()
            pyAesCrypt.decryptFile('{}-encrypted'.format(fname), '{}.{}'.format(fname, fexten), encodekey, bufferSize)
            remove('{}.txt'.format(keyfile))
            remove('{}-encrypted'.format(fname))
            op_status('<><> FILE DECRYPTED! <><>')
            print('\n')

    elif funct == 3:
        print('=-'*15)
        sleep(.4)
        event = False

    else:
        op_status('{}INVALID OPTION!'.format(' '*5))
        sleep(1.)
