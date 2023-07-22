class ContextRegistry:
    """Registers classes from apps for use in context"""
    __registry = {}

    @classmethod
    def register(cls, url_name):
        def registrar(wrapped_class):
            cls.__registry[url_name] = wrapped_class
            return wrapped_class
        return registrar

    def __getitem__(self, key):
        return self.__registry[key]

    def __contains__(self, key):
        if key in self.__registry:
            return True
        return False
