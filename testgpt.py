import openai

# 设置 OpenAI API 密钥
openai.api_key = "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"
def test_gpt_connection():
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="What is the meaning of life?",
            max_tokens=50,
            temperature=0.7
        )
        generated_text = response.choices[0].text.strip()
        print("Generated response:", generated_text)
    except Exception as e:
        print("Connection test failed:", str(e))

# 调用连接测试函数
test_gpt_connection()
