from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

new_directory = '/opt/idfs/terraform-ws'

@app.route('/terraform/apply', methods=['POST'])
def apply_terraform():
    try:
        # Run Terraform apply command
        result = subprocess.run(['terraform', 'apply', '-auto-approve'], cwd=new_directory, capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({"message": "Terraform apply successful", "output": result.stdout}), 200
        else:
            return jsonify({"message": "Terraform apply failed", "error": result.stderr}), 500
    except Exception as e:
        return jsonify({"message": "Error occurred", "error": str(e)}), 500

@app.route('/terraform/destroy', methods=['POST'])
def destroy_terraform():
    try:
        # Run Terraform destroy command
        result = subprocess.run(['terraform', 'destroy', '-auto-approve'], cwd=new_directory, capture_output=True, text=True)
        if result.returncode == 0:
            return jsonify({"message": "Terraform destroy successful", "output": result.stdout}), 200
        else:
            return jsonify({"message": "Terraform destroy failed", "error": result.stderr}), 500
    except Exception as e:
        return jsonify({"message": "Error occurred", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

