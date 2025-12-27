#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  blockedips.py
import ipaddress

class CheckIp():
    def __init__(self):
        self.__tpl_fbd = ( '79.137.156.0/24',
                           '79.137.143.0/24',
                           '95.163.144.0/24',
                           '89.208.31.0/24', 
                           '79.137.130.0/24',
                           '79.137.138.0/24',
                           '79.137.151.0/24',
                           '79.137.142.0/24',
                           '81.177.172.0/24',
                           '81.177.173.0/24',
                        )

    def isForbidden(self, ip: str) -> bool:
        """
        Проверяет, принадлежит ли указанный IP-адрес к запрещенному диапазону.

        Параметры:
          ip (str): IP-адрес в строковом формате.

        Возвращает:
          bool: True, если IP-адрес принадлежит к запрещенному диапазону, иначе False.
        """
        for i in self.__tpl_fbd:
            network = ipaddress.ip_network(i)
            if ipaddress.ip_address(ip) in network:
                return True
        return False
    
"""
Nessly Company
https://myip.ms/view/ip_owners/630251/Nessly_Company.html#a
79.137.156.0 - 79.137.156.255
79.137.143.0 - 79.137.143.255
95.163.144.0 - 95.163.144.255
89.208.31.0 - 89.208.31.255
79.137.130.0 - 79.137.130.255
79.137.138.0 - 79.137.138.255
79.137.151.0 - 79.137.151.255
79.137.142.0 - 79.137.142.255

KRIBRUM
81.177.172.0 - 81.177.173.255

95.163.144.228 - vseodnoklasniki.com
95.163.144.228 - 95.163.144.228
"""
