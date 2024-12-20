#!/usr/bin/python
import os
import ctypes

current_dir = os.path.dirname(os.path.abspath(__file__))
dll_path = os.path.join(current_dir, 'include', 'SunplusCamera_x64.dll')

class CameraController:
    def __init__(self):
        self._exposure_level = 210
        self._hllDll = ctypes.CDLL(dll_path)

        # Set DLL Function camera_init
        self._camera_init = self._hllDll.SunplusCam_Init
        self._camera_init.argtypes = [ctypes.c_int]
        self._camera_init.restypes = ctypes.c_int
        self._nRst = self._camera_init(0)

        # Set DLL Function get_sensor_reg
        self._get_sensor_reg = self._hllDll.GetSensorRegister
        self._get_sensor_reg.argtypes = [ctypes.c_byte, ctypes.c_ushort, ctypes.POINTER(ctypes.c_ushort)]
        self._get_sensor_reg.restypes = ctypes.c_int

        # Set DLL Function set_sensor_reg
        self._set_sensor_reg = self._hllDll.SetSensorRegister
        self._set_sensor_reg.argtypes = [ctypes.c_byte, ctypes.c_ushort, ctypes.c_ushort]
        self._set_sensor_reg.restypes = ctypes.c_int

    def get_sensor_reg(self, address):
        slave_id = ctypes.c_byte(0)
        reg_addr = ctypes.c_ushort(address)
        reg_value = ctypes.c_ushort()
        nRst = self._get_sensor_reg(slave_id, reg_addr, reg_value)
        return reg_value

    def set_sensor_reg(self, address, value):
        slave_id = ctypes.c_byte(0)
        reg_addr = ctypes.c_ushort(address)
        reg_value = ctypes.c_ushort(value)
        nRst = self._set_sensor_reg(slave_id, reg_addr, reg_value)
        return

    def get_exposure_level(self):
        return self._exposure_level

    def set_exposure_level(self, level):
        if 0 <= level <= 320:
            self._exposure_level = level
            if level <= 160:
                self.set_sensor_reg(0x07, 0x01)
                self.set_sensor_reg(0x04, level)
            elif 160 < level <= 240:
                self.set_sensor_reg(0x07, 0x02)
                self.set_sensor_reg(0x04, level-81)
            elif level > 240:
                self.set_sensor_reg(0x07, 0x03)
                self.set_sensor_reg(0x04, level-161)
        return

    def increase_exposure_level(self, increase):
        self.set_exposure_level(self._exposure_level + increase)
        return

    def decrease_exposure_level(self, decrease):
        self.set_exposure_level(self._exposure_level - decrease)
        return
