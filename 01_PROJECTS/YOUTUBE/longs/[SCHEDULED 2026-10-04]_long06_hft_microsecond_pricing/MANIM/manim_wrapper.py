"""
Manim CLI Runner Wrapper with Regex-Safe Warning Filter
Resolves standard library re.error when file paths contain bracketed dates like [IN_PROGRESS 2026-09-30].
"""
import warnings, re, sys, os

orig = warnings.filterwarnings
def safe_fw(action, message="", category=Warning, module="", lineno=0, append=False):
    if isinstance(module, str):
        try:
            re.compile(module)
        except re.error:
            module = re.escape(module)
    return orig(action, message=message, category=category, module=module, lineno=lineno, append=append)
warnings.filterwarnings = safe_fw

# Ensure YouTube root is on sys.path
MANIM_DIR = os.path.dirname(os.path.abspath(__file__))
EPISODE_DIR = os.path.abspath(os.path.join(MANIM_DIR, ".."))
YOUTUBE_DIR = os.path.abspath(os.path.join(EPISODE_DIR, "..", ".."))
if YOUTUBE_DIR not in sys.path:
    sys.path.insert(0, YOUTUBE_DIR)

import manim.__main__

if __name__ == "__main__":
    manim.__main__.main()
