# http://tinyurl.com/jkaorle

class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        # clients can use this
        print("You can use the 'public_method' with confidence.\n")
        pass

    def _unsafe_method(self):
        #clients should NOT use this
        print("Use the '_unsafe_method' at your own risk.\n")
        pass

ex1 = PublicPrivateExample()
ex1.public_method()
ex1._unsafe_method()
