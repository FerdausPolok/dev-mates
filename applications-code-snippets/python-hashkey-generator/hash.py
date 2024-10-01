import datetime, random, hashlib

email = "someone@gmail.com"
salt = '%0*d%0*d' % (8, random.randint(0, 99999999), 8, random.randint(0, 99999999))
activation_key = hashlib.md5((email+salt).encode("utf-8")).hexdigest()[:10]