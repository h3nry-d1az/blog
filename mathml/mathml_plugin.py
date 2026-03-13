import re
from mkdocs.plugins import BasePlugin
import latex2mathml.converter


class MathMLPlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        block_pattern = re.compile(r"(?<!\\)\$\$(.*?)\$\$", re.DOTALL)
        inline_pattern = re.compile(r"(?<!\\)\$(?!\s)(.+?)(?<!\s)\$")

        def replace_block(match):
            latex_code = match.group(1).strip()
            try:
                return latex2mathml.converter.convert(latex_code, display="block")
            except Exception as e:
                return f"\n{match.group(0)}"

        def replace_inline(match):
            latex_code = match.group(1).strip()
            try:
                return latex2mathml.converter.convert(latex_code, display="inline")
            except Exception as e:
                return f"{match.group(0)}"

        markdown = block_pattern.sub(replace_block, markdown)
        markdown = inline_pattern.sub(replace_inline, markdown)

        return markdown
