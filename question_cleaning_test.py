# 참고자료 https://api.ncloud-docs.com/docs/clovastudio-openaicompatibility
# 대상정보 증강 템플릿 적용 테스트

import os
import yaml
from dotenv import load_dotenv
from openai import OpenAI


# 🔹 CLOVA API, URL 로드
load_dotenv()
CLOVA_API_KEY = os.getenv("CLOVASTUDIO_API_KEY")
BASE_URL = os.getenv("CLOVASTUDIO_API_BASE_URL")


# 🔹 프롬프트 템플릿 로드
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
PROMPT_TEMPLATE = config["target_augmentation_template"]


# 🔹 OpenAI 호환 client 구성
client = OpenAI(
    api_key=CLOVA_API_KEY,
    base_url=BASE_URL
)
def execute_clovastudio(user_input: str):
    prompt = PROMPT_TEMPLATE.format(user_input=user_input)

    response = client.chat.completions.create(
        model="HCX-005",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


# 🔹 실행
if __name__ == "__main__":
    user_input = input("문장을 입력하세요: ")
    try:
        result = execute_clovastudio(user_input)
        print("\n=== Clova Studio 응답 ===")
        print(result)
    except Exception as e:
        print(f"오류 발생: {e}")
