import base64
import binascii
c = 'I300ryGVTXJVT803Sdt/KcOGlyPStZkeIHKapRjzwWf9+p7fIWkBnCWu/IWls+5S'
key = 'iyq1bFDkirtGqiFz7OVi4A=='
c_ba = base64.b64decode(c)
k_ba = base64.b64decode(key)
print(c_ba)
print(binascii.b2a_hex(c_ba))
print(binascii.b2a_hex(k_ba))
