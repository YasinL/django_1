import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt
from .models import Choice, Question, UserProfile, Menu
from django.core.urlresolvers import reverse
from django.http import Http404

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'django_app/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'django_app/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'django_app/results.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'django_app/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('django_app:results', args=(p.id,)))


# ==================== 用户管理视图 ====================

def user_list(request):
    """用户列表页面"""
    users = UserProfile.objects.all()
    return render(request, 'django_app/user_list.html', {'users': users})


@csrf_exempt
def user_create(request):
    """创建用户"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8')) if request.body else request.POST
            username = data.get('username', '')
            email = data.get('email', '')
            phone = data.get('phone', '')
            real_name = data.get('real_name', '')
            status = int(data.get('status', 1))
            
            if not username:
                return JsonResponse({'success': False, 'message': '用户名不能为空'})
            
            if UserProfile.objects.filter(username=username).exists():
                return JsonResponse({'success': False, 'message': '用户名已存在'})
            
            user = UserProfile.objects.create(
                username=username,
                email=email,
                phone=phone,
                real_name=real_name,
                status=status
            )
            return JsonResponse({'success': True, 'message': '创建成功', 'id': user.id})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return render(request, 'django_app/user_form.html', {'action': 'create'})


@csrf_exempt
def user_update(request, user_id):
    """更新用户"""
    user = get_object_or_404(UserProfile, pk=user_id)
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8')) if request.body else request.POST
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            user.phone = data.get('phone', user.phone)
            user.real_name = data.get('real_name', user.real_name)
            user.status = int(data.get('status', user.status))
            user.save()
            return JsonResponse({'success': True, 'message': '更新成功'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return render(request, 'django_app/user_form.html', {'action': 'update', 'user': user})


@csrf_exempt
def user_delete(request, user_id):
    """删除用户"""
    if request.method == 'POST':
        try:
            user = get_object_or_404(UserProfile, pk=user_id)
            user.delete()
            return JsonResponse({'success': True, 'message': '删除成功'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': '请求方法不正确'})


def user_detail(request, user_id):
    """用户详情"""
    user = get_object_or_404(UserProfile, pk=user_id)
    return render(request, 'django_app/user_detail.html', {'user': user})


# ==================== 菜单管理视图 ====================

def menu_list(request):
    """菜单列表页面"""
    menus = Menu.objects.filter(parent__isnull=True)
    return render(request, 'django_app/menu_list.html', {'menus': menus})


@csrf_exempt
def menu_create(request):
    """创建菜单"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8')) if request.body else request.POST
            name = data.get('name', '')
            url = data.get('url', '')
            icon = data.get('icon', '')
            parent_id = data.get('parent_id')
            order = int(data.get('order', 0))
            status = int(data.get('status', 1))
            
            if not name:
                return JsonResponse({'success': False, 'message': '菜单名称不能为空'})
            
            parent = None
            if parent_id:
                parent = get_object_or_404(Menu, pk=parent_id)
            
            menu = Menu.objects.create(
                name=name,
                url=url,
                icon=icon,
                parent=parent,
                order=order,
                status=status
            )
            return JsonResponse({'success': True, 'message': '创建成功', 'id': menu.id})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    parent_menus = Menu.objects.filter(parent__isnull=True)
    return render(request, 'django_app/menu_form.html', {'action': 'create', 'parent_menus': parent_menus})


@csrf_exempt
def menu_update(request, menu_id):
    """更新菜单"""
    menu = get_object_or_404(Menu, pk=menu_id)
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8')) if request.body else request.POST
            menu.name = data.get('name', menu.name)
            menu.url = data.get('url', menu.url)
            menu.icon = data.get('icon', menu.icon)
            menu.order = int(data.get('order', menu.order))
            menu.status = int(data.get('status', menu.status))
            
            parent_id = data.get('parent_id')
            if parent_id:
                menu.parent = get_object_or_404(Menu, pk=parent_id)
            else:
                menu.parent = None
            
            menu.save()
            return JsonResponse({'success': True, 'message': '更新成功'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    parent_menus = Menu.objects.filter(parent__isnull=True).exclude(pk=menu_id)
    return render(request, 'django_app/menu_form.html', {'action': 'update', 'menu': menu, 'parent_menus': parent_menus})


@csrf_exempt
def menu_delete(request, menu_id):
    """删除菜单"""
    if request.method == 'POST':
        try:
            menu = get_object_or_404(Menu, pk=menu_id)
            menu.delete()
            return JsonResponse({'success': True, 'message': '删除成功'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': '请求方法不正确'})


def menu_detail(request, menu_id):
    """菜单详情"""
    menu = get_object_or_404(Menu, pk=menu_id)
    return render(request, 'django_app/menu_detail.html', {'menu': menu})













