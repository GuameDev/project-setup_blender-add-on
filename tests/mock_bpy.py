# tests/mock_bpy.py

class Props:
    def StringProperty(self, name="", default=""):
        return default

class BpyTypes:
    class Operator:
        pass

class BpyMock:
    types = BpyTypes()
    props = Props()

bpy = BpyMock()
