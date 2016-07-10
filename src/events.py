class PostEvent(object):
    def __init__(self, post_form):
        self.msg_id = post_form['id'].value
        self.msg_from = post_form['from'].value
        self.msg_type = post_form['type'].value
        self.msg_site_id = post_form['site_id'].value
        self.msg_timestamp = post_form['timestamp'].value

        if self.msg_type == 'message':
            self.data_message = post_form['data_message'].value
        elif self.msg_type == 'status':
            self.data_status = post_form['data_status'].value
