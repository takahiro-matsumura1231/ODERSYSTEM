from django.test import TestCase
from django.urls import reverse
from ordering.models import Product, Table, OrderProduct, Order
from django.utils import timezone
# Create your tests here.
class OrderingTestCase(TestCase):
    #初期設定
    def setUp(self):
        #商品の登録
        product1 = Product(category_id = 1, tax = True, price = 500, name = "Udon")
        product1.save()
        product2 = Product(category_id = 2, tax = True, price = 500, name = "Cola")
        product2.save() 
        product3 = Product(category_id = 3, tax = True, price = 500, name = "Candy")
        product3.save()
        
        #OrderProductの作成
        orderproduct1 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2 = OrderProduct(product = product3, count = 1)
        orderproduct2.save()
        
        #テーブル番号の登録
        table1 = Table(name = "1", already_ordered = False)
        table1.save()
        table2 = Table(name = "2", already_ordered = False)
        table2.save()
        
        #Orderの作成
        order1 = Order(table = table1, date = timezone.now())
        order1.save()
        order1.order_products.add(orderproduct1)
        order1.order_products.add(orderproduct2)
        
    #商品の作成ができているかどうか
    def test_saved_product(self):
        count = Product.objects.count()
        self.assertEqual(count, 3)
     
    #テーブルの作成ができているかどうか
    def test_saved_Table(self):
        count = Table.objects.count()
        self.assertEqual(count, 2)
           
    #注文確定したときにalready_orderedが変化しているかどうか
    def test_already_ordered_change(self):
        response = self.client.get(reverse('ordering:order_completed', args=[1]))
        table = Table.objects.get(name='1')
        self.assertTrue(table.already_ordered)
     
    #メニュー編集画面で商品が表示されているかどうか   
    def test_change_menu(self):
        response = self.client.get(reverse('ordering:change_menu'))  
        self.assertContains(response, 'Udon')  
        self.assertContains(response, 'Cola')
        self.assertContains(response, 'Candy')
             
    #商品の削除が行われているかどうか    
    def test_delete_menu(self):
        response = self.client.get(reverse('ordering:delete_menu', args=[1]))
        count = Product.objects.count()
        self.assertEqual(count, 2) 
          
    #商品編集画面で商品が表示されているかどうか   
    def test_edit_menu(self):
        response = self.client.get(reverse('ordering:edit_menu', args=[1]))  
        self.assertContains(response, 'Udon')

    #新規注文画面で選択したテーブル番号が表示されているかどうか
    def test_new_order(self):
        response = self.client.get(reverse('ordering:new_order', args=[1]))
        self.assertContains(response, '1')   
        
    #注文画面で選択したテーブル番号が表示されているかどうか、商品が表示されているかどうか
    def test_order_list(self):
        response = self.client.get(reverse('ordering:order_list', args=[1]))
               
         #テーブル番号が表示されているかどうか
        self.assertContains(response, '1')
         #商品が表示されているかどうか
        self.assertContains(response, 'Udon')
        self.assertContains(response, 'Cola')
        self.assertContains(response, 'Candy')
          
         #カテゴリーごとで分かれているかどうか
        count1 = Product.objects.filter(category_id = 1).count()
        self.assertEqual(count1, 1)
        count2 = Product.objects.filter(category_id = 1).count()
        self.assertEqual(count1, 1)
        count3 = Product.objects.filter(category_id = 1).count()
        self.assertEqual(count1, 1)    
     
   
    #注文確認画面が正しく動作しているかどうか   
    def test_check_order(self):
        response = self.client.get(reverse('ordering:check_order', args=[1]))    
        
        #テーブル番号が表示されているかどうか
        self.assertContains(response, '1')
        #入力した注文が表示されているかどうか
        self.assertContains(response, 'Cola')
        self.assertContains(response, 'Candy')
         
    #注文が無い場合の注文確認画面
    def test_check_order_not(self):
        Order.objects.all().delete()
        response = self.client.get(reverse('ordering:check_order', args=[1])) 
        
        #テーブル番号が表示されているかどうか
        self.assertContains(response, '1')
        #注文がありませんが表示されているかどうか
        self.assertContains(response, '注文がありません')
    
    #確認/修正画面が正しく動作しているかどうか
    def test_modification_order(self):
        response = self.client.get(reverse('ordering:modification_order', args=[1]))    
        
        #テーブル番号が表示されているかどうか
        self.assertContains(response, '1')
        #入力した注文が表示されているかどうか
        self.assertContains(response, 'Cola')
        self.assertContains(response, 'Candy')  
        
     #確認/修正画面が正しく動作しているかどうか
    def test_accounting(self):
        response = self.client.get(reverse('ordering:accounting', args=[1]))    
        
        #テーブル番号が表示されているかどうか
        self.assertContains(response, '1')
        #入力した注文が表示されているかどうか
        self.assertContains(response, 'Cola')
        self.assertContains(response, 'Candy')  
        #求める会計の値は表示されているかどうか
        self.assertContains(response, '1000')
           
           
