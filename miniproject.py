from flask import Flask, render_template, request

app = Flask(__name__,template_folder='Template')


def encrypt_message(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isupper():
            encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_message += char
    return encrypted_message


def decrypt_message(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isupper():
            decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_message += char
    return decrypted_message


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form['message']
    shift = int(request.form['shift'])
    encrypted_message = encrypt_message(message, shift)
    return render_template('result.html', result=encrypted_message)


@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_message = request.form['message']
    shift = int(request.form['shift'])
    decrypted_message = decrypt_message(encrypted_message, shift)
    return render_template('result.html', result=decrypted_message)


if __name__ == '__main__':
    app.run(debug=True)
