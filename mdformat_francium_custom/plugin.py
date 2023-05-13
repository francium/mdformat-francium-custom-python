from typing import Mapping

from markdown_it import MarkdownIt
from mdformat.renderer import RenderContext, RenderTreeNode
from mdformat.renderer._context import make_render_children
from mdformat.renderer.typing import Render

# Nothing needs to be done here, but because the only way to do what we're
# doing here is by defining a mdformat parser plugin, this update_mdit is part
# of the parser plugin interface and must be defined, even if it does nothing
def update_mdit(_mdit: MarkdownIt) -> None:
    pass


def _make_render_children_root() -> Render:
    f = make_render_children("\n\n")

    def render_children(
        node: RenderTreeNode,
        context: RenderContext,
    ) -> str:
        return f(node, context).strip()

    return render_children


RENDERERS: Mapping[str, Render] = {
    "root": _make_render_children_root(),
}
