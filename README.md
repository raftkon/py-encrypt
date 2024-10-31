# Python encryption tool

The project provides 2 scripts for encrypt and decrypt files. It will create a key and save it to `secret.key` file and save the encrypted file as `<filename>.encrypted` in the `/certs` folder. Provide the encrypted file to the `decrypt.py` script and see the decrypted file as `<filename>_decrypted.txt`.

## Usage

Create a `/certs` directory and put inside the files you want to encrypt.

Run encryption script and provide the name of the file:

```bash
python encrypt.py <filename>
```

Run decryption script and provide the name of the file:

```bash
python decryption.py <filename>
```
