#подключение библиотек
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#вывод в чат
for i in range(10):
    mc.postToChat("SALAM")
