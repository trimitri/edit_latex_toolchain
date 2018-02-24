edit\_latex\_toolchain
======================
This is an Anki 2.1 Plugin to customize the LaTeX build process.
It is basically a copy of [this existing plugin](https://ankiweb.net/shared/info/937148547) which wasn't compatible with Anki 2.1 at the time.

The Plugin is also uploaded to [AnkiWeb](https://ankiweb.net/shared/info/933614828).

Installation
------------
This plugin is compatible with Anki 2.1. I didn't test it in 2.0 ([Issue #2](https://github.com/trimitri/edit_latex_toolchain/issues/2)).

### Manual Installation
To use the plugin, first find your Anki 2.1 plugin folder.
In Arch Linux, it resides here:

    ~/.local/share/Anki2/addons21/

If you just clone this repository into that folder and restart Anki, everything
should work out of the box.
Your directory structure would look as follows:

    ~/.local/share/Anki2/addons21/edit_latex_toolchain/<files you see here>

Please let me know if it doesn't work or if you have tried it under Windows or
Mac and can give info.

### AnkiWeb installation
You can also get the Plugin straigt from AnkiWeb to your client:
https://ankiweb.net/shared/info/933614828

Usage
-----
Adjust the commands in `edit_latex_toolchain.py` to your needs.
Anki 2.1 can be configured to either generate png or svg graphics.
Depending on what method you choose, find the appropriate code block.
Each line is executed one after another.

For debugging your custom LaTeX toolchain, consider having a look at the
generated code and results at `/tmp/anki_temp/` (or somewhere else in Windows).

Notes
-----
Anki 2.1 does support _MathJax_ for math rendering.
It works for me across AnkiDroid and Anki 2.1 on desktop.
