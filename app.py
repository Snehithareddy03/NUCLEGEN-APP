import os
import re
import io
import base64
import logging
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import RNA
import forgi.visual.mplotlib as fvm
import forgi.graph.bulge_graph as fgb
from flask import Flask, request, jsonify

# Suppress noisy logs
logging.getLogger("PIL").setLevel(logging.WARNING)
logging.getLogger("forgi").setLevel(logging.WARNING)

app = Flask(__name__)

# Root route
@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Welcome to the RNA Structure Prediction API!",
        "usage": "Send a POST request to /RnaApp with a JSON payload: { 'sequence': 'AUGCUUAGC...' }"
    })

# Validate RNA sequence
def is_valid_rna_sequence(sequence):
    return re.fullmatch(r'^[AUGCaucg]+$', sequence) is not None

# Main prediction route
@app.route('/RnaApp', methods=['POST'])
def predict_rna():
    try:
        data = request.json
        rna_sequence = data.get('sequence', '').upper()

        if not rna_sequence:
            return jsonify({'error': 'RNA sequence is required'}), 400

        if not is_valid_rna_sequence(rna_sequence):
            return jsonify({'error': 'Invalid RNA sequence. Use only A, U, G, C.'}), 400

        # Predict structure
        fc = RNA.fold_compound(rna_sequence)
        structure, mfe = fc.mfe()

        # Visualize structure
        cg = fgb.BulgeGraph.from_dotbracket(structure, rna_sequence)
        plt.figure(figsize=(16, 16))
        ax = plt.gca()
        fvm.plot_rna(cg, text_kwargs={"fontweight": "bold", "fontsize": 12}, lighten=0.5, ax=ax)

        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', bbox_inches='tight', dpi=400)
        plt.close()
        img_buffer.seek(0)

        image_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')

        return jsonify({
            'structure': structure,
            'mfe': mfe,
            'image': image_base64
        })

    except Exception as e:
        logging.error(f"Error during RNA prediction: {e}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

# Run the app (Render uses PORT env variable)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
