with open("flag", "rb") as f:
    FLAG = f.read()

gz_chat = [
    b"Hey man, have you ever heard of man-in-the-middle attacks?.",
    b"That's right, I'm studying network security recently and I know that this kind of attack is very dangerous.",
    b"Do you know how to prevent this kind of attack?",
    b"Thank you very much for your suggestion, I will take measures to protect my personal information as soon as possible. So, can you give me the flag now?"
]
mm_chat = [
    b"Yes, I've heard of it. It is a network security attack where hackers intercept packets of data and then tamper with or steal the data.",
    b"Yes, this attack allows hackers to steal personal information such as login credentials, credit card information, and more.",
    b"There are several ways to prevent man-in-the-middle attacks. First, you can use the HTTPS protocol, which encrypts data transfers. Second, you can use a virtual private network (VPN), which creates an encrypted tunnel between you and the Internet. Finally, you can use digital certificates, which verify a website's identity and integrity.",
    f"Here is your flag:{FLAG}. Go away!!! You just want flag, but not my answer!!!!"
    .encode()
]
