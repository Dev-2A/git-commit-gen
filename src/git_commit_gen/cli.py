import os
import click
from dotenv import load_dotenv

from git_commit_gen.git_utils import get_staged_diff, get_staged_files, create_commit
from git_commit_gen.generator import generate_commit_message


load_dotenv()


@click.command()
@click.option("--commit", is_flag=True, help="생성된 메시지로 바로 커밋합니다.")
@click.option("--type", "commit_type", type=str, default=None, help="커밋 타입 (feat, fix, docs 등)")
@click.option("--lang", type=click.Choice(["ko", "en"]), default="ko", help="커밋 메시지 언어 (기본: ko)")
def main(commit: bool, commit_type: str | None, lang: str) -> None:
    """Git diff를 분석해서 커밋 메시지를 자동 생성합니다."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        click.echo("오류: OPENAI_API_KEY 환경변수가 설정되지 않았습니다.", err=True)
        click.echo("export OPENAI_API_KEY='your-key' 또는 .env 파일을 생성하세요.", err=True)
        raise SystemExit(1)
    
    files = get_staged_files()
    if not files:
        click.echo("오류: 스테이징된 파일이 없습니다.", err=True)
        click.echo("git add <파일>로 변경사항을 스테이징하세요.", err=True)
        raise SystemExit(1)
    
    diff = get_staged_diff()
    if not diff.strip():
        click.echo("오류: 스테이징된 변경사항이 없습니다.", err=True)
        raise SystemExit(1)
    
    click.echo(f"📂 변경된 파일: {', '.join(files)}")
    click.echo(f"🌐 언어: {'English' if lang == 'en' else '한국어'}")
    click.echo("🤖 커밋 메시지 생성 중...")
    
    try:
        message = generate_commit_message(diff, files, commit_type, api_key, lang)
    except Exception as e:
        click.echo(f"오류: 메시지 생성 실패 - {e}", err=True)
        raise SystemExit(1)
    
    click.echo(f"\n💬 생성된 커밋 메시지:\n{message}\n")
    
    if commit:
        if create_commit(message):
            click.echo("✅ 커밋 완료!")
        else:
            click.echo("❌ 커밋 실패", err=True)
            raise SystemExit(1)
    else:
        click.echo("팁: --commit 옵션으로 바로 커밋할 수 있습니다.")


if __name__ == "__main__":
    main()