class AccountingTests(TestCase):
    #初期設定
    def setUp(self):
        #商品の登録
        product1 = Product(category_id = 1, tax = True, price = 108, name = "a_8")
        product1.save()
        product2 = Product(category_id = 2, tax = True, price = 216, name = "b_8")
        product2.save() 
        product3 = Product(category_id = 3, tax = True, price = 324, name = "c_8")
        product3.save()
        product4 = Product(category_id = 4, tax = False, price = 110, name = "a_10")
        product4.save()
        product5 = Product(category_id = 5, tax = False, price = 220, name = "b_10")
        product5.save()
        product6 = Product(category_id = 6, tax = False, price = 330, name = "c_10")
        product6.save()
        
        #OrderProductの作成
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct1.save()
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct2.save()
        orderproduct3 = OrderProduct(product = product3, count = 1)
        orderproduct3.save()
        orderproduct4 = OrderProduct(product = product4, count = 1)
        orderproduct4.save()
        orderproduct5 = OrderProduct(product = product5, count = 1)
        orderproduct5.save()
        orderproduct6 = OrderProduct(product = product6, count = 1)
        orderproduct6.save()
        orderproduct7 = OrderProduct(product = product1, count = 2)
        orderproduct7.save()
        
        #テーブル番号の登録
        table1 = Table(name = "1", already_ordered = True)
        table1.save()
        table2 = Table(name = "2", already_ordered = True)
        table2.save()
        table3 = Table(name = "3", already_ordered = True)
        table3.save()
        table4 = Table(name = "4", already_ordered = True)
        table4.save()
        
        #Orderの作成
        #(税率8%商品)
        order1 = Order(table = table1, date = timezone.now())
        order1.save()
        order1.order_products.add(orderproduct1)
        order1.order_products.add(orderproduct2)
        order1.order_products.add(orderproduct3)
        #(税率10%商品)
        order2 = Order(table = table2, date = timezone.now())
        order2.save()
        order2.order_products.add(orderproduct4)
        order2.order_products.add(orderproduct5)
        order2.order_products.add(orderproduct6)
        #(税率8%,10%商品)
        order3 = Order(table = table3, date = timezone.now())
        order3.save()
        order3.order_products.add(orderproduct1)
        order3.order_products.add(orderproduct2)
        order3.order_products.add(orderproduct3)
        order3.order_products.add(orderproduct4)
        order3.order_products.add(orderproduct5)
        order3.order_products.add(orderproduct6)
        #複数個のテスト
        order4 = Order(table = table4, date = timezone.now())
        order4.save()
        order4.order_products.add(orderproduct7)
        
    #商品の作成ができているかどうか
    def test_saved_product(self):
        count = Product.objects.count()
        self.assertEqual(count, 6)
        
    #order_productの作成ができているかどうか
    def test_saved_order_product(self):
        count = OrderProduct.objects.count()
        self.assertEqual(count, 7)
     
    #テーブルの作成ができているかどうか
    def test_saved_Table(self):
        count = Table.objects.count()
        self.assertEqual(count, 4)

    #各テーブルの会計計算ができているか
    def test_accounting_calculation1_1(self):
        table_url = reverse('ordering:accounting', args=[1])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['in'], 648)
    def test_accounting_calculation1_2(self):
        table_url = reverse('ordering:accounting', args=[1])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['out'], 600)
    def test_accounting_calculation1_3(self):
        table_url = reverse('ordering:accounting', args=[1])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['out8'], 600)
    def test_accounting_calculation1_4(self):
        table_url = reverse('ordering:accounting', args=[1])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['out10'], 0)
    def test_accounting_calculation1_5(self):
        table_url = reverse('ordering:accounting', args=[1])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['tax8'], 48)
    def test_accounting_calculation1_6(self):
        table_url = reverse('ordering:accounting', args=[1])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['tax10'], 0)
    def test_accounting_calculation1_7(self):
        table_url = reverse('ordering:accounting', args=[1])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['tax'], 48)
        
    def test_accounting_calculation2_1(self):
        table_url = reverse('ordering:accounting', args=[2])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['in'], 660)
    def test_accounting_calculation2_2(self):
        table_url = reverse('ordering:accounting', args=[2])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['out'], 600)
    def test_accounting_calculation2_3(self):
        table_url = reverse('ordering:accounting', args=[2])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['out8'], 0)
    def test_accounting_calculation2_4(self):
        table_url = reverse('ordering:accounting', args=[2])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['out10'], 600)
    def test_accounting_calculation2_5(self):
        table_url = reverse('ordering:accounting', args=[2])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['tax8'], 0)
    def test_accounting_calculation2_6(self):
        table_url = reverse('ordering:accounting', args=[2])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['tax10'], 60)
    def test_accounting_calculation2_7(self):
        table_url = reverse('ordering:accounting', args=[2])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['tax'], 60)
        
    def test_accounting_calculation3_1(self):
        table_url = reverse('ordering:accounting', args=[3])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['in'], 1308)
    def test_accounting_calculation3_2(self):
        table_url = reverse('ordering:accounting', args=[3])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['out'], 1200)
    def test_accounting_calculation3_3(self):
        table_url = reverse('ordering:accounting', args=[3])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['out8'], 600)
    def test_accounting_calculation3_4(self):
        table_url = reverse('ordering:accounting', args=[3])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['out10'], 600)
    def test_accounting_calculation3_5(self):
        table_url = reverse('ordering:accounting', args=[3])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['tax8'], 48)
    def test_accounting_calculation3_6(self):
        table_url = reverse('ordering:accounting', args=[3])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['tax10'], 60)
    def test_accounting_calculation3_7(self):
        table_url = reverse('ordering:accounting', args=[3])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']   
        self.assertEqual(total['tax'], 108)
        
    def test_accounting_calculation4_1(self):
        table_url = reverse('ordering:accounting', args=[4])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['in'], 216)
    def test_accounting_calculation4_2(self):
        table_url = reverse('ordering:accounting', args=[4])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['out'], 200)
    def test_accounting_calculation4_3(self):
        table_url = reverse('ordering:accounting', args=[4])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['out8'], 200)
    def test_accounting_calculation4_4(self):
        table_url = reverse('ordering:accounting', args=[4])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['out10'], 0)
    def test_accounting_calculation4_5(self):
        table_url = reverse('ordering:accounting', args=[4])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['tax8'], 16)
    def test_accounting_calculation4_6(self):
        table_url = reverse('ordering:accounting', args=[4])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['tax10'], 0)
    def test_accounting_calculation4_7(self):
        table_url = reverse('ordering:accounting', args=[4])
        response = self.client.get(table_url)
        self.assertEqual(response.status_code, 200)
        total = response.context['total']
        self.assertEqual(total['tax'], 16)
        
        #注文確定したときにalready_orderedが変化しているかどうか
    def test_already_ordered_change(self):
        response = self.client.get(reverse('ordering:accounting_completed', args=[1]))
        table = Table.objects.get(name='1')
        self.assertFalse(table.already_ordered)