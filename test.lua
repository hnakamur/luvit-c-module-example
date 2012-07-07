local example = require("example")
local math = require("math")

assert(example.sin(0) == 0)
assert(math.abs(example.sin(0.5) - 0.4794255386042) < 1e-14)
