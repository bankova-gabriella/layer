import time

from lib.layer import Layer

# time
start = time.time()

layer = Layer()

layer.mold_brics()

# execute selected brics
layer.lay_brics()

# build docker images

# time
end = time.time()
print('Seconds to complete whole program', end - start)
