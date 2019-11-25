import ctypes

_dsl = ctypes.CDLL('dsl-lib.so')

DSL_RETURN_SUCCESS = 0

##
## dsl_source_csi_new()
##
_dsl.dsl_source_csi_new.argtypes = \
    [ctypes.c_wchar_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint]
_dsl.dsl_source_csi_new.restype = ctypes.c_uint
def dsl_source_csi_new(name, width, height, fps_n, fps_d):
    global _dsl
    result =_dsl.dsl_source_csi_new(name, width, height, fps_n, fps_d)
    return int(result)
#print(dsl_source_csi_new("csi-source", 1280, 720, 30, 1))

##
## dsl_source_uri_new()
##
_dsl.dsl_source_uri_new.argtypes = \
    [ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint]
_dsl.dsl_source_uri_new.restype = ctypes.c_uint
def dsl_source_uri_new(name, uri, cudadec_mem_type, intra_decode, drop_frame_interval):
    global _dsl
    result =_dsl.dsl_source_uri_new(name, uri, cudadec_mem_type, intra_decode, drop_frame_interval)
    return int(result)
#print(dsl_source_uri_new("uri-source", "../../test/streams/sample_1080p_h264.mp4", 0, 0, 0))

##
## dsl_source_is_live()
##
_dsl.dsl_source_is_live.argtypes = [ctypes.c_wchar_p]
_dsl.dsl_source_is_live.restype = ctypes.c_bool
def dsl_source_is_live(name):
    global _dsl
    result =_dsl.dsl_source_is_live(name)
    return bool(result)
#print(dsl_source_is_live("uri-source"))

##
## dsl_source_get_num_in_use()
##
_dsl.dsl_source_get_num_in_use.restype = ctypes.c_uint
def dsl_source_get_num_in_use():
    global _dsl
    result =_dsl.dsl_source_get_num_in_use()
    return int(result)
#print(dsl_source_get_num_in_use())

##
## dsl_source_get_num_in_use_max()
##
_dsl.dsl_source_get_num_in_use_max.restype = ctypes.c_uint
def dsl_source_get_num_in_use_max():
    global _dsl
    result =_dsl.dsl_source_get_num_in_use_max()
    return int(result)
#print(dsl_source_get_num_in_use_max())

##
## dsl_source_set_num_in_use_max()
##
_dsl.dsl_source_set_num_in_use_max.argtypes = [ctypes.c_uint]
def dsl_source_set_num_in_use_max(max):
    global _dsl
    result =_dsl.dsl_source_set_num_in_use_max(max)
dsl_source_set_num_in_use_max(20)
#print(dsl_source_get_num_in_use_max())

##
## dsl_sink_overlay_new()
##
_dsl.dsl_sink_overlay_new.argtypes = \
    [ctypes.c_wchar_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint, ctypes.c_uint]
_dsl.dsl_sink_overlay_new.restype = ctypes.c_uint
def dsl_sink_overlay_new(name, offsetX, offsetY, width, height):
    global _dsl
    result =_dsl.dsl_sink_overlay_new(name, offsetX, offsetY, width, height)
    return int(result)
#print(dsl_sink_overlay_new("overlay-sink", 0, 0, 1280, 720))

##
## dsl_osd_new()
##
_dsl.dsl_osd_new.argtypes = [ctypes.c_wchar_p, ctypes.c_bool]
_dsl.dsl_osd_new.restype = ctypes.c_uint
def dsl_osd_new(name, is_clock_enabled):
    global _dsl
    result =_dsl.dsl_osd_new(name, is_clock_enabled)
    return int(result)
#print(dsl_osd_new("on-screen-display", False))

##
## dsl_gie_primary_new()
##
_dsl.dsl_gie_primary_new.argtypes = \
    [ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint, ctypes.c_uint]
_dsl.dsl_gie_primary_new.restype = ctypes.c_uint
def dsl_gie_primary_new(name, infer_config_file, model_engine_file, interval, unique_id):
    global _dsl
    result =_dsl.dsl_gie_primary_new(name, infer_config_file, model_engine_file, interval, unique_id)
    return int(result)
#print(dsl_gie_primary_new("primary-gie", "../../test/configs/config_infer_primary_nano.txt", 
#    "../../test/models/Primary_Detector_Nano/resnet10.caffemodel", 0, 0))

