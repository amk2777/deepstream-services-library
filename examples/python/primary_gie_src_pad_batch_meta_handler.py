import sys
sys.path.insert(0, "../../")
import time
import math
import pyds
from dsl import *

DSL_RETURN_SUCCESS = 0

# Filespecs for the Primary GIE
primary_infer_config_file = '../../test/configs/config_infer_primary_nano.txt'
primary_model_engine_file = '../../test/models/Primary_Detector_Nano/resnet10.caffemodel_b1_fp16.engine'

def primary_gie_batch_meta_handler_cb(buffer, user_data):

    batch_meta = pyds.gst_buffer_get_nvds_batch_meta(buffer)
    l_frame = batch_meta.frame_meta_list
    while l_frame is not None:
        try:
            frame_meta = pyds.glist_get_nvds_frame_meta(l_frame.data)
        except StopIteration:
            break    

#        '''
        print("Frame Number is ", frame_meta.frame_num)
        print("Source id is ", frame_meta.source_id)
        print("Batch id is ", frame_meta.batch_id)
        print("Source Frame Width ", frame_meta.source_frame_width)
        print("Source Frame Height ", frame_meta.source_frame_height)
        print("Num object meta ", frame_meta.num_obj_meta)
 #       '''

        try:
            l_frame=l_frame.next
        except StopIteration:
            break
    return True

## 
# Function to be called on XWindow KeyRelease event
## 
def xwindow_key_event_handler(key_string, client_data):
    print('key released = ', key_string)
    if key_string.upper() == 'P':
        dsl_pipeline_pause('pipeline')
    elif key_string.upper() == 'R':
        dsl_pipeline_play('pipeline')
    elif key_string.upper() == 'Q' or key_string == '':
        dsl_main_loop_quit()

## 
# Function to be called on XWindow Delete event
## 
def xwindow_delete_event_handler(client_data):
    print('delete window event')
    dsl_main_loop_quit()

## 
# Function to be called on every change of Pipeline state
## 
def state_change_listener(old_state, new_state, client_data):
    print('previous state = ', old_state, ', new state = ', new_state)

def main(args):
    
    ##
    # Since we're not using args, we can Let DSL initialize GST on first call
    ##
    while True:

        ## 
        # New URI File Source
        ## 
        retval = dsl_source_uri_new('uri-source', "../../test/streams/sample_1080p_h264.mp4", False, 0, 0, 0)
        if retval != DSL_RETURN_SUCCESS:
            break

        ## 
        # New Primary GIE using the filespecs above with interval = 0
        ## 
        retval = dsl_gie_primary_new('primary-gie', primary_infer_config_file, primary_model_engine_file, 0)
        if retval != DSL_RETURN_SUCCESS:
            break

        ## 
        # Add the above defined batch meta handler to the Source Pad of the primary-gie
        ## 
        retval = dsl_gie_primary_batch_meta_handler_add('primary-gie', DSL_PAD_SRC, primary_gie_batch_meta_handler_cb, None)
        if retval != DSL_RETURN_SUCCESS:
            break
        
        ## 
        # New KTL Tracker, setting max width and height of input frame
        ## 
        retval = dsl_tracker_ktl_new('ktl-tracker', 480, 272)
        if retval != DSL_RETURN_SUCCESS:
            break

        ## 
        # New Tiled Display, setting width and height, use default cols/rows set by source count
        ## 
        retval = dsl_tiler_new('tiler', 1280, 720)
        if retval != DSL_RETURN_SUCCESS:
            break

        ## 
        # New OSD with clock disabled... using default values.
        ## 
        retval = dsl_osd_new('on-screen-display', False)
        if retval != DSL_RETURN_SUCCESS:
            break

        ## 
        ## New Window Sink, 0 x/y offsets and same dimensions as Tiled Display
        ## 
        retval = dsl_sink_window_new('window-sink', 0, 0, 1280, 720)
        if retval != DSL_RETURN_SUCCESS:
            break

        # New Pipeline to use with the above components
        retval = dsl_pipeline_new('pipeline')
        if retval != DSL_RETURN_SUCCESS:
            break

        # Add all the components to our pipeline
        retval = dsl_pipeline_component_add_many('pipeline', 
            ['uri-source', 'primary-gie', 'ktl-tracker', 'tiler', 'on-screen-display', 'window-sink', None])    
        if retval != DSL_RETURN_SUCCESS:
            break

        ## 
        ## Add the XWindow event handler functions defined above
        ##
        retval = dsl_pipeline_xwindow_key_event_handler_add("pipeline", xwindow_key_event_handler, None)
        if retval != DSL_RETURN_SUCCESS:
            break

        retval = dsl_pipeline_xwindow_delete_event_handler_add("pipeline", xwindow_delete_event_handler, None)
        if retval != DSL_RETURN_SUCCESS:
            break

        ## 
        ## Add the listener callback function defined above
        ## 
        retval = dsl_pipeline_state_change_listener_add('pipeline', state_change_listener, None)


        # Play the pipeline
        retval = dsl_pipeline_play('pipeline')
        if retval != DSL_RETURN_SUCCESS:
            break

        dsl_main_loop_run()
        retval = DSL_RETURN_SUCCESS
        break

    # Print out the final result
    print(dsl_return_value_to_string(retval))

    # Need to delete the Pipeline first, returning all component to a state of not-in-use,
    # then all components can be deleted freeing up resoureces.
    dsl_pipeline_delete_all()
    dsl_component_delete_all()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
