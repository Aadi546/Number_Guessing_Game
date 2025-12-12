from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    attempts_left = 5
    
    if request.method == 'POST':
        guess = int(request.form.get('guess', 0))
        
        # Game state (stored in session-like variables for demo)
        if not hasattr(index, 'secret_number'):
            index.secret_number = random.randint(1, 50)
            index.attempts = 0
        
        index.attempts += 1
        attempts_left = 5 - index.attempts
        
        if guess == index.secret_number:
            message = f"🎉 Correct! It was {index.secret_number} in {index.attempts} attempts!"
            # Reset for new game
            del index.secret_number
            del index.attempts
        elif attempts_left > 0:
            if guess < index.secret_number:
                message = f"Too low! ⬆️ Guess higher. Attempts left: {attempts_left}"
            else:
                message = f"Too high! ⬇️ Guess lower. Attempts left: {attempts_left}"
        else:
            message = f"💀 Game over! The number was {index.secret_number}. Play again!"
            # Reset for new game
            del index.secret_number
            del index.attempts
    
    return render_template('index.html', message=message, attempts_left=attempts_left)

if __name__ == '__main__':
    app.run(debug=True)
