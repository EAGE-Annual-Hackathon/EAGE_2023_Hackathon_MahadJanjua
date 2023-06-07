import pandas as pd

# -------------------------------------------------
# Separate module for state resets
# -------------------------------------------------

def set_all_states(state):
    
    if "process_select" not in state:
        state.process_select = None

    if "process_select_confirmed" not in state:
        state.process_select_confirmed = False

    if "begin_process" not in state:
        state.begin_process = False

    if "file" not in state:
        state.file = None

    if "method_one_df" not in state:
        state.method_one_df = None

    if "query_method_one" not in state:
        state.query_method_one = None

    if "prompt_method_one" not in state:
        state.prompt_method_one = None
    
    if "get_response_method_one" not in state:
        state.get_response_method_one = None

    if "response_method_one" not in state:
        state.response_method_one = None

    if "save_prompt" not in state:
        state.save_query = False

    if "que_response_gen" not in state:
        state.que_response_gen = False

    if "root_dir" not in state:
        state.root_dir = None

    if "file_types_options" not in state:
        state.file_types_options = None

    if "begin_file_data_collation" not in state:
        state.begin_file_data_collation = False

    if "method_two_df" not in state:
        state.method_two_df = None

    if "query_method_two" not in state:
        state.query_method_two = None

    if "save_query_two" not in state:
        state.save_query_two = False

    if "prompt_method_two" not in state:
        state.prompt_method_two = None

    if "get_response_method_two" not in state:
        state.get_response_method_two = None

    if "response_method_two" not in state:
        state.response_method_two = None

    if "que_response_gen_two" not in state:
        state.que_response_gen_two = False

    if "output_two" not in state:
        state.output_two = None

    if "file_3" not in state:
        state.file_3 = None

    if "file_path_3" not in state:
        state.file_path_3 = None

    if "query_method_three" not in state:
        state.query_method_three = None

    if "save_query_three" not in state:
        state.save_query_three = False
    
    if "prompt_method_three" not in state:
        state.prompt_method_three = None

    if "que_response_gen_three" not in state:
        state.que_response_gen_three = False

    if "response_method_three" not in state:
        state.response_method_three = None
    return state


def state_upload_file_none(state):

    state.process_select = None
    state.process_select_confirmed = False
    state.method_one_df = None
    state.query_method_one = None
    state.prompt_method_one = None
    state.get_response_method_one = None
    state.response_method_one = None
    state.save_query = False
    state.que_response_gen = False

    return state


def state_upload_file_3_none(state):
    
    state.file_3 = None
    state.file_path_3 = None
    state.query_method_three = None
    state.save_query_three = False
    state.prompt_method_three = None
    state.que_response_gen_three = False
    state.response_method_three = None

    return state
