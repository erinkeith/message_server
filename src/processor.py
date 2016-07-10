def process_event(event, current_sites, messages):
    if event.msg_id not in messages:
        messages.append(event.msg_id)

        current_sites.add_site(event.msg_site_id)
        site = current_sites.get_site(event.msg_site_id)

        if event.msg_type == 'message':
            process_message(event, site)
        elif event.msg_type == 'status':
            process_status(event, site)

        save_stats(current_sites)


def process_message(event, site):
    if site.online:
        send_message(event.data_message, site)
    elif not site.online:
        send_email(event.data_message, site)

    site.add_visitor(event.msg_from)


def process_status(event, site):
    if event.data_status == 'online':
        site.online = True
        site.add_operator(event.msg_from)
    # ASSUME operators send correct statuses
    elif event.data_status == 'offline':
        site.remove_operator(event.msg_from)
        if site.num_online_operators() < 1:
         site.online = False


def send_message(data, site):
    site.messages += 1


def send_email(data, site):
    site.emails += 1


def save_stats(current_sites):
    json_string = build_json_string(current_sites)
    write_json_file(json_string)


def build_json_string(current_sites):
    json_string = '['
    for site_id in current_sites.list_sorted_site_ids():
        site = current_sites.get_site(site_id)
        json_string += '{' + '"site_id": {}, "messages": {}, "emails": {}, "operators": {}, "visitors": {}'.format(
            site_id, site.messages, site.emails, site.num_operators(), site.num_visitors()) + '},'
    json_string = json_string[:-1] + ']'
    return json_string


def write_json_file(json_string):
    with open('stats.json', 'w+') as json_file:
        json_file.write(json_string)
