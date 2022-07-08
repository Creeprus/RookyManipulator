#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
"""Пример работы с манипулятором Rooky."""

__author__ = "Promobot"
__license__ = "Apache License, Version 2.0"
__status__ = "Production"
__url__ = "https://git.promo-bot.ru"
__version__ = "0.1.0"

# Импортируем необходимые библиотеки
# Библиотека для работы с Rooky версии 2
import Rooky2

# Библиотеsка для работы с временными задержками
import time

# Укажем тип Rooky left или right
side = "left"
# Создадим объект Rooky в соответствии с его типом: левая или правая
# '/dev/RS_485' - последовательный порт, для ubuntu по умолчанию - '/dev/RS_485'.
arm = Rooky2.Rooky('COM2', side)

arm.reset_joints()
