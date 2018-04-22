# _*_ coding: utf-8 _*_

from django.shortcuts import render
from django.views.decorators import csrf
import pdb

# 接收POST请求数据
def search_post(request):
	ctx = {}
	if request.POST:
		ctx['rlt'] = request.POST['q']
	# pdb.set_trace()
	print(ctx)
	return render(request, "post.html", ctx)