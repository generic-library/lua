#!/usr/bin/python
# --------------------------------------------------------
# -- Linear Math librairy
# --------------------------------------------------------
import lutinModule as module
import lutinTools as tools

def get_desc():
	return "Lua Lua interpretic script module"


def create(target):
	myModule = module.Module(__file__, 'lua', 'LIBRARY')
	
	myModule.add_module_depend('etk')
	
	myModule.compile_flags_CC([
		'-DLUA_VERSION_TAG_NAME="\"5.2\""',
		'-Wall'])
	
	myModule.add_export_path(tools.get_current_path(__file__))
	myModule.add_path(tools.get_current_path(__file__)+"/lua/")
	
	
	myModule.add_export_flag_CC('-DLUA_COMPAT_ALL');
	
	#ifeq ("$(TARGET_OS)","Windows")
	#	myModule.compile_flags_CC('-D_WIN32')
	#else
	myModule.compile_flags_CC('-DLUA_USE_LINUX')
	#endif
	
	
	myModule.add_src_file([
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
	return myModule



