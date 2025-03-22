from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

# Générer un email aléatoire
def generate_random_email():
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{random_string}@temp.com"

# API pour générer un email temporaire
@app.route('/generate_email', methods=['GET'])
def generate_email():
    email = generate_random_email()
    return jsonify({"email": email})

# API pour copier l'email (simule le copier dans le presse-papier)
@app.route('/copy_email', methods=['POST'])
def copy_email():
    email = request.json.get("email")
    if email:
        # Ici tu pourrais ajouter une logique pour traiter l'email (par exemple, le stocker dans une base de données temporaire)
        return jsonify({"message": f"Email {email} copié!"})
    else:
        return jsonify({"error": "Email non fourni"}), 400

if __name__ == '__main__':
    app.run(debug=True)