##
## dsl_display_new()
##
_dsl.dsl_display_new.argtypes = \
    [ctypes.c_wchar_p, ctypes.c_uint, ctypes.c_uint]
_dsl.dsl_display_new.restype = ctypes.c_uint
def dsl_display_new(name, width, height):
    global _dsl
    result =_dsl.dsl_display_new(name, width, height)
    return int(result)
#print(dsl_display_new("tiled-display", 1280, 720))

##
## dsl_component_delete()
##
_dsl.dsl_component_delete.argtypes = [ctypes.c_wchar_p]
_dsl.dsl_component_delete.restype = ctypes.c_uint
def dsl_component_delete(name):
    global _dsl
    result =_dsl.dsl_component_delete(name)
    return int(result)
#print(dsl_component_delete("tiled-display"))

##
## dsl_component_delete_many()
##
#_dsl.dsl_component_delete_many.argtypes = [Array]
_dsl.dsl_component_delete_many.restype = ctypes.c_uint
def dsl_component_delete_many(components):
    global _dsl
    arr = (ctypes.c_wchar_p * len(components))()
    arr[:] = components
    result =_dsl.dsl_component_delete_many(arr)
    return int(result)
#print(dsl_component_delete_many(["on-screen-display", "primary-gie", None]))

##
## dsl_component_delete_all()
##
_dsl.dsl_component_delete_all.restype = ctypes.c_uint
def dsl_component_delete_all():
    global _dsl
    result =_dsl.dsl_component_delete_all()
    return int(result)
#print(dsl_component_delete_all())

##
## dsl_component_list_size()
##
_dsl.dsl_component_list_size.restype = ctypes.c_uint
def dsl_component_list_size():
    global _dsl
    result =_dsl.dsl_component_list_size()
    return int(result)
#print(dsl_component_list_size())

##
## dsl_component_list_all()
##
# _dsl.dsl_component_list_size.restype = ctypes.POINTER(ctypes.c_wchar_p)
def dsl_component_list_all():
    global _dsl
    result = _dsl.dsl_component_list_all()

#print(dsl_osd_new("on-screen-display-1", False))
#print(dsl_osd_new("on-screen-display-2", False))
#print(dsl_component_list_size())
#result = dsl_component_list_all()
#index = 0
#while True:
#    p = result[index]
#    if p is None:
#        break
#    index += 1
#    print(p)

##
## dsl_pipeline_new()
##
_dsl.dsl_pipeline_new.argtypes = [ctypes.c_wchar_p]
_dsl.dsl_pipeline_new.restype = ctypes.c_uint
def dsl_pipeline_new(name):
    global _dsl
    result =_dsl.dsl_pipeline_new(name)
    return int(result)
#print(dsl_pipeline_new("pipeline-1"))

##
## dsl_pipeline_new_many()
##
#_dsl.dsl_pipeline_new_many.argtypes = []
_dsl.dsl_pipeline_new_many.restype = ctypes.c_uint
def dsl_pipeline_new_many(pipelines):
    global _dsl
    arr = (ctypes.c_wchar_p * len(pipelines))()
    arr[:] = pipelines
    result =_dsl.dsl_pipeline_new_many(arr)
    return int(result)
#print(dsl_pipeline_new_many(["pipeline-2", "pipeline-3", "pipeline-4", None]))

##
## dsl_pipeline_delete()
##
_dsl.dsl_pipeline_delete.argtypes = [ctypes.c_wchar_p]
_dsl.dsl_pipeline_delete.restype = ctypes.c_uint
def dsl_pipeline_delete(name):
    global _dsl
    result =_dsl.dsl_pipeline_delete(name)
    return int(result)

##
## dsl_pipeline_delete_many()
##
#_dsl.dsl_component_delete_many.argtypes = [Array]
_dsl.dsl_pipeline_delete_many.restype = ctypes.c_uint
def dsl_pipeline_delete_many(pipelines):
    global _dsl
    arr = (ctypes.c_wchar_p * len(pipelines))()
    arr[:] = pipelines
    result =_dsl.dsl_pipeline_delete_many(arr)
    return int(result)
#print(dsl_pipeline_delete_many(["pipeline-2", "pipeline-3", None]))

##
## dsl_pipeline_delete_all()
##
_dsl.dsl_pipeline_delete_all.restype = ctypes.c_uint
def dsl_pipeline_delete_all():
    global _dsl
    result =_dsl.dsl_pipeline_delete_all()
    return int(result)
