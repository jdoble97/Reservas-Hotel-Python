import ctypes

def getResolucion():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    resolucion = str(round(ancho*0.8))+"x"+str(round(alto*0.8))
    return resolucion