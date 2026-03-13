import re
import textwrap
import traceback
import types
from mkdocs.plugins import BasePlugin
import pythagoras


class GeometryPlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        pattern = re.compile(r"\[\{(.*?)\}\]", re.DOTALL)

        def compile_svg(match):
            raw_code = match.group(1)
            code = textwrap.dedent(raw_code).strip()
            ctx = pythagoras.Canvas(500, 500)
            namespace = {"ctx": ctx}
            namespace.update(
                {
                    k: v
                    for k, v in vars(pythagoras).items()
                    if not k.startswith("_") and not isinstance(v, types.ModuleType)
                }
            )
            try:
                exec(code, namespace, namespace)
                return f'<div align="center">{ctx.svg()}</div>'
            except Exception as e:
                print(f"\n[Geometry] Error compiling SVG in {page.file.src_path}:")
                traceback.print_exc()
                return f"\n```python\n{code}\n```"

        return pattern.sub(compile_svg, markdown)
