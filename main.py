"""Transcrição do pseudocódigo para Python.

Este exemplo implementa o padrão Bridge: uma hierarquia de
abstração (RemoteControl) que mantém uma referência para a
hierarquia de implementação (Device). Comentários e nomes
estão em português para manter consistência com o original.
"""

from abc import ABC, abstractmethod
from typing import Optional


class Device(ABC):
    """Interface 'implementação' que todos os dispositivos seguem."""

    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def get_volume(self) -> int:
        pass

    @abstractmethod
    def set_volume(self, percent: int) -> None:
        pass

    @abstractmethod
    def get_channel(self) -> int:
        pass

    @abstractmethod
    def set_channel(self, channel: int) -> None:
        pass


class Tv(Device):
    def __init__(self) -> None:
        self._enabled = False
        self._volume = 30
        self._channel = 1

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        self._enabled = True
        print("TV: ligada")

    def disable(self) -> None:
        self._enabled = False
        print("TV: desligada")

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int) -> None:
        self._volume = max(0, min(100, percent))
        print(f"TV: volume ajustado para {self._volume}%")

    def get_channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int) -> None:
        self._channel = max(1, channel)
        print(f"TV: canal ajustado para {self._channel}")


class Radio(Device):
    def __init__(self) -> None:
        self._enabled = False
        self._volume = 50
        self._channel = 1  # para rádio, pode ser frequência em outra implementação

    def is_enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        self._enabled = True
        print("Rádio: ligado")

    def disable(self) -> None:
        self._enabled = False
        print("Rádio: desligado")

    def get_volume(self) -> int:
        return self._volume

    def set_volume(self, percent: int) -> None:
        self._volume = max(0, min(100, percent))
        print(f"Rádio: volume ajustado para {self._volume}%")

    def get_channel(self) -> int:
        return self._channel

    def set_channel(self, channel: int) -> None:
        self._channel = max(1, channel)
        print(f"Rádio: canal ajustado para {self._channel}")


class RemoteControl:
    """A 'abstração' que delega o trabalho ao Device."""

    def __init__(self, device: Device) -> None:
        self.device = device

    def toggle_power(self) -> None:
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self) -> None:
        self.device.set_volume(self.device.get_volume() - 10)

    def volume_up(self) -> None:
        self.device.set_volume(self.device.get_volume() + 10)

    def channel_down(self) -> None:
        self.device.set_channel(self.device.get_channel() - 1)

    def channel_up(self) -> None:
        self.device.set_channel(self.device.get_channel() + 1)


class AdvancedRemoteControl(RemoteControl):
    """Extensão da abstração com funcionalidades adicionais."""

    def mute(self) -> None:
        self.device.set_volume(0)


if __name__ == "__main__":
    # Demonstração rápida
    tv = Tv()
    remote = RemoteControl(tv)
    print("-- Controle remoto simples sobre TV --")
    remote.toggle_power()   # liga
    remote.volume_up()
    remote.channel_up()
    remote.toggle_power()   # desliga

    print("\n-- Controle remoto avançado sobre Rádio --")
    radio = Radio()
    advanced = AdvancedRemoteControl(radio)
    advanced.toggle_power()
    advanced.volume_down()
    advanced.mute()
    advanced.toggle_power()
