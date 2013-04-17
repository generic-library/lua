#!/usr/bin/python
# --------------------------------------------------------
# -- Linear Math librairy
# --------------------------------------------------------
import module
import buildTools

myModule = module.module(__file__, 'lua', 'LIBRARY')

myModule.AddModuleDepend('etk')

myModule.CompileFlags_CC([
	'-DLUA_VERSION_TAG_NAME="\"5.2\""',
	'-Wall'])

myModule.AddExportPath(buildTools.GetCurrentPath(__file__))
myModule.AddPath(buildTools.GetCurrentPath(__file__)+"/lua/")


myModule.AddExportFlag_CC('-DLUA_COMPAT_ALL');

#ifeq ("$(TARGET_OS)","Windows")
#	myModule.CompileFlags_CC('-D_WIN32')
#else
myModule.CompileFlags_CC('-DLUA_USE_LINUX')
#endif


myModule.AddSrcFile([
	'lua/lapi.cpp',
	'lua/lauxlib.cpp',
	'lua/lbaselib.cpp',
	'lua/lbitlib.cpp',
	'lua/lcode.cpp',
	'lua/lcorolib.cpp',
	'lua/lctype.cpp',
	'lua/ldblib.cpp',
	'lua/ldebug.cpp',
	'lua/ldo.cpp',
	'lua/ldump.cpp',
	'lua/lfunc.cpp',
	'lua/lgc.cpp',
	'lua/linit.cpp',
	'lua/liolib.cpp',
	'lua/llex.cpp',
	'lua/lmathlib.cpp',
	'lua/lmem.cpp',
	'lua/loadlib.cpp',
	'lua/lobject.cpp',
	'lua/lopcodes.cpp',
	'lua/loslib.cpp',
	'lua/lparser.cpp',
	'lua/lstate.cpp',
	'lua/lstring.cpp',
	'lua/lstrlib.cpp',
	'lua/ltable.cpp',
	'lua/ltablib.cpp',
	'lua/ltm.cpp',
	'lua/lundump.cpp',
	'lua/lvm.cpp',
	'lua/lzio.cpp'])



# add the currrent module at the 
module.AddModule(myModule)



