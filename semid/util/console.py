import ctypes, textwrap, os
class Console:
    @staticmethod
    def color(text) -> str:
        try:
            text = str(text)
        except:
            pass
        return "\033[96m{}\033[0m".format(text)

    def set_title(title:str) -> bool:
        import sys
        sys.stdout.flush()
        if os.name == "nt":
            return ctypes.windll.kernel32.SetConsoleTitleA(title.encode())
        else:
            return print("\x1b]0;"+title.encode(), end="\a")
    def center(text:str) -> str:
        lines = textwrap.wrap(text)
        return "\n".join(line.center(100) for line in lines)
    def red(text:str) -> str:
        return f"\033[31m{text}\033[0m"
    def green(text:str) -> str:
        return f"\033[32m{text}\033[0m"
