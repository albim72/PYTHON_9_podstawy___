import pickle

class PickleBoom:
    def __reduce__(self):
        import os
        return (os.system,('echo BOOM!',))

boom = PickleBoom()
pb = pickle.dumps(boom)

unp_b = pickle.loads(pb)
