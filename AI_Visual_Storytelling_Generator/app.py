from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_script():

    data = request.json

    product = data.get('product')
    audience = data.get('audience')
    tone = data.get('tone')
    platform = data.get('platform')
    content_type = data.get('content_type')

    result = f"""
🔥 HOOK
"Luxury is no longer a style.
It's an identity."

━━━━━━━━━━━━━━━━━━━

🎬 VISUAL STORY FLOW

Scene 1:
Close-up cinematic shot of {product} under soft ambient lighting.

Scene 2:
A confident {audience} creator walking through a futuristic urban setting.

Scene 3:
Slow-motion transitions with dramatic camera angles optimized for {platform}.

Scene 4:
Minimal luxury aesthetics combined with emotional storytelling visuals.

━━━━━━━━━━━━━━━━━━━

🎤 VOICEOVER SCRIPT

"They follow trends.
You create presence.

{product} isn't made to impress everyone.
It's designed for the people who understand elegance without explanation."

━━━━━━━━━━━━━━━━━━━

🎥 CINEMATIC SHOTS

• Neon lighting aesthetics  
• Soft luxury color grading  
• Editorial-style framing  
• Slow-motion cinematic transitions  
• Urban night visuals  
• Premium fashion-inspired composition

━━━━━━━━━━━━━━━━━━━

📢 CALL TO ACTION

"Experience the future of premium storytelling with {product}."

━━━━━━━━━━━━━━━━━━━

📝 VIRAL CAPTION

Some products are seen.
Others are remembered. ✨

━━━━━━━━━━━━━━━━━━━

🚀 HASHTAGS

#{product.replace(" ", "")}
#LuxuryBranding
#CinematicMarketing
#GenZAesthetic
#CreativeAdvertising
#VisualStorytelling
#DigitalBranding
"""

    return jsonify({
        "result": result
    })


if __name__ == '__main__':
    app.run(debug=True)