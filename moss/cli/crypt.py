#! /usr/bin/env python

import click

from moss.framework.management.crypt import crypt_cli_edit_encrypted_file, crypt_cli_generate_key, \
                                            crypt_cli_lock_plaintext_file, crypt_cli_unlock_encrypted_file

@click.command(short_help = 'Edit a currently encrypted file')
@click.option('-j', '--json', is_flag=True, help = 'Output in JSON format')
@click.option('-k', '--key', default=None, help = 'Key to be used for encryption')
@click.option('-c', '--crypt-file', default=None, help = 'Target encrypted file to be edited')
def edit(json, key, crypt_file):
    crypt_cli_edit_encrypted_file(json, key, crypt_file)


@click.command(short_help = 'Generate an 256 bit key for encryption')
def generate_key():
    crypt_cli_generate_key()


@click.command(short_help = 'Encrypt a plaintext file with AES-256')
@click.option('-j', '--json', is_flag=True, help = 'Output in JSON format')
@click.option('-k', '--key', default=None, help = 'Key to be used for encryption')
@click.option('-p', '--plaintext-file', default=None, help = 'Target file to be encrypted')
def lock(json, key, plaintext_file):
    crypt_cli_lock_plaintext_file(json, key, plaintext_file)


@click.command(short_help = 'Decrypt an encrypted file')
@click.option('-j', '--json', is_flag=True, help = 'Output in JSON format')
@click.option('-k', '--key', default=None, help = 'Key to be used for encryption')
@click.option('-c', '--crypt-file', default=None, help = 'Target file to be decrypted')
def unlock(json, key, crypt_file):
    crypt_cli_unlock_encrypted_file(json, key, crypt_file)


@click.group(short_help = 'Control encryption, decryption, and editing for files')
def crypt():
    pass


crypt.add_command(edit)
crypt.add_command(generate_key, name = 'generate-key')
crypt.add_command(lock)
crypt.add_command(unlock)
