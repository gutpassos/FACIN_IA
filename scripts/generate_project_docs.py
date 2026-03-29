"""Gera HTMLs e PDFs a partir dos Markdowns do projeto Conversa_Folha_doc.

Adaptado do generate_project_docs.py do projeto AGE/FACIN_IA.
Autor: Guttenberg Ferreira Passos
"""
from __future__ import annotations

import html as html_module
import re
import threading
from pathlib import Path

from markdown import markdown

# ---------------------------------------------------------------------------
# Caminhos
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent          # scripts/
PROJECT_DIR = SCRIPT_DIR.parent                       # Conversa_Folha_Doc/

DOCS_DIR = PROJECT_DIR / "docs"
ERRORS_DIR = PROJECT_DIR / "erros"



# ---------------------------------------------------------------------------
# HTML / CSS
# ---------------------------------------------------------------------------
CSS = """
:root { --bg: #f4f1e8; --panel: #fffaf0; --ink: #17324d; --line: #d4c7ad; --accent: #0b5c63; }
* { box-sizing: border-box; }
body { margin: 0; font-family: Segoe UI, Arial, sans-serif; background: var(--bg); color: var(--ink); }
main { max-width: 1100px; margin: 0 auto; padding: 28px 22px 40px; }
article { background: var(--panel); border: 1px solid var(--line); border-radius: 24px; padding: 28px;
          box-shadow: 0 16px 36px rgba(23,50,77,0.08); }
h1, h2, h3, h4 { color: #0b3a66; }
h1 { font-size: 32px; margin-top: 0; }
h2 { border-top: 1px solid var(--line); padding-top: 18px; }
p, li { line-height: 1.6; }
a { color: var(--accent); }
table { width: 100%; border-collapse: collapse; margin: 18px 0; font-size: 13px; }
th, td { border: 1px solid var(--line); padding: 8px; vertical-align: top; }
th { background: #eadfc6; text-align: left; }
code { background: #efe5d1; padding: 2px 4px; }
pre { background: #f7f0e5; padding: 14px; overflow-x: auto; border-radius: 14px; }
.mermaid { margin: 24px 0; text-align: center; overflow-x: auto; }
"""


def inject_mermaid_support(html_text: str) -> str:
    html_text = re.sub(
        r'<pre><code class="language-mermaid">(.*?)</code></pre>',
        lambda m: f'<div class="mermaid">{html_module.unescape(m.group(1))}</div>',
        html_text,
        flags=re.DOTALL,
    )
    mermaid_script = (
        '<script type="module">'
        'import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";'
        "mermaid.initialize({ startOnLoad: true });"
        "</script>"
    )
    return html_text.replace("</body>", f"{mermaid_script}\n</body>")


def md_to_html(md_path: Path, html_path: Path) -> None:
    md_text = md_path.read_text(encoding="utf-8")
    title = "Conversa_Folha_doc"
    for line in md_text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break
    body = markdown(md_text, extensions=["tables", "fenced_code", "toc"])
    html_doc = (
        f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"/>'
        f'<meta name="viewport" content="width=device-width, initial-scale=1"/>'
        f"<title>{html_module.escape(title)}</title><style>{CSS}</style></head>"
        f"<body><main><article>{body}</article></main></body></html>"
    )
    html_doc = inject_mermaid_support(html_doc)
    html_path.write_text(html_doc, encoding="utf-8")


# ---------------------------------------------------------------------------
# PDF (xhtml2pdf)
# ---------------------------------------------------------------------------
CSS_VARS = {
    "var(--bg)": "#f4f1e8",
    "var(--panel)": "#fffaf0",
    "var(--ink)": "#17324d",
    "var(--line)": "#d4c7ad",
    "var(--accent)": "#0b5c63",
}


def html_to_pdf(html_path: Path, pdf_path: Path, timeout: int = 60) -> bool:
    try:
        from xhtml2pdf import pisa
    except ImportError:
        print("  xhtml2pdf não disponível. Instale com: pip install xhtml2pdf")
        return False
    try:
        html_text = html_path.read_text(encoding="utf-8")
        for var, val in CSS_VARS.items():
            html_text = html_text.replace(var, val)
        # Remove mermaid divs que travam o xhtml2pdf
        html_text = re.sub(r'<div class="mermaid">.*?</div>', '<p>[Diagrama Mermaid - visualizar no HTML]</p>', html_text, flags=re.DOTALL)
        # Remove scripts
        html_text = re.sub(r'<script.*?</script>', '', html_text, flags=re.DOTALL)
        if len(html_text) > 300_000:
            print(f"  SKIP PDF: {html_path.name} (HTML muito grande para xhtml2pdf)")
            return False

        result = [False]

        def _generate():
            try:
                with open(pdf_path, "wb") as f:
                    status = pisa.CreatePDF(html_text, dest=f)
                result[0] = not status.err
            except Exception:
                result[0] = False

        t = threading.Thread(target=_generate, daemon=True)
        t.start()
        t.join(timeout=timeout)
        if t.is_alive():
            print(f"  TIMEOUT PDF: {html_path.name} (>{timeout}s)")
            return False
        return result[0]
    except Exception as e:
        print(f"  Erro PDF {html_path.name}: {e}")
        return False


# ---------------------------------------------------------------------------
# Publicação completa (MD → HTML → PDF)
# ---------------------------------------------------------------------------
def publish_markdown(md_text: str, stem: str, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    md_path = output_dir / f"{stem}.md"
    html_path = output_dir / f"{stem}.html"
    pdf_path = output_dir / f"{stem}.pdf"
    md_path.write_text(md_text, encoding="utf-8")
    md_to_html(md_path, html_path)
    if html_to_pdf(html_path, pdf_path):
        print(f"  OK: {stem} (.md + .html + .pdf)")
    else:
        print(f"  OK: {stem} (.md + .html) — PDF ignorado")


# ---------------------------------------------------------------------------
# Conversão em lote de .md existentes
# ---------------------------------------------------------------------------
def convert_existing_docs(skip_stems: set[str] | None = None) -> int:
    skip = skip_stems or set()
    total = 0
    for folder in [DOCS_DIR, ERRORS_DIR]:
        if not folder.exists():
            continue
        for md in sorted(folder.glob("*.md")):
            if md.stem in skip:
                print(f"  SKIP: {md.stem} (já processado)")
                continue
            html_path = md.with_suffix(".html")
            pdf_path = md.with_suffix(".pdf")
            md_to_html(md, html_path)
            html_to_pdf(html_path, pdf_path)
            print(f"  OK: {md.stem} (.html + .pdf)")
            total += 1
    return total


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    ERRORS_DIR.mkdir(exist_ok=True)

    print("=" * 60)
    print("Conversa_Folha_doc — Gerador de Documentação do Projeto")
    print("=" * 60)

    # Converter todos os .md existentes para HTML + PDF
    print("\nConvertendo documentos .md → .html + .pdf...")
    total = convert_existing_docs()
    print(f"  Total de documentos convertidos: {total}")

    print("\n" + "=" * 60)
    print("Concluído com sucesso!")
    print("=" * 60)


if __name__ == "__main__":
    main()
