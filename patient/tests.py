import smtplib

EMAIL = "shahariasajjad72@gmail.com"
PASSWORD = "sbqt zeca dutv pwlp"

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    print("Login successful")
except Exception as e:
    print(f"Login failed: {e}")
finally:
    server.quit()

