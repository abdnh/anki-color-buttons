import functools
from typing import List

from aqt import gui_hooks, mw
from aqt.editor import Editor


def add_buttons(buttons: List[str], editor: Editor) -> None:
    config = mw.addonManager.getConfig(__name__)

    def set_color(editor: Editor, color: str) -> None:
        editor.web.eval(f"setFormat('forecolor', '{color}')")

    for i, data in enumerate(config["text_colors"]):
        color = data["color"]
        shortcut = data["shortcut"]
        tip = f"Set text color to {color}" + (f" ({shortcut})" if shortcut else "")
        buttons.append(
            editor.addButton(
                icon=None,
                cmd=f"text_color{i}",
                func=functools.partial(set_color, color=color),
                tip=tip,
                label=f"<span style='color: {color}'>C</span>",
                keys=shortcut,
            )
        )


gui_hooks.editor_did_init_buttons.append(add_buttons)
