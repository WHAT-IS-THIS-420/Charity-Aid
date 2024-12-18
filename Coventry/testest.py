import os
import time
from cryptography.hazmat.primitives.twofactor.totp import TOTP
from cryptography.hazmat.primitives.hashes import SHA1
key = os.urandom(20)
totp = TOTP(key, 8, SHA1(), 30)
time_value = time.time()
totp_value = totp.generate(time_value)
totp.verify(totp_value, time_value)