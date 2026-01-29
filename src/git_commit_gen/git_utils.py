import subprocess


def get_staged_diff() -> str:
    """스테이징된 변경사항의 diff를 반환합니다."""
    result = subprocess.run(
        ["git", "diff", "--cached"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )
    return result.stdout or ""


def get_staged_files() -> list[str]:
    """스테이징된 파일 목록을 반환합니다."""
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )
    stdout = result.stdout or ""
    return [f for f in stdout.strip().split("\n") if f]


def create_commit(message: str) -> bool:
    """주어진 메시지로 커밋을 생성합니다."""
    result = subprocess.run(
        ["git", "commit", "-m", message],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return result.returncode == 0