import sys
sys.path.insert(0, "../../")
import time

from dsl import *

DSL_RETURN_SUCCESS = 0

# Filespecs for the Primary GIE
inferConfigFile = '../../test/configs/config_infer_primary_nano.txt'
modelEngineFile = '../../test/models/Primary_Detector_Nano/resnet10.caffemodel'

while True:

    # First new URI File Source
    retval = dsl_source_uri_new('uri-source-1', "../../test/streams/sample_1080p_h264.mp4", 0, 0, 2)

    if retval != DSL_RETURN_SUCCESS:
        print(retval)
        break

    # New Primary GIE using the filespecs above, with interval and Id
    retval = dsl_gie_primary_new('primary-gie', inferConfigFile, modelEngineFile, 4, 1)

    if retval != DSL_RETURN_SUCCESS:
        print(retval)
        break

    # New Tiled Display, setting width and height, use default cols/rows set by source count
    retval = dsl_display_new('tiled-display', 1280, 720)

    if retval != DSL_RETURN_SUCCESS:
        print(retval)
        break

    # New Overlay Sink, 0 x/y offsets and same dimensions as Tiled Display
    retval = dsl_sink_overlay_new('overlay-sink', 0, 0, 1280, 720)

    if retval != DSL_RETURN_SUCCESS:
        print(retval)
        break

    # New Pipeline to use with the above components
    retval = dsl_pipeline_new('simple-pipeline')

    if retval != DSL_RETURN_SUCCESS:
        print(retval)
        break

    # Add all the components to our pipeline
#    retval = dsl_pipeline_component_add_many('simple-pipeline', ['uri-source', 'primary-gie', 'tiled-display', 'overlay-sink', None])
    retval = dsl_pipeline_component_add_many('simple-pipeline', ['uri-source-1' , 'tiled-display', 'overlay-sink', None])

    if retval != DSL_RETURN_SUCCESS:
        print(retval)
        break

    # Play the pipeline
    retval = dsl_pipeline_play('simple-pipeline')

    if retval != DSL_RETURN_SUCCESS:
        print(retval)
        break

    # Pause to allow the first source to get ahead
    time.sleep(2)
    
    # Play the pipeline
    retval = dsl_pipeline_pause('simple-pipeline')

    if retval != DSL_RETURN_SUCCESS:
        print(retval)
        break

    # create a second uri file source using the same file
    # Note: often called from a seperate thread or callback
    retval = dsl_source_uri_new('uri-source-2', "../../test/streams/sample_1080p_h264_dup.mp4", 0, 0, 2)

    if retval != DSL_RETURN_SUCCESS:
        print(retval)
        break
    
    # Add the second source while the Pipeline is currently playing
    retval = dsl_pipeline_component_add('simple-pipeline', 'uri-source-2')

    # Play the pipeline
    retval = dsl_pipeline_play('simple-pipeline')

    if retval != DSL_RETURN_SUCCESS:
        print(retval)
        break

    dsl_main_loop_run()
    break

dsl_pipeline_delete_all()
dsl_component_delete_all()