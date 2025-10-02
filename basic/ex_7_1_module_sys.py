import sys

print(sys.argv)
print("---")

print("getwindowsversion()", sys.getwindowsversion())
print("---")
print("copyright", sys.copyright)
print("---")
print("version", sys.version)
print("---")
print("path", sys.path)
print("---")
print("platform", sys.platform)
print("---")
print("maxsize", sys.maxsize)
print("---")
print("executable", sys.executable)
print("---")
print("getdefaultencoding()", sys.getdefaultencoding())
print("---")
print("getrecursionlimit()", sys.getrecursionlimit())

sys.exit()