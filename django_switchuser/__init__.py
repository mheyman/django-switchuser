def version2str(ver):
    ver = [x for x in map(str, ver)]
    return ".".join(ver[:3]) + "".join(ver[3:])

__version__ = (0, 6, 2)

version_str = version2str(__version__)
