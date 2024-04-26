import sys


class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False


ANY = AnyType("*")


class Field:
    @staticmethod
    def field(field: str | list, data: dict = None) -> tuple[str | list, dict] | tuple[str | list]:
        if data:
            return (field, data,)
        return (field,)

    @staticmethod
    def boolean(
            default: float = False, force: bool = False
    ) -> tuple[str, dict]:
        field_data = {"default": default, "force": force}
        return Field.field("BOOLEAN", field_data)

    @staticmethod
    def float(
            default: float = 1, min: float = -sys.float_info.max, max: float = sys.float_info.max, step: float = 0.01,
            force: bool = False
    ) -> tuple[str, dict]:
        field_data = {"default": default, "min": min, "max": max, "step": step, "forceInput": force}
        return Field.field("FLOAT", field_data)

    @staticmethod
    def int(
            default: int = 1, min: int = -sys.maxsize, max: int = sys.maxsize, step: int = 1, force: bool = False
    ) -> tuple[str, dict]:
        field_data = {"default": default, "min": min, "max": max, "step": step, "forceInput": force}
        return Field.field("INT", field_data)

    @staticmethod
    def string(
            default: str = '',
            multiline: bool = False,
            force: bool = False,
            dynamicPrompts: bool = False
    ) -> tuple[str, dict]:
        field_data = {"default": default, 'multiline': multiline, "forceInput": force, "dynamicPrompts": dynamicPrompts}
        return Field.field("STRING", field_data)

    @staticmethod
    def any():
        return Field.field(ANY, {"forceInput": False})

    @staticmethod
    def latent(force: bool = False):
        field_data = {"forceInput": force}
        return Field.field("LATENT", field_data)

    @staticmethod
    def image(force: bool = False):
        field_data = {"forceInput": force}
        return Field.field("IMAGE", field_data)

    @staticmethod
    def model(force: bool = False):
        field_data = {"forceInput": force}
        return Field.field("MODEL", field_data)

    @staticmethod
    def lora(force: bool = False):
        field_data = {"forceInput": force}
        return Field.field("LORA", field_data)

    @staticmethod
    def vae(force: bool = False):
        field_data = {"forceInput": force}
        return Field.field("VAE", field_data)

    @staticmethod
    def conditioning(force: bool = False):
        field_data = {"forceInput": force}
        return Field.field("CONDITIONING", field_data)

    @staticmethod
    def clip(force: bool = False):
        field_data = {"forceInput": force}
        return Field.field("CLIP", field_data)

    @staticmethod
    def combo(data: list, force: bool = False):
        field_data = {"forceInput": force}
        return Field.field(data, field_data)
