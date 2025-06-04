from flask import Flask, request, jsonify, render_template
from fill_pdf import create_translated_pdf
app=Flask(__name__)

# @app.route("/")  #기본라우트
# def home():
#     return "✅ Flask 서버가 실행 중입니다!"

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/fill_pdf_api', methods=['POST'])
def fill_pdf_api():
    req_data = request.get_json()
    lang_code = req_data.get("lang_code")
    form_data = req_data.get("form_data")

    if not lang_code or not form_data:
        return jsonify({"error": "lang_code 또는 form_data가 누락되었습니다."}), 400

    try:
        output_path = create_translated_pdf(lang_code, form_data)
        return jsonify({"message": "PDF 생성 완료", "output_path": output_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