#print(dsl_pipeline_delete_all())

##
## dsl_pipeline_list_size()
##
_dsl.dsl_pipeline_list_size.restype = ctypes.c_uint
def dsl_pipeline_list_size():
    global _dsl
    result =_dsl.dsl_pipeline_list_size()
    return int(result)
#print(dsl_pipeline_list_size())

##
## dsl_pipeline_component_add()
##
_dsl.dsl_pipeline_component_add.argtypes = [ctypes.c_wchar_p, ctypes.c_wchar_p]
_dsl.dsl_pipeline_component_add.restype = ctypes.c_uint
def dsl_pipeline_component_add(pipeline, component):
    global _dsl
    result =_dsl.dsl_pipeline_component_add(pipeline, component)
    return int(result)
#print(dsl_display_new("tiled-display", 1280, 720))
#print(dsl_pipeline_new("pipeline-1"))
#print(dsl_pipeline_component_add("pipeline-1", "tiled-display"))

##
## dsl_pipeline_component_add_many()
##
#_dsl.dsl_pipeline_component_add_many.argtypes = [ctypes.c_wchar_p, ctypes.c_wchar_p]
_dsl.dsl_pipeline_component_add_many.restype = ctypes.c_uint
def dsl_pipeline_component_add_many(pipeline, components):
    global _dsl
    arr = (ctypes.c_wchar_p * len(components))()
    arr[:] = components
    result =_dsl.dsl_pipeline_component_add_many(pipeline, arr)
    return int(result)
#print(dsl_display_new("tiled-display-2", 1280, 720))
#print(dsl_pipeline_new("pipeline-2"))
#print(dsl_pipeline_component_add_many("pipeline-2", ["tiled-display-2", None]))

##
## dsl_pipeline_pause()
##
_dsl.dsl_pipeline_pause.argtypes = [ctypes.c_wchar_p]
_dsl.dsl_pipeline_pause.restype = ctypes.c_uint
def dsl_pipeline_pause(name):
    global _dsl
    result =_dsl.dsl_pipeline_pause(name)
    return int(result)
#print(dsl_pipeline_pause("pipeline-1"))

##
## dsl_pipeline_play()
##
_dsl.dsl_pipeline_play.argtypes = [ctypes.c_wchar_p]
_dsl.dsl_pipeline_play.restype = ctypes.c_uint
def dsl_pipeline_play(name):
    global _dsl
    result =_dsl.dsl_pipeline_play(name)
    return int(result)
#print(dsl_pipeline_play("pipeline-1"))

##
## dsl_pipeline_stop()
##
_dsl.dsl_pipeline_stop.argtypes = [ctypes.c_wchar_p]
_dsl.dsl_pipeline_stop.restype = ctypes.c_uint
def dsl_pipeline_stop(name):
    global _dsl
    result =_dsl.dsl_pipeline_stop(name)
    return int(result)
#print(dsl_pipeline_stop("pipeline-1"))

##
## dsl_pipeline_dump_to_dot()
##
_dsl.dsl_pipeline_dump_to_dot.argtypes = [ctypes.c_wchar_p, ctypes.c_wchar_p]
_dsl.dsl_pipeline_dump_to_dot.restype = ctypes.c_uint
def dsl_pipeline_dump_to_dot(pipeline, filename):
    global _dsl
    result =_dsl.dsl_pipeline_dump_to_dot(pipeline, filename)
    return int(result)
#print(dsl_pipeline_dump_to_dot("pipeline-1", "dot-file-name"))

##
## dsl_pipeline_dump_to_dot_with_ts()
##
_dsl.dsl_pipeline_dump_to_dot_with_ts.argtypes = [ctypes.c_wchar_p, ctypes.c_wchar_p]
_dsl.dsl_pipeline_dump_to_dot_with_ts.restype = ctypes.c_uint
def dsl_pipeline_dump_to_dot_with_ts(pipeline, filename):
    global _dsl
    result =_dsl.dsl_pipeline_dump_to_dot_with_ts(pipeline, filename)
    return int(result)
#print(dsl_pipeline_dump_to_dot_with_ts("pipeline-1", "dot-file-name"))

##
## dsl_main_loop_run()
##
def dsl_main_loop_run():
    global _dsl
    result =_dsl.dsl_main_loop_run()