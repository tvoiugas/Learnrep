from django.shortcuts import render


def product_list(request):

	context = {
		"phone": {'title': 'Iphone 12', 'desc': 'Super cool phone'},
		'car': 'BMV',
		'microwave': 'Microwave',
	}

	return render(request, 'page/product_list.html', context = context)

def product_detail(request):

	context = {
		'phone': {'price': 70000, 'color': 'черный', 'screen': '2532x1170'},
		'car': {'price': 250000, 'color': 'красный', 'capacity': '5л'},
		'microwave': {'price': 40000, 'color': 'белый', 'model': 'Toshiba EM131A5C'},
	}

	return render(request, 'page/phone.html', context = context)
