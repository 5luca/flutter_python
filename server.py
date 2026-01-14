from flask import Flask, jsonify, request
import os # pridej na zacatek souboru

app = Flask(__name__)

# Tohle je nas "endpoint" - misto, kam se mobil pripoji
@app.route('/vypocet', methods=['GET'])
def vypocet():
    try:
        # Ziskame cislo, ktere poslal mobil (jako parametr ?cislo=5)
        vstup = request.args.get('cislo')
        cislo = float(vstup)
        
        # --- TADY SE DEJE TVOJE VEDA ---
        # Pro ukazku jen mocnina, ale tady muze byt cokoliv
        vysledek = cislo * cislo
        zprava = f"Python spocital, ze {cislo} na2 je {vysledek}"
        # -------------------------------

        print(f"Mobil se ptal na {cislo}, odpovidam {vysledek}")
        
        # Posleme odpoved jako JSON
        return jsonify({
            'status': 'ok',
            'vysledek': vysledek,
            'zprava': zprava
        })

    except Exception as e:
        return jsonify({'status': 'error', 'zprava': str(e)})

if __name__ == '__main__':
    # Render si port urcuje sam v promenne prostredi PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)