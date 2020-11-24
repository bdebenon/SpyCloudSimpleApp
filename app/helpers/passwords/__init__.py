import hashlib

import passlib.hash


def decrypt_password(password, encryption_type):
    # There are many other encryption types not supported
    # May need to add more in the future as necessary

    if encryption_type == "plaintext":
        return password

    elif encryption_type == "sha3_224":
        return hashlib.sha3_224(password.encode()).hexdigest()

    elif encryption_type == "sha3_256":
        return hashlib.sha3_256(password.encode()).hexdigest()

    elif encryption_type == "sha3_384":
        return hashlib.sha3_384(password.encode()).hexdigest()

    elif encryption_type == "sha3_512":
        return hashlib.sha3_512(password.encode()).hexdigest()

    elif encryption_type == "sha1":
        return hashlib.sha1(password.encode()).hexdigest()

    elif encryption_type == "sha224":
        return hashlib.sha224(password.encode()).hexdigest()

    elif encryption_type == "sha256":
        return hashlib.sha256(password.encode()).hexdigest()

    elif encryption_type == "sha384":
        return hashlib.sha384(password.encode()).hexdigest()

    elif encryption_type == "sha512":
        return hashlib.sha512(password.encode()).hexdigest()

    elif encryption_type == "md5":
        return hashlib.md5(password.encode()).hexdigest()

    elif encryption_type == "phpass":
        # TODO: This may need salt and # of rounds support in the future
        return passlib.hash.phpass.encrypt(password)

    elif encryption_type == "bcrypt_sha256":
        return passlib.hash.bcrypt_sha256.encrypt(password)

    elif encryption_type == "bcrypt_sha256":
        return passlib.hash.sha256_crypt.encrypt(password)

    elif encryption_type == "snefru256":
        pass  # TODO:

    elif encryption_type == "base64":
        pass  # TODO:

    return password
