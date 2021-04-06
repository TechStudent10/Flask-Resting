class ResourceIsNotInherited(Exception):
    def __init__(self):
        super().__init__("Resource is not inherited from the 'Resource' class.")
