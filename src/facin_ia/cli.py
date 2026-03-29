from __future__ import annotations

import argparse
from pathlib import Path

from .scaffold import available_profiles, scaffold_project


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="facin-ia",
        description="Provisiona a estrutura FACIN_IA em um repositorio alvo.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser(
        "init",
        help="Materializa agentes, skills, prompts, plugin e arquivos de template.",
    )
    init_parser.add_argument(
        "--profile",
        choices=available_profiles(),
        default="customizacao",
        help="Perfil de scaffolding a aplicar no repositorio alvo.",
    )
    init_parser.add_argument(
        "--target",
        default=".",
        help="Diretorio onde o FACIN_IA sera provisionado.",
    )
    init_parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Sobrescreve arquivos existentes.",
    )

    subparsers.add_parser("list-profiles", help="Lista os perfis disponiveis.")
    return parser


def _run_init(args: argparse.Namespace) -> int:
    target_dir = Path(args.target).resolve()
    result = scaffold_project(target_dir=target_dir, profile=args.profile, overwrite=args.overwrite)

    print(f"FACIN_IA provisionado em: {target_dir}")
    print(f"Perfil aplicado: {args.profile}")
    print(f"Arquivos gravados: {len(result.written)}")
    if result.skipped:
        print(f"Arquivos preservados: {len(result.skipped)}")
        print("Use --overwrite para substituir arquivos existentes.")
    return 0


def _run_list_profiles() -> int:
    for profile in available_profiles():
        print(profile)
    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "init":
        return _run_init(args)
    if args.command == "list-profiles":
        return _run_list_profiles()

    parser.error("Comando invalido.")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
