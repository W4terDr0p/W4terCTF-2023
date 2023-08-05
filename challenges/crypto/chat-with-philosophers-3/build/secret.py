with open("flag", "rb") as f:
    FLAG = f.read()

part_len = len(FLAG) // 2

a_chat = [
    b"Then what should I do? I feel limited by the values of this society.",
    b"Thank you for your suggestions. I will try to think about my own life and values, and find my true direction and meaning.",
    b"Thank you for your suggestion, Mr. Sartre. I will try to re-examine my life, think about my ideals and values, and fight for them.",
    b"Oh! That's what I want, but you aren't Weber and Marcuse, you're just chatGPT who came to lie to me!!!!!!!!!"
]

Weber_chat = [
    b"Hello, Xiao Ming. We all know how you feel. From the perspective of sociology and philosophy, we believe that the structure and values of modern society often impose certain restrictions and constraints on people's lives, and these restrictions and constraints may lead to people's sense of emptiness and loss.",
    b"We cannot deny the existence and influence of society, but we can try to find our own direction and value through self-reflection and practice, so as to find our position and meaning in this society.",
    f"Very good, we believe that you can find your own place and meaning, and strive for it. What's more, this is part of your flag:{FLAG[:part_len]}."
    .encode()
]

Marcuse_chat = [
    b"Yes, the organization and culture of modern society often frame people within a certain range, making people lose their freedom and autonomy, which leads to mediocrity and boring life.",
    b"Yes, we need to get rid of the shackles of modern society and find our own way of life and meaning. It won't be easy, but with courage and determination, we believe you can achieve self-liberation.",
    f"We look forward to seeing your growth and transformation, come on! Here is your flag:{FLAG[part_len:]}"
    .encode()
]
