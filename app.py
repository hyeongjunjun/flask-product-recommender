from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "YOUR_API_KEY"  # ⚠️ 나중에 Render에 환경변수로 설정할 예정!

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    title = data.get('title', '')
    keyword = data.get('keyword', '')

    prompt = f"상품명: {title}\n키워드: {keyword}\n이 상품을 바탕으로 사람들이 구매하고 싶어지는 상세 설명을 작성해줘."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 나중에 필요하면 4로 업그레이드 가능
            messages=[
                {"role": "system", "content": "너는 뛰어난 상품 설명 전문가야."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        result = response.choices[0].message.content
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
