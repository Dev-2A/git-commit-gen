# git-commit-gen

Git diff를 분석해서 커밋 메시지를 자동 생성하는 CLI 도구.

## 설치

```bash
pip install -e .
```

## 사용법

```bash
# 스테이징된 변경사항으로 커밋 메시지 작성
git-commit-gen

# 영어로 커밋 메시지 작성
git-commit-gen --lang en

# 커밋 타입 지정
git-commit-gen --type feat

# 생성된 메시지로 바로 커밋
git-commit-gen --commit

# 옵션 조합
git-commit-gen --lang en --type fix --commit
```

## 옵션

| 옵션 | 설명 | 기본값 |
| --- | --- | --- |
| `--lang` | 커밋 메시지 언어 (`ko`, `en`) | `ko` |
| `--type` | 커밋 타입 (feat, fix, docs 등) | 자동 |
| `--commit` | 생성된 메시지로 바로 커밋 | - |

## 설정

`.env` 파일 또는 환경변수로 OpenAI API 키를 설정하세요:

```bash
export OPENAI_API_KEY='your-key'
```

## 라이선스

MIT

## 개발자

- Dev-2A
