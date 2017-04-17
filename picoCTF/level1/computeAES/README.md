## computeAES

### 题目:  
> Encrypted with AES in ECB mode. All values base64 encoded  
ciphertext = I300ryGVTXJVT803Sdt/KcOGlyPStZkeIHKapRjzwWf9+p7fIWkBnCWu/IWls+5S  
key = iyq1bFDkirtGqiFz7OVi4A==

这题的目的是解出题目提供的AES密码。。。。但是出题者已经把key都给你了....毫无难度，只需要在解字串之前解码一下base64然后把所得字符hex一下就可以还原出密文和key(以16进制模式)。。。然后导入AES算法解码就行

### 还原结果:
> flag{do_not_let_machines_win_2d4975bc}__________
