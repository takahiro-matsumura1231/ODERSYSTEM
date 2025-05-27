from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Product, Order, Table, OrderProduct
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import MenuForm
from django.http import JsonResponse
from django.views import View
from django.utils import timezone


# カテゴリー番号とカテゴリー名の対応を保持したリスト
category_list = {1:'食べもの', 2:'飲みもの', 3:'お持ち帰り'}


class HomeView(TemplateView):
    template_name = 'ordering/home.html'
    
class InputNumView(TemplateView):
    template_name = 'ordering/input_table_number.html'
    max_table_number = 20; # 最大テーブル数
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table_list = {}
        # テーブル番号と注文の有無を保持したリストを作成
        for num in range(1, self.max_table_number+1):
            table = get_object_or_404(Table, name=num)
            table_list[num] = table.already_ordered
        context['table_list'] = table_list
        return context
   
class CheckAlreadyOrdered(TemplateView):
    template_name = 'ordering/input_table_number.html'
    
    def get(self, request, *args, **kwargs):
        table_number = self.kwargs.get('table_number')
        table = get_object_or_404(Table, name=table_number)

        if table.already_ordered: # 既に注文があった場合
            return redirect('ordering:manage_order', table_number=table_number)
        else:                     # 新規で注文する場合
            return redirect('ordering:new_order', table_number=table_number)

class NewOrderView(TemplateView):
    template_name = 'ordering/new_order.html'  

class ManageOrderView(TemplateView):
    template_name = 'ordering/manage_order.html'
    
class OrderView(TemplateView):
    template_name = 'ordering/order_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table_number = context['table_number']
        table = Table.objects.get(name=table_number)
     
        if table.already_ordered: # 既に注文がある場合
            order = table.order_set.last()
        else:                     # 新規注文の場合
            order = Order.objects.create(table=table, date=timezone.now())
            
        product_list = []
        for product in Product.objects.all(): # 商品リストを作成
            pro = {'id':product.id, 'name':product.name, 'price':product.price, 'category_id':product.category_id, 'count':0}
            order_product = order.order_products.filter(product=product)
            if order_product :
                pro['count'] = order_product[0].count
            product_list.append(pro)
        
        context['order'] = order                 # 注文データ
        context['product_list'] = product_list   # 全商品リスト
        context['category_list'] = category_list # カテゴリーリスト
        return context
    
class AddOrderView(TemplateView):
    template_name = 'ordering/add_order_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table_number = context['table_number']
        table = Table.objects.get(name=table_number)
     
        if table.already_ordered: # 既に注文がある場合
            order = table.order_set.last()
        else:                     # 新規注文の場合
            order = Order.objects.create(table=table, date=timezone.now())
            
        product_list = []
        for product in Product.objects.all(): # 商品リストを作成
            pro = {'id':product.id, 'name':product.name, 'price':product.price, 'category_id':product.category_id, 'count':0}
            order_product = order.order_products.filter(product=product)
            if order_product :
                pro['count'] = order_product[0].count
            product_list.append(pro)
        
        context['order'] = order                 # 注文データ
        context['product_list'] = product_list   # 全商品リスト
        context['category_list'] = category_list # カテゴリーリスト
        return context
     
class CheckOrderView(TemplateView):
    template_name = 'ordering/check_order.html'
    
    def get(self, request, *args, **kwargs):
        table_number = self.kwargs.get('table_number')
        table = get_object_or_404(Table, name=table_number)
        
        if table.already_ordered != True:
            table.already_ordered = False
            table.save()
        
        latest_order = table.order_set.last()
        if latest_order:
            order_products = latest_order.order_products.all()
        else:
            order_products = None
            
        order_product_id = self.kwargs.get('order_product_id')
        if order_product_id : # order_product_idが送信された場合削除
            order_product = get_object_or_404(OrderProduct, id=order_product_id)
            order_product.delete()
            
        context = {'table_number': table_number, 'order':latest_order, 'order_products': order_products}
        return render(request, 'ordering/check_order.html', context)
 
class CheckAddedOrderView(TemplateView):
    template_name = 'ordering/check_added_order.html'
    
    def get(self, request, *args, **kwargs):
        table_number = self.kwargs.get('table_number')
        table = get_object_or_404(Table, name=table_number)
        
        if table.already_ordered != True:
            table.already_ordered = False
            table.save()
        
        latest_order = table.order_set.last()
        if latest_order:
            order_products = latest_order.order_products.all()
        else:
            order_products = None
            
        order_product_id = self.kwargs.get('order_product_id')
        if order_product_id : # order_product_idが送信された場合削除
            order_product = get_object_or_404(OrderProduct, id=order_product_id)
            order_product.delete()
            
        context = {'table_number': table_number, 'order':latest_order, 'order_products': order_products}
        return render(request, 'ordering/check_added_order.html', context)
 
 
class OrderConfirmedView(TemplateView):
    template_name = 'ordering/order_confirmed.html'
    
class OrderCompletedView(TemplateView):
    template_name = 'ordering/home.html'
    
    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        table_number = context['table_number']
        table = get_object_or_404(Table, name=table_number)
        latest_order = table.order_set.last()
        
        if latest_order:
            # オーダーが存在する場合、関連する製品を取得
            order_products = latest_order.order_products.all()
        else:
            order_products = None
            
        for order_product in order_products:
            if order_product.count == 0: # 0個だった場合削除
                order_product.delete()
                latest_order.save()
                continue

        table.already_ordered = True
        table.save()
        
        context = {'table_number' : table_number}
        
        return render(request, 'ordering/home.html', context) 
        
