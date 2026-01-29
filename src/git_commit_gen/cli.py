import click

@click.command()
@click.option("--commit", is_flag=True, help="생성된 메시지로 바로 커밋합니다.")
@click.option("--type", "commit_type", type=str, default=None, help="커밋 타입 (feat, fix, docs 등)")
def main(commit: bool, commit_type: str | None) -> None:
    """Git diff를 분석해서 커밋 메시지를 자동 생성합니다."""
    click.echo("git-commit-gen v0.1.0")
    click.echo("아직 구현 중입니다...")


if __name__ == "__main__":
    main()