from termcolor import colored

# List of messages returned in terminal. Used in console_message fun
messages = {
    'check_message': 'Checking links in file:',
    'check_link_message': 'Link checked:',
    'all_good_message': 'No broken links found in ditamap:',
    'no_links_warn': 'Links ditamap not well-formed or no external links to check in file:',
    'no_ditamap_warn': 'Based on filename, file is not a ditamap:',
    'not_xml_error': 'File is not a well-formed xml file: ',
    'status_code_error': 'Browser sent back error status code. Check link:',
    'invalid_url_error': 'Link is not well-formed. Check link in your browser:',
    'connection_error': 'Failed to connect to link:',
    'no_such_file_error': 'Could not find file:',
    'error_count_message': 'Links to be checked:',
    'file_not_spec_error': 'Specify a ditamap file for the command. For example: python links_map_checker.py foo.ditamap'
}

# List of message tags and colors used in console_message fun. Tags and
# colors are all optional
message_types = {
    'ok': {
        'color': 'green',
        'tag': 'SUCCESS!!!!!'
    },
    'error': {
        'color': 'red',
        'tag': 'ERROR!!!!!'
    },
    'warning': {
        'color': 'yellow',
        'tag': 'WARNING!!!!!'
    },
    'info': {
        'color': 'blue',
        'tag': 'INFO:'
    }
}


def console_message(type, key, arg, with_color=True, with_tag=True):
    """
    Constructs message based on:
      * type (i.e. 'info' or 'error')
      * message key (i.e. 'check_message' or 'invalid_url_error')
      * arg (a variable, such as a link or file name)
    """
    message = ' '.join((messages[key], arg))

    # If with_tag is set to true (default), tag corresponding to type is used
    # as prefix to the message
    if with_tag:
        tag = message_types[type]['tag']
        message = ' '.join((tag, message))

    # If with_color is set to true (default), color corresponding to type is
    # used to format the message
    if with_color:
        color = message_types[type]['color']
        return colored(message, color)

    return message
