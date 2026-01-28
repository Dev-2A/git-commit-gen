# git-commit-gen

Git diff를 분석해서 커밋 메시지를 자동 생성하는 CLI 도구.

## 설치

```bash
pip install -e .
```

## 사용법

```bash
# 스테이징된 변경사항으로 커밋 메시지 생성
git-commit-gen

# 생성된 메시지로 바로 커밋
git-commit-gen --commit
```

## 기능 (예정)

- [ ] git diff 분석
- [ ] LLM 기반 커밋 메시지 생성
- [ ] Conventional Commits 포맷 지원
- [ ] 커밋 메시지 직접 적용 옵션

## 라이선스

MIT
