from django.shortcuts import render, get_object_or_404, redirect
import datetime
from django.http import HttpResponse
from django.views.decorators.http import (
    require_http_methods, require_GET
)
from django.views.decorators.cache import cache_control, never_cache
from asgiref.sync import sync_to_async
import asyncio
from .models import Section, Story, MyModel

# View hiển thị danh sách câu chuyện
def story_list_view(request):
    section = Section.objects.first()  # Lấy phần đầu tiên
    story_list = Story.objects.all()  # Lấy tất cả câu chuyện
    return render(request, 'story_list.html', {'section': section, 'story_list': story_list})

# View trang index
def index(request):
    return render(request, 'index.html')

# View hiển thị thời gian hiện tại
def current_datetime(request):
    now = datetime.datetime.now()
    html = f"<html><body>It is now {now}.</body></html>"
    return HttpResponse(html)

# View trả về phản hồi với mã trạng thái 201
def my_view(request):
    return HttpResponse(status=201)

# View hiển thị chi tiết câu chuyện
def story_detail_view(request, story_id):
    obj = get_object_or_404(MyModel, pk=story_id)
    return render(request, "myapp/story_detail.html", {"story": obj})

# View chuyển hướng
def redirect_view(request):
    return redirect('current_datetime')

# View xử lý lỗi 404
def my_custom_page_not_found_view(request, exception):
    return HttpResponse("Page not found", status=404)

# View xử lý lỗi 500
def my_custom_error_view(request):
    return HttpResponse("Server error", status=500)

# View xử lý yêu cầu GET hoặc POST, không đồng bộ
@require_http_methods(["GET", "POST"])
@cache_control(no_cache=True)
async def my_async_view(request):
    await asyncio.sleep(1)  # Giả lập tác vụ mất thời gian
    return HttpResponse("Hello from async view!")

# View chỉ xử lý yêu cầu GET, không đồng bộ
@require_GET
async def safe_view(request):
    return HttpResponse("This is a safe async view.")

# View không được cache, không đồng bộ
@never_cache
async def non_cache_view(request):
    return HttpResponse("This page is never cached.")

# Hàm đồng bộ sử dụng sync_to_async
def sync_function():
    return "This is a sync function."

# View không đồng bộ sử dụng hàm đồng bộ
async def async_view_using_sync_function(request):
    result = await sync_to_async(sync_function)()
    return HttpResponse(result)
