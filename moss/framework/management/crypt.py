#! /usr/bin/env python

import sys

from moss.framework.crypt import MossCrypt
from moss.framework.utils import print_data_in_json

def crypt_cli_edit_encrypted_file(json, key, crypt_file):
    '''
    Summary:
    Controls editing of an encrypted file between the cli interface
    and operations from MossCrypt.
    '''

    if not key:
        print '-k/--key is a required argument.'
        sys.exit(1)

    if not crypt_file:
        print '-c/--crypt-file is a required argument.'
        sys.exit(1)

    result = MossCrypt().edit_encrypted_file(key, crypt_file)

    if result['result'] == 'fail' and not json:
        print 'Edit failed: {}'.format(result['reason'])
        sys.exit(1)

    if json:
        print_data_in_json(result)


def crypt_cli_generate_key():
    '''
    Summary:
    Returns a random key that can be used for encryption.
    '''

    print MossCrypt().generate_aes_encryption_key()


def crypt_cli_lock_plaintext_file(json, key, plaintext_file):
    '''
    Summary:
    Controls decryption of an encrypted file between the cli interface
    and operations from MossCrypt.
    '''

    if not plaintext_file:
        print '-p/--plaintext-file is a required argument.'
        sys.exit(1)

    result = MossCrypt().encrypt_file(key, plaintext_file)

    if result['result'] == 'fail' and not json:
        print 'Encryption failed: {}'.format(result['reason'])
        sys.exit(1)

    if not json:
        print 'Encryption {}'.format(result['result'])
        print 'Output file: {}'.format(result['data']['output_file'])
        sys.exit(0)

    print_data_in_json(result)


def crypt_cli_unlock_encrypted_file(json, key, crypt_file):
    '''
    Summary:
    Controls encryption of a plaintext file between the cli interface
    and operations from MossCrypt.
    '''

    if not key:
        print '-k/--key is a required argument.'
        sys.exit(1)

    if not crypt_file:
        print '-c/--crypt-file is a required argument.'
        sys.exit(1)

    result = MossCrypt().decrypt_file(key, crypt_file)

    if result['result'] == 'fail' and not json:
        print 'Decryption failed: {}'.format(result['reason'])
        sys.exit(1)

    if not json:
        print 'Decryption {}'.format(result['result'])
        print 'Output file: {}'.format(result['data']['output_file'])
        sys.exit(0)

    print_data_in_json(result)
