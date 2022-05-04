from django.shortcuts import render


def product_list(request):

	context = {
		"phone12": {'title': 'Iphone 12', 'desc': 'Super cool phone'},
		'vacuum_cleaner': {'title': 'Vacuum Cleaner', 'desc': 'Make your room clean'},
		'microwave': {'title': 'Microwave', 'desc': 'Best thing to keep your food warm'},
		'drone': {'title': 'DJI Mavic Mini 2', 'desc': 'Wow, that shit can fly'},
		'spinner': {'title': 'Fidget Spinner', 'desc': 'Does anyone still use it?'},
		'phone13': {'title': 'Iphone 13 Pro', 'desc': 'Better one'},
		'samsung1': {'title': 'Samsung', 'desc': 'Yo, this kinda sucks'},
		'iphone11': {'title': 'Iphone 11 Pro', 'desc': "Nice one"},
	}

	return render(request, 'page/product_list.html', context = context)

def product_detail(request):

	context = {
		'phone': {'title': 'Iphone 12', 'desc': 'Super cool phone', 'price': 70000, 'color': 'black', 'screen': '2532x1170'},
	}

	return render(request, 'page/phone.html', context = context)
