LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

# name of the librairy
LOCAL_MODULE := lua

# name of the dependency
LOCAL_STATIC_LIBRARIES := etk

LOCAL_C_INCLUDES := $(LOCAL_PATH) $(LOCAL_PATH)/lua/

LOCAL_EXPORT_C_INCLUDES := $(LOCAL_PATH)

LOCAL_CFLAGS := -DLUA_COMPAT_ALL \
                -DLUA_USE_LINUX \
                -DLUA_VERSION_TAG_NAME="\"5.2-$(BUILD_DIRECTORY_MODE)\""

# load the common sources file of the platform
include $(LOCAL_PATH)/file.mk

LOCAL_SRC_FILES := $(FILE_LIST)

include $(BUILD_STATIC_LIBRARY)


