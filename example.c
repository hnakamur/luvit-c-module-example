#include <lauxlib.h>
#include <math.h>

static int l_sin(lua_State *L) {
  double d = luaL_checknumber(L, 1);
  lua_pushnumber(L, sin(d));
  return 1;
}

static const struct luaL_Reg example[] = {
  {"sin", l_sin},
  {NULL, NULL}
};

int luaopen_example(lua_State *L) {
  luaL_register(L, "example", example);
  return 1;
}
