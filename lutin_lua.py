#!/usr/bin/python
import realog.debug as debug
import lutin.tools as tools


def get_type():
	return "LIBRARY"

def get_desc():
	return "Lua interpretic script module"

def get_licence():
	return "MIT"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "lua"

def get_maintainer():
	return "authors.txt"

def get_version():
	return "version.txt"

def configure(target, my_module):
	my_module.add_depend([
	    'elog',
	    'etk',
	    ])
	
	my_module.add_flag('c', [
		'-DLUA_VERSION_TAG_NAME="\"5.2\""',
		'-Wall',
		])
	
	my_module.add_flag('c', '-DLUA_COMPAT_ALL', export=True);
	
	#ifeq ("$(TARGET_OS)","Windows")
	#	my_module.compile_flags_CC('-D_WIN32')
	#else
	my_module.add_flag('c', '-DLUA_USE_LINUX')
	#endif
	
	my_module.add_src_file([
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
	    'lua/lzio.cpp',
	    ])
	
	my_module.add_header_file([
	    'lua/ltm.h',
	    'lua/llimits.h',
	    'lua/lctype.h',
	    'lua/lgc.h',
	    'lua/lstring.h',
	    'lua/lzio.h',
	    'lua/lmem.h',
	    'lua/lobject.h',
	    'lua/lvm.h',
	    'lua/ldebug.h',
	    'lua/lundump.h',
	    'lua/lcode.h',
	    'lua/ltable.h',
	    'lua/lfunc.h',
	    'lua/lparser.h',
	    'lua/lopcodes.h',
	    'lua/lua.h',
	    'lua/ldo.h',
	    'lua/llex.h',
	    'lua/lapi.h',
	    'lua/lstate.h',
	    'lua/lualib.h',
	    'lua/lauxlib.h',
	    'lua/luaconf.h',
	    ])

	my_module.compile_version('c', 1999, gnu=False)
	
	return True



