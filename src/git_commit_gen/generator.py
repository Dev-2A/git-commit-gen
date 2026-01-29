from openai import OpenAI


SYSTEM_PROMPT_KO = """당신은 Git 커밋 메시지 작성 전문가입니다.
주어진 git diff를 분석하여 Conventional Commits 형식의 커밋 메시지를 생성하세요.

규칙:
1. 형식: <type>: <description>
2. type 종류: feat, fix, docs, style, refactor, test, chore
3. description은 한글로, 50자 이내로 작성
4. 명령형으로 작성 (예: "추가", "수정", "삭제")
5. 커밋 메시지만 출력하고 다른 설명은 하지 마세요"""


SYSTEM_PROMPT_EN = """You are a Git commit message expert.
Analyze the given git diff and generate a commit message in Conventional Commits format.

Rules:
1. Format: <type>: <description>
2. Types: feat, fix, docs, style, refactor, test, chore
3. Description in English, under 50 characters
4. Use imperative mood (e.g., "Add", "Fix", "Remove")
5. Output only the commit message, no explanations"""


def generate_commit_message(
    diff: str,
    files: list[str],
    commit_type: str | None = None,
    api_key: str | None = None,
    lang: str = "ko",
) -> str:
    """diff를 분석하여 커밋 메시지를 생성합니다."""
    client = OpenAI(api_key=api_key)
    
    system_prompt = SYSTEM_PROMPT_EN if lang == "en" else SYSTEM_PROMPT_KO
    user_content = f"변경된 파일: {', '.join(files)}\n\n```diff\n{diff}\n```"
    
    if commit_type:
        user_content += f"\n\n커밋 타입은 반드시 '{commit_type}'을 사용하세요."
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ],
        max_tokens=100,
        temperature=0.3,
    )
    
    return response.choices[0].message.content.strip()