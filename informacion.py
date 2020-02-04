import platform
info = []
info.append("SO: "+platform.system())
info.append("Version SO: "+platform.release())
info.append("Build SO: "+platform.version())
info.append("Procesador: "+platform.processor().split(" ")[0])
info.append("Arquitectura: "+platform.architecture()[0])
info.append("Python "+platform.python_version())
print(info)