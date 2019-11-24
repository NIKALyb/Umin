#подключение библиотек
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#вывод в чат
for i in range(20):
    mc.postToChat("SALAM")