class ModificationOrderView(TemplateView):
    template_name = 'ordering/modification_order.html'
    
    def get(self, request, *args, **kwargs):
        table_number = self.kwargs.get('table_number')
        table = get_object_or_404(Table, name=table_number)
        latest_order = table.order_set.last()
        
        if latest_order:
            order_products = latest_order.order_products.all()
        else:
            order_products = None
            
        order_product_id = self.kwargs.get('order_product_id')
        if order_product_id :
            order_product = get_object_or_404(OrderProduct, id=order_product_id)
            order_product.delete()
            
        context = {'table_number': table_number, 'order':latest_order, 'order_products': order_products}
        return render(request, 'ordering/modification_order.html', context)
    
class UpdateOrderProductView(View):

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        order_id = request.POST.get('order_id')
        action = request.POST.get('action')

        product = get_object_or_404(Product, id=product_id)
        order = get_object_or_404(Order, pk=order_id)
        order_product = order.order_products.filter(product=product)

        if order_product :
            order_product = order_product[0]
            if action == 'add':   # 数量を増やす
                order_product.count += 1
            elif action == 'sub': # 数量を減らす
                if order_product.count > 0:
                    order_product.count -= 1
        else :
            if action == 'add':
                # 新しいOrderProductを作成
                order_product = OrderProduct.objects.create(product=product, count=1)
                order.order_products.add(order_product)
        order_product.save()

        return JsonResponse({'count': order_product.count})

class AccountingView(TemplateView):
    template_name = 'ordering/accounting.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table_number = context['table_number']
        table = get_object_or_404(Table, name=table_number)
        latest_order = table.order_set.last()
        
        if latest_order:
            # オーダーが存在する場合、関連する製品を取得
            order_products = latest_order.order_products.all()
        else:
            order_products = None
        
        total = {}
        total_in8 = 0  # 8%税込み合計
        total_in10 = 0 # 10%税込み合計    
        order_list = []
        for order_product in order_products:
            if order_product.count == 0: # 0個だった場合削除
                order_product.delete()
                latest_order.save()
                continue
            product = order_product.product
            pro = {'name': product.name, 'tax': product.tax, 'count': order_product.count}
            if product.tax: # 税率8%
                pro['price'] = round(product.price / (1 + 0.08))
                total_in8 += product.price * order_product.count
            else:           # 税率10%
                pro['price'] = round(product.price / (1 + 0.1))
                total_in10 += product.price * order_product.count
            pro['sum'] = pro['price'] * pro['count']
            order_list.append(pro);
                
        total['in'] = total_in8 + total_in10          # 税込み合計
        total['out8'] = round(total_in8 / (1 + 0.08)) # 8%税抜き合計
        total['tax8'] = total_in8 - total['out8']     # 8%消費税合計
        total['out10'] = round(total_in10 / (1+ 0.1)) # 10%税抜き合計
        total['tax10'] = total_in10 - total['out10']  # 10%消費税合計
        total['out'] = total['out8'] + total['out10'] # 税抜き合計
        total['tax'] = total['tax8'] + total['tax10'] # 消費税合計
        
        context['table_number'] = table_number
        context['order_list'] = order_list
        context['total'] = total
        return context
    
class AccountingConfirmedView(TemplateView):
    template_name = 'ordering/accounting_confirmed.html'
    
class AccountingCompletedView(TemplateView):
    template_name = 'ordering/accounting_completed.html'
    
    def get(self, request, *args, **kwargs):
        table_number = self.kwargs.get('table_number')
        table = get_object_or_404(Table, name=table_number)
        table.already_ordered = False
        table.save()
        
        context = {'table_number' : table_number}
        
        return render(request, 'ordering/accounting_completed.html', context)
    
class ChangeMenuView(ListView):
    model = Product
    template_name = 'ordering/change_menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = category_list
        context['object_list'] = Product.objects.all()
        context['tax'] = ['8%', '10%']
        return context
    
def delete_menu(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('ordering:change_menu'))

class EditMenuView(TemplateView):
    model = Product
    template_name = 'ordering/edit_menu.html'
    success_url = 'change_menu'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = context['product_id']
        category_id = self.request.POST.get('category_id')
        name = self.request.POST.get('name')
        price = self.request.POST.get('price')
        tax = self.request.POST.get('tax')

        product = get_object_or_404(Product, pk=product_id)
        product.name = name
        product.price = price
        product.tax = tax
        product.category_id = category_id
        product.save()
        return HttpResponseRedirect(reverse('ordering:change_menu'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = context['product_id']
        product = get_object_or_404(Product, pk=product_id)
        data = {
            'name': product.name,
            'price': product.price,
            'tax': product.tax,
            'category_id': product.category_id
        }
        context['form'] = MenuForm(initial=data)
        return context

class AddMenuView(CreateView):
    model = Product
    form_class = MenuForm
    template_name = 'ordering/add_menu.html'
    success_url = 'change_menu'
    
class CheckOrderProductCount(TemplateView):
    template_name = 'ordering/home.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        table_number = context['table_number']
        table = get_object_or_404(Table, name=table_number)
        latest_order = table.order_set.last()
        
        if latest_order:
            # オーダーが存在する場合、関連する製品を取得
            order_products = latest_order.order_products.all()
        else:
            order_products = None
            
        for order_product in order_products:
            if order_product.count == 0: # 0個だった場合削除
                order_product.delete()
                latest_order.save()
                continue
        return HttpResponseRedirect(reverse('ordering:home'))
