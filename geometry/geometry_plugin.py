import re
import textwrap
import traceback
from mkdocs.plugins import BasePlugin
from pythagoras import prelude as gm


def update_namespace(ns, mod):
    ns.update({k: v for k, v in vars(mod).items() if not k.startswith("_")})


class GeometryPlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        pattern = re.compile(r"\[\{(.*?)\}\]", re.DOTALL)

        def compile_svg(match):
            raw_code = match.group(1)
            code = textwrap.dedent(raw_code).strip()
            ctx = gm.Canvas()
            namespace = {"ctx": ctx}
            update_namespace(namespace, gm)
            update_namespace(namespace, gm.color)
            update_namespace(namespace, gm.draw)
            update_namespace(namespace, gm.line)
            update_namespace(namespace, gm.opacity)
            try:
                exec(code, namespace, namespace)
                return f'<div align="center">{ctx.svg()}</div>'
            except Exception:
                print(f"\n[Geometry] Error compiling SVG in {page.file.src_path}:")
                traceback.print_exc()
                return f"\n```python\n{code}\n```"

        return pattern.sub(compile_svg, markdown)
