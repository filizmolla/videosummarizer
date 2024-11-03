from django.urls import resolve

def mark_active_link(menu, current_path_name):
    for item in menu:
        item['is_active'] = item.get('name', '') == current_path_name

        if 'children' in item:
            item['children'] = mark_active_link(item['children'], current_path_name)

            if any(child.get('is_active', False) for child in item['children']):
                item['is_active'] = True

    return menu

def sidebar_menu(request):
	sidebar_menu = [{
		'text': 'Navigation',
		'is_header': 'true'
	},
    { 
		'url': '/', 'icon': 'fa fa-home', 'title': 'Home'
	}, 
	{ 
		'url': '/videolar', 'icon': 'fa fa-list', 'title': 'Videolar'
	}, 
    { 
		'url': '/add_video', 'icon': 'fa fa-plus', 'title': 'Add Video'
	} 
   
     

     ]
	
	resolved_path = resolve(request.path_info)

	current_path_name = resolved_path.url_name
	
	sidebar_menu = mark_active_link(sidebar_menu, current_path_name)

	return {'sidebar_menu': sidebar_menu}