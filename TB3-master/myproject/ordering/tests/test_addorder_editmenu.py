from django.test import TestCase
from django.urls import reverse
from ordering.models import Product, Table, OrderProduct, Order
from django.utils import timezone
# Create your tests here.
class OrderingTestCase(TestCase):
    #初期設定
    def setUp(self):
        #商品の登録
        product1 = Product(category_id = 1, tax = False, price = 1, name = "A_8")
        product2 = Product(category_id = 1, tax = True, price = 1, name = "A_10")
        product3 = Product(category_id = 2, tax = False, price = 1, name = "B_8")
        product4 = Product(category_id = 2, tax = True, price = 1, name = "B_10")
        product5 = Product(category_id = 3, tax = False, price = 1, name = "C_8")
        product6 = Product(category_id = 3, tax = True, price = 1, name = "C_10")
        product1.save()
        product2.save()
        product3.save()
        product4.save()
        product5.save()
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
        
        #テーブル番号の登録
        table1 = Table(name = "1", already_ordered = True)
        table1.save()
        table2 = Table(name = "2", already_ordered = True)
        table2.save()
        
        #Orderの作成
        order1 = Order(table = table1, date = timezone.now())
        order1.save()
        
        #追加注文のテスト
    def test_add_order_1(self):   
        product = Product.objects.get(name="A_8")
        orderproduct = OrderProduct(product = product, count = 1)
        orderproduct.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')

    def test_add_order_2(self):   
        product = Product.objects.get(name="A_10")
        orderproduct = OrderProduct(product = product, count = 1)
        orderproduct.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        
    def test_add_order_3(self):   
        product = Product.objects.get(name="B_8")
        orderproduct = OrderProduct(product = product, count = 1)
        orderproduct.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_8')
    
    def test_add_order_4(self):   
        product = Product.objects.get(name="B_10")
        orderproduct = OrderProduct(product = product, count = 1)
        orderproduct.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_10')
        
    def test_add_order_5(self):   
        product = Product.objects.get(name="C_8")
        orderproduct = OrderProduct(product = product, count = 1)
        orderproduct.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'C_8')
        
    def test_add_order_6(self):   
        product = Product.objects.get(name="C_10")
        orderproduct = OrderProduct(product = product, count = 1)
        orderproduct.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'C_10')
        
    def test_add_order_1_double(self):   
        product1 = Product.objects.get(name="A_8")
        product2 = Product.objects.get(name="A_10")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        
    def test_add_order_2_double(self):   
        product1 = Product.objects.get(name="A_8")
        product2 = Product.objects.get(name="B_8")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_8')
        
    def test_add_order_3_double(self):   
        product1 = Product.objects.get(name="A_8")
        product2 = Product.objects.get(name="B_10")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_10')
        
    def test_add_order_4_double(self):   
        product1 = Product.objects.get(name="A_8")
        product2 = Product.objects.get(name="C_8")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'C_8')
         
    def test_add_order_5_double(self):   
        product1 = Product.objects.get(name="A_8")
        product2 = Product.objects.get(name="C_10")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_6_double(self):   
        product1 = Product.objects.get(name="A_10")
        product2 = Product.objects.get(name="B_8")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')  
        
    def test_add_order_7_double(self):   
        product1 = Product.objects.get(name="A_10")
        product2 = Product.objects.get(name="B_10")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_10')
        
    def test_add_order_8_double(self):   
        product1 = Product.objects.get(name="A_10")
        product2 = Product.objects.get(name="C_8")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'C_8')
        
    def test_add_order_9_double(self):   
        product1 = Product.objects.get(name="A_10")
        product2 = Product.objects.get(name="C_10")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'C_10')
        
    def test_add_order_10_double(self):   
        product1 = Product.objects.get(name="B_8")
        product2 = Product.objects.get(name="B_10")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        
    def test_add_order_11_double(self):   
        product1 = Product.objects.get(name="B_8")
        product2 = Product.objects.get(name="C_8")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_8')
        
    def test_add_order_12_double(self):   
        product1 = Product.objects.get(name="B_8")
        product2 = Product.objects.get(name="C_10")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_13_double(self):   
        product1 = Product.objects.get(name="B_10")
        product2 = Product.objects.get(name="C_8")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        
    def test_add_order_14_double(self):   
        product1 = Product.objects.get(name="B_10")
        product2 = Product.objects.get(name="C_10")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_10')

        
    def test_add_order_15_double(self):   
        product1 = Product.objects.get(name="C_8")
        product2 = Product.objects.get(name="C_10")
        orderproduct1 = OrderProduct(product = product1, count = 1)
        orderproduct2 = OrderProduct(product = product2, count = 1)
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_1_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_8")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        
    def test_add_order_2_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_10')
        
    def test_add_order_3_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_8")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'C_8')
        
    def test_add_order_4_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'C_10')
        
    def test_add_order_5_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        
    def test_add_order_6_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_8")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_8')
        
    def test_add_order_7_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_8_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_8")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        
    def test_add_order_9_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_10')
        
    def test_add_order_10_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_11_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        
    def test_add_order_12_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_8")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_8')
        
    def test_add_order_13_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_14_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_8")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        
    def test_add_order_15_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_10')
        
    def test_add_order_16_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct2 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_17_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_8")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        
    def test_add_order_18_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_10')
        
    def test_add_order_19_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_20_triple(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct2 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_1_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct4 = OrderProduct.objects.get(product__name = "B_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        
    def test_add_order_2_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_8")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_8')
        
    def test_add_order_3_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_4_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_8")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        
    def test_add_order_5_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_10')
        
    def test_add_order_6_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_7_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_8")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        
    def test_add_order_8_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_10')
        
    def test_add_order_9_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_10_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_11_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_8")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        
    def test_add_order_12_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_10')
        
    def test_add_order_13_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_14_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_15_four(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_1_five(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct4 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct5 = OrderProduct.objects.get(product__name = "C_8")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        order.order_products.add(orderproduct5)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        
    def test_add_order_2_five(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct4 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct5 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        order.order_products.add(orderproduct5)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_10')
        
    def test_add_order_3_five(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct5 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        order.order_products.add(orderproduct5)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_4_five(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct5 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        order.order_products.add(orderproduct5)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_5_five(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct5 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        order.order_products.add(orderproduct5)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
    
    def test_add_order_6_five(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct2 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct4 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct5 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        order.order_products.add(orderproduct5)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_six(self):
        orderproduct1 = OrderProduct.objects.get(product__name = "A_8")
        orderproduct2 = OrderProduct.objects.get(product__name = "A_10")
        orderproduct3 = OrderProduct.objects.get(product__name = "B_8")
        orderproduct4 = OrderProduct.objects.get(product__name = "B_10")
        orderproduct5 = OrderProduct.objects.get(product__name = "C_8")
        orderproduct6 = OrderProduct.objects.get(product__name = "C_10")
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        order.order_products.add(orderproduct3)
        order.order_products.add(orderproduct4)
        order.order_products.add(orderproduct5)
        order.order_products.add(orderproduct6)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        
    def test_add_order_delete_1(self):
        orderproduct = OrderProduct.objects.get(product__name = 'A_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        Order.objects.filter(order_products__product__name = 'A_8').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_8')
        self.assertEqual(order.count(), 0)
        
    def test_add_order_delete_2(self):
        orderproduct = OrderProduct.objects.get(product__name = 'A_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        Order.objects.filter(order_products__product__name = 'A_10').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_10')
        self.assertEqual(order.count(), 0)
        
    def test_add_order_delete_3(self):
        orderproduct = OrderProduct.objects.get(product__name = 'B_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_8')
        Order.objects.filter(order_products__product__name = 'B_8').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'B_8')
        self.assertEqual(order.count(), 0)
        
    def test_add_order_delete_4(self):
        orderproduct = OrderProduct.objects.get(product__name = 'B_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_10')
        Order.objects.filter(order_products__product__name = 'B_10').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'B_10')
        self.assertEqual(order.count(), 0)
        
    def test_add_order_delete_5(self):
        orderproduct = OrderProduct.objects.get(product__name = 'C_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'C_8')
        Order.objects.filter(order_products__product__name = 'C_8').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'C_8')
        self.assertEqual(order.count(), 0)
     
    def test_add_order_delete_6(self):
        orderproduct = OrderProduct.objects.get(product__name = 'C_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'C_10')
        Order.objects.filter(order_products__product__name = 'C_10').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'C_10')
        self.assertEqual(order.count(), 0)
        
    def test_add_order_delete_1_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'A_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        Order.objects.filter(order_products__product__name = 'A_8').delete()
        Order.objects.filter(order_products__product__name = 'A_10').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'A_10')
        self.assertEqual(order.count(), 0)
        
    def test_add_order_delete_2_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_8')
        Order.objects.filter(order_products__product__name = 'A_8').delete()
        Order.objects.filter(order_products__product__name = 'B_8').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'B_8')
        self.assertEqual(order.count(), 0)
        
    def test_add_order_delete_3_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_10')
        Order.objects.filter(order_products__product__name = 'A_8').delete()
        Order.objects.filter(order_products__product__name = 'B_10').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'B_10')
        self.assertEqual(order.count(), 0) 
        
    def test_add_order_delete_5_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'C_10')
        Order.objects.filter(order_products__product__name = 'A_8').delete()
        Order.objects.filter(order_products__product__name = 'C_10').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_10')
        self.assertEqual(order.count(), 0) 
        
    def test_add_order_delete_6_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        Order.objects.filter(order_products__product__name = 'A_10').delete()
        Order.objects.filter(order_products__product__name = 'B_8').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_10')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'B_8')
        self.assertEqual(order.count(), 0) 
        
    def test_add_order_delete_7_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_10')
        Order.objects.filter(order_products__product__name = 'A_10').delete()
        Order.objects.filter(order_products__product__name = 'B_10').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_10')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'B_10')
        self.assertEqual(order.count(), 0) 
        
    def test_add_order_delete_8_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'C_8')
        Order.objects.filter(order_products__product__name = 'A_10').delete()
        Order.objects.filter(order_products__product__name = 'C_8').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_10')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_8')
        self.assertEqual(order.count(), 0)
        
    def test_add_order_delete_9_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'C_10')
        Order.objects.filter(order_products__product__name = 'A_10').delete()
        Order.objects.filter(order_products__product__name = 'C_10').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_10')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_10')
        self.assertEqual(order.count(), 0)
        
    def test_add_order_delete_10_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        Order.objects.filter(order_products__product__name = 'B_8').delete()
        Order.objects.filter(order_products__product__name = 'B_10').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'B_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'B_10')
        self.assertEqual(order.count(), 0) 
        
    def test_add_order_delete_11_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_8')
        Order.objects.filter(order_products__product__name = 'B_8').delete()
        Order.objects.filter(order_products__product__name = 'C_8').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'B_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_8')
        self.assertEqual(order.count(), 0) 
        
    def test_add_order_delete_12_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_10')
        Order.objects.filter(order_products__product__name = 'B_8').delete()
        Order.objects.filter(order_products__product__name = 'C_10').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'B_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_10')
        self.assertEqual(order.count(), 0)
        
    def test_add_order_delete_13_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        Order.objects.filter(order_products__product__name = 'B_10').delete()
        Order.objects.filter(order_products__product__name = 'C_8').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'B_10')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_8')
        self.assertEqual(order.count(), 0)
        
    def test_add_order_delete_14_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_10')
        Order.objects.filter(order_products__product__name = 'B_10').delete()
        Order.objects.filter(order_products__product__name = 'C_10').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'B_10')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_10')
        self.assertEqual(order.count(), 0)
        
    def test_add_order_delete_15_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'C_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        Order.objects.filter(order_products__product__name = 'C_8').delete()
        Order.objects.filter(order_products__product__name = 'C_10').delete()
        response = self.client.get(reverse('ordering:check_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'C_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_10')
        self.assertEqual(order.count(), 0) 
    
    #編集画面のテスト
    def test_edit_price_menu_1(self):
        product = Product.objects.get(name="A_8")
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, '2')
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        
    def test_edit_price_menu_2(self):
        product = Product.objects.get(name="A_10")
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, '2')
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        
    def test_edit_price_menu_3(self):
        product = Product.objects.get(name="B_8")
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, '2')
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        
    def test_edit_price_menu_4(self):
        product = Product.objects.get(name="B_10")
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, '2')
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        
    def test_edit_price_menu_5(self):
        product = Product.objects.get(name="C_8")
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, '2')
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        
    def test_edit_price_menu_6(self):
        product = Product.objects.get(name="C_10")
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, '2')
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        
    def test_edit_name_menu_1(self):
        product = Product.objects.get(name="A_8")
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        product.name = "A_8"
        product.save()
        
    def test_edit_name_menu_2(self):
        product = Product.objects.get(name="A_10")
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        product.name = "A_10"
        product.save()
        
    def test_edit_name_menu_3(self):
        product = Product.objects.get(name="B_8")
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        product.name = "B_8"
        product.save()
        
    def test_edit_name_menu_4(self):
        product = Product.objects.get(name="B_10")
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        product.name = "B_10"
        product.save()
        
    def test_edit_name_menu_5(self):
        product = Product.objects.get(name="C_8")
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        product.name = "C_8"
        product.save()
        
    def test_edit_name_menu_6(self):
        product = Product.objects.get(name="C_10")
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        product.name = "C_10"
        product.save()
        
    def test_edit_tax_menu_1(self):
        product = Product.objects.get(name="A_8")
        product.tax = True
        product.save()
        self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        product.tax = False
        product.save()
        
    def test_edit_tax_menu_2(self):
        product = Product.objects.get(name="A_10")
        product.tax = False
        product.save()
        self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        product.tax = True
        product.save()
        
    def test_edit_tax_menu_3(self):
        product = Product.objects.get(name="B_8")
        product.tax = True
        product.save()
        self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        product.tax = False
        product.save()
        
    def test_edit_tax_menu_4(self):
        product = Product.objects.get(name="B_10")
        product.tax = False
        product.save()
        self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        product.tax = True
        product.save()
        
    def test_edit_tax_menu_5(self):
        product = Product.objects.get(name="C_8")
        product.tax = True
        product.save()
        self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        product.tax = False
        product.save()
        
    def test_edit_tax_menu_6(self):
        product = Product.objects.get(name="C_10")
        product.tax = False
        product.save()
        self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        product.tax = True
        product.save()
        
    def test_edit_category_id_menu_1(self):
        product = Product.objects.get(name="A_8")
        product.category_id = 2
        product.save()
        self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        product.category_id = 1
        product.save()
        
    def test_edit_category_id_menu_2(self):
        product = Product.objects.get(name="A_10")
        product.category_id = 2
        product.save()
        self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        product.category_id = 1
        product.save()
        
    def test_edit_category_id_menu_3(self):
        product = Product.objects.get(name="B_8")
        product.category_id = 3
        product.save()
        self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        product.category_id = 2
        product.save()
        
    def test_edit_category_id_menu_4(self):
        product = Product.objects.get(name="B_10")
        product.category_id = 3
        product.save()
        self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        product.category_id = 2
        product.save()
        
    def test_edit_category_id_menu_5(self):
        product = Product.objects.get(name="C_8")
        product.category_id = 1
        product.save()
        self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        product.category_id = 3
        product.save()
        
    def test_edit_category_id_menu_6(self):
        product = Product.objects.get(name="C_10")
        product.category_id = 1
        product.save()
        self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        product.category_id = 3
        product.save()
        
    def test_edit_name_tax_menu_1(self):
        product = Product.objects.get(name="A_8")
        product.name = "Change"
        product.tax = True
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        product.name = "A_8"
        product.tax = False
        product.save()
        
    def test_edit_name_tax_menu_2(self):
        product = Product.objects.get(name="A_10")
        product.name = "Change"
        product.tax = False
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        product.name = "A_10"
        product.tax = True
        product.save()
        
    def test_edit_name_tax_menu_3(self):
        product = Product.objects.get(name="B_8")
        product.name = "Change"
        product.tax = True
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        product.name = "B_8"
        product.tax = False
        product.save()
        
    def test_edit_name_tax_menu_4(self):
        product = Product.objects.get(name="B_10")
        product.name = "Change"
        product.tax = False
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        product.name = "B_10"
        product.tax = True
        product.save()
        
    def test_edit_name_tax_menu_5(self):
        product = Product.objects.get(name="C_8")
        product.name = "Change"
        product.tax = True
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        product.name = "C_8"
        product.tax = False
        product.save()
        
    def test_edit_name_tax_menu_6(self):
        product = Product.objects.get(name="C_10")
        product.name = "Change"
        product.tax = False
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        product.name = "C_10"
        product.tax = True
        product.save()
        
    def test_edit_name_price_menu_1(self):
        product = Product.objects.get(name="A_8")
        product.name = "Change"
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        self.assertContains(response, '2')
        product.name = "A_8"
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        
    def test_edit_name_price_menu_2(self):
        product = Product.objects.get(name="A_10")
        product.name = "Change"
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        self.assertContains(response, '2')
        product.name = "A_10"
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        
    def test_edit_name_price_menu_3(self):
        product = Product.objects.get(name="B_8")
        product.name = "Change"
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        self.assertContains(response, '2')
        product.name = "B_8"
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        
    def test_edit_name_price_menu_4(self):
        product = Product.objects.get(name="B_10")
        product.name = "Change"
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        self.assertContains(response, '2')
        product.name = "B_10"
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        
    def test_edit_name_price_menu_5(self):
        product = Product.objects.get(name="C_8")
        product.name = "Change"
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        self.assertContains(response, '2')
        product.name = "C_8"
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        
    def test_edit_name_price_menu_6(self):
        product = Product.objects.get(name="C_10")
        product.name = "Change"
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        self.assertContains(response, '2')
        product.name = "C_10"
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        
    def test_edit_name_category_id_menu_1(self):
        product = Product.objects.get(name="A_8")
        product.name = "Change"
        product.category_id = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        product.name = "A_8"
        product.category_id = 1
        product.save()
        
    def test_edit_name_category_id_menu_2(self):
        product = Product.objects.get(name="A_10")
        product.name = "Change"
        product.category_id = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)

        
    def test_edit_name_category_id_menu_3(self):
        product = Product.objects.get(name="B_8")
        product.name = "Change"
        product.category_id = 3
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)

        
    def test_edit_name_category_id_menu_4(self):
        product = Product.objects.get(name="B_10")
        product.name = "Change"
        product.category_id = 3
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        
    def test_edit_name_category_id_menu_5(self):
        product = Product.objects.get(name="C_8")
        product.name = "Change"
        product.category_id = 1
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        
    def test_edit_name_category_id_menu_6(self):
        product = Product.objects.get(name="C_10")
        product.name = "Change"
        product.category_id = 1
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, 'Change')
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        
    def test_edit_tax_price_menu_1(self):
        product = Product.objects.get(name="A_8")
        product.tax = True
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, '2')
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        
    def test_edit_tax_price_menu_2(self):
        product = Product.objects.get(name="A_10")
        product.tax = False
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, '2')
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        
    def test_edit_tax_price_menu_3(self):
        product = Product.objects.get(name="B_8")
        product.tax = True
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, '2')
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        
    def test_edit_tax_price_menu_4(self):
        product = Product.objects.get(name="B_10")
        product.tax = False
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, '2')
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        
    def test_edit_tax_price_menu_5(self):
        product = Product.objects.get(name="C_8")
        product.tax = True
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, '2')
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        
    def test_edit_tax_price_menu_6(self):
        product = Product.objects.get(name="C_10")
        product.tax = False
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        self.assertContains(response, '2')
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        
    def test_edit_tax_category_id_menu_1(self):
        product = Product.objects.get(name="A_8")
        product.tax = True
        product.category_id = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        
    def test_edit_tax_category_id_menu_2(self):
        product = Product.objects.get(name="A_10")
        product.tax = False
        product.category_id = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        
    def test_edit_tax_category_id_menu_3(self):
        product = Product.objects.get(name="B_8")
        product.tax = True
        product.category_id = 3
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        
    def test_edit_tax_category_id_menu_4(self):
        product = Product.objects.get(name="B_10")
        product.tax = False
        product.category_id = 3
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        
    def test_edit_tax_category_id_menu_5(self):
        product = Product.objects.get(name="C_8")
        product.tax = True
        product.category_id = 1
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        
    def test_edit_tax_category_id_menu_6(self):
        product = Product.objects.get(name="C_10")
        product.tax = False
        product.category_id = 1
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
  
    def test_edit_price_category_id_menu_1(self):  
        product = Product.objects.get(name="A_8")
        product.price = 2
        product.category_id = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        
    def test_edit_price_category_id_menu_2(self):  
        product = Product.objects.get(name="A_10")
        product.price = 2
        product.category_id = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        
    def test_edit_price_category_id_menu_3(self):  
        product = Product.objects.get(name="B_8")
        product.price = 2
        product.category_id = 3
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        
    def test_edit_price_category_id_menu_4(self):  
        product = Product.objects.get(name="B_10")
        product.price = 2
        product.category_id = 3
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        
    def test_edit_price_category_id_menu_5(self):  
        product = Product.objects.get(name="C_8")
        product.price = 2
        product.category_id = 1
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        
    def test_edit_price_category_id_menu_6(self):  
        product = Product.objects.get(name="C_10")
        product.price = 2
        product.category_id = 1
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        
    def test_edit_category_id_tax_price_menu_1(self): 
        product = Product.objects.get(name="A_8")
        product.category_id = 2
        product.tax = True
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1)
        
    def test_edit_category_id_tax_price_menu_2(self): 
        product = Product.objects.get(name="A_10")
        product.category_id = 2
        product.tax = False
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1)

    def test_edit_category_id_tax_price_menu_3(self): 
        product = Product.objects.get(name="B_8")
        product.category_id = 3
        product.tax = True
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1)
        
    def test_edit_category_id_tax_price_menu_4(self): 
        product = Product.objects.get(name="B_10")
        product.category_id = 3
        product.tax = False
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        
    def test_edit_category_id_tax_price_menu_5(self): 
        product = Product.objects.get(name="C_8")
        product.category_id = 1
        product.tax = True
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4)
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1)
        
    def test_edit_category_id_tax_price_menu_6(self): 
        product = Product.objects.get(name="C_10")
        product.category_id = 1
        product.tax = False
        product.price = 2
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4)
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1)  
        
    def test_edit_category_id_tax_name_menu_1(self): 
        product = Product.objects.get(name="A_8")
        product.category_id = 2
        product.tax = True
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4) 
        self.assertContains(response, 'Change')
        
    def test_edit_category_id_tax_name_menu_2(self): 
        product = Product.objects.get(name="A_10")
        product.category_id = 2
        product.tax = False
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4) 
        self.assertContains(response, 'Change') 
        
    def test_edit_category_id_tax_name_menu_3(self): 
        product = Product.objects.get(name="B_8")
        product.category_id = 3
        product.tax = True
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4) 
        self.assertContains(response, 'Change')
        
    def test_edit_category_id_tax_name_menu_4(self): 
        product = Product.objects.get(name="B_10")
        product.category_id = 3
        product.tax = False
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4) 
        self.assertContains(response, 'Change')
        
    def test_edit_category_id_tax_name_menu_5(self): 
        product = Product.objects.get(name="C_8")
        product.category_id = 1
        product.tax = True
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4) 
        self.assertContains(response, 'Change')
        
    def test_edit_category_id_tax_name_menu_6(self): 
        product = Product.objects.get(name="C_10")
        product.category_id = 1
        product.tax = False
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4) 
        self.assertContains(response, 'Change') 
        
    def test_edit_category_id_price_name_menu_1(self): 
        product = Product.objects.get(name="A_8")
        product.category_id = 2
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_category_id_price_name_menu_2(self): 
        product = Product.objects.get(name="A_10")
        product.category_id = 2
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_category_id_price_name_menu_3(self): 
        product = Product.objects.get(name="B_8")
        product.category_id = 3
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_category_id_price_name_menu_4(self): 
        product = Product.objects.get(name="B_10")
        product.category_id = 3
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_category_id_price_name_menu_5(self): 
        product = Product.objects.get(name="C_8")
        product.category_id = 1
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_category_id_price_name_menu_6(self): 
        product = Product.objects.get(name="C_10")
        product.category_id = 1
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_tax_price_name_menu_1(self): 
        product = Product.objects.get(name="A_8")
        product.tax = True
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4) 
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_tax_price_name_menu_2(self): 
        product = Product.objects.get(name="A_10")
        product.tax = False
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4) 
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_tax_price_name_menu_3(self): 
        product = Product.objects.get(name="B_8")
        product.tax = True
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4) 
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_tax_price_name_menu_4(self): 
        product = Product.objects.get(name="B_10")
        product.tax = False
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4) 
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_tax_price_name_menu_5(self): 
        product = Product.objects.get(name="C_8")
        product.tax = True
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4) 
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_tax_price_name_menu_6(self): 
        product = Product.objects.get(name="C_10")
        product.tax = False
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4) 
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_all_menu_1(self): 
        product = Product.objects.get(name="A_8")
        product.category_id = 2
        product.tax = True
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4) 
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_all_menu_2(self): 
        product = Product.objects.get(name="A_10")
        product.category_id = 2
        product.tax = False
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=1)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4) 
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_all_menu_3(self): 
        product = Product.objects.get(name="B_8")
        product.category_id = 3
        product.tax = True
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4) 
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_all_menu_4(self): 
        product = Product.objects.get(name="B_10")
        product.category_id = 3
        product.tax = False
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=2)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4) 
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_all_menu_5(self): 
        product = Product.objects.get(name="C_8")
        product.category_id = 1
        product.tax = True
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=True)
        self.assertEqual(products.count(), 4) 
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
    def test_edit_all_menu_6(self): 
        product = Product.objects.get(name="C_10")
        product.category_id = 1
        product.tax = False
        product.price = 2
        product.name = "Change"
        product.save()
        response = self.client.get(reverse('ordering:change_menu'))
        products = Product.objects.filter(category_id=3)
        self.assertEqual(products.count(), 1)
        products = Product.objects.filter(tax=False)
        self.assertEqual(products.count(), 4) 
        products = Product.objects.filter(price='2')
        self.assertEqual(products.count(), 1) 
        self.assertContains(response, 'Change')
        
        #編集画面のテスト 
    def test_modefication_1(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_8')
        orderproduct1.count = 2
        orderproduct1.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 1)
        
    def test_modefication_2(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_10')
        orderproduct1.count = 2
        orderproduct1.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 1)
        
    def test_modefication_3(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_8')
        orderproduct1.count = 2
        orderproduct1.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 1)
        
    def test_modefication_4(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_10')
        orderproduct1.count = 2
        orderproduct1.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 1)
        
    def test_modefication_5(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'C_8')
        orderproduct1.count = 2
        orderproduct1.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 1)
        
    def test_modefication_6(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'C_10')
        orderproduct1.count = 2
        orderproduct1.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 1)
        
    def test_modefication_1_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'A_10')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modefication_2_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_8')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modefication_3_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_10')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modefication_4_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_8')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modefication_5_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modefication_6_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_8')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modefication_7_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_10')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modefication_8_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_8')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modefication_9_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modefication_10_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_10')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modefication_11_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_8')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modefication_12_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modefication_13_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_8')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modefication_14_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modefication_15_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'C_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        orderproduct1.count = 2
        orderproduct2.count = 2
        orderproduct1.save()
        orderproduct2.save()
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        orderproducts = OrderProduct.objects.filter(count=2)
        self.assertEqual(orderproducts.count(), 2)
        
    def test_modification_delete_1(self):
        orderproduct = OrderProduct.objects.get(product__name = 'A_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'A_8')
        Order.objects.filter(order_products__product__name = 'A_8').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_8')
        self.assertEqual(order.count(), 0) 
        
    def test_modification_delete_2(self):
        orderproduct = OrderProduct.objects.get(product__name = 'A_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'A_10')
        Order.objects.filter(order_products__product__name = 'A_10').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_10')
        self.assertEqual(order.count(), 0)  
        
    def test_modification_delete_3(self):
        orderproduct = OrderProduct.objects.get(product__name = 'B_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'B_8')
        Order.objects.filter(order_products__product__name = 'B_8').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'B_8')
        self.assertEqual(order.count(), 0) 
        
    def test_modification_delete_4(self):
        orderproduct = OrderProduct.objects.get(product__name = 'B_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'B_10')
        Order.objects.filter(order_products__product__name = 'B_10').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'B_10')
        self.assertEqual(order.count(), 0) 
        
    def test_modification_delete_5(self):
        orderproduct = OrderProduct.objects.get(product__name = 'C_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'C_8')
        Order.objects.filter(order_products__product__name = 'C_8').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'C_8')
        self.assertEqual(order.count(), 0)  
        
    def test_modification_delete_6(self):
        orderproduct = OrderProduct.objects.get(product__name = 'C_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'C_10')
        Order.objects.filter(order_products__product__name = 'C_10').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'C_10')
        self.assertEqual(order.count(), 0)
        
    def test_modification_delete_1_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'A_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'A_10')
        Order.objects.filter(order_products__product__name = 'A_8').delete()
        Order.objects.filter(order_products__product__name = 'A_10').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'A_10')
        self.assertEqual(order.count(), 0)
        
    def test_modification_delete_2_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_8')
        Order.objects.filter(order_products__product__name = 'A_8').delete()
        Order.objects.filter(order_products__product__name = 'B_8').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'B_8')
        self.assertEqual(order.count(), 0)
        
    def test_modification_delete_3_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'B_10')
        Order.objects.filter(order_products__product__name = 'A_8').delete()
        Order.objects.filter(order_products__product__name = 'B_10').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'B_10')
        self.assertEqual(order.count(), 0) 
        
    def test_modification_delete_5_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'A_8')
        self.assertContains(response, 'C_10')
        Order.objects.filter(order_products__product__name = 'A_8').delete()
        Order.objects.filter(order_products__product__name = 'C_10').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_10')
        self.assertEqual(order.count(), 0) 
        
    def test_modification_delete_6_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_8')
        Order.objects.filter(order_products__product__name = 'A_10').delete()
        Order.objects.filter(order_products__product__name = 'B_8').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_10')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'B_8')
        self.assertEqual(order.count(), 0) 
        
    def test_modification_delete_7_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'B_10')
        Order.objects.filter(order_products__product__name = 'A_10').delete()
        Order.objects.filter(order_products__product__name = 'B_10').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_10')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'B_10')
        self.assertEqual(order.count(), 0) 
        
    def test_modification_delete_8_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'C_8')
        Order.objects.filter(order_products__product__name = 'A_10').delete()
        Order.objects.filter(order_products__product__name = 'C_8').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_10')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_8')
        self.assertEqual(order.count(), 0)
        
    def test_modification_delete_9_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'A_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'A_10')
        self.assertContains(response, 'C_10')
        Order.objects.filter(order_products__product__name = 'A_10').delete()
        Order.objects.filter(order_products__product__name = 'C_10').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'A_10')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_10')
        self.assertEqual(order.count(), 0)
        
    def test_modification_delete_10_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'B_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'B_10')
        Order.objects.filter(order_products__product__name = 'B_8').delete()
        Order.objects.filter(order_products__product__name = 'B_10').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'B_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'B_10')
        self.assertEqual(order.count(), 0) 
        
    def test_modification_delete_11_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_8')
        Order.objects.filter(order_products__product__name = 'B_8').delete()
        Order.objects.filter(order_products__product__name = 'C_8').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'B_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_8')
        self.assertEqual(order.count(), 0) 
        
    def test_modification_delete_12_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'B_8')
        self.assertContains(response, 'C_10')
        Order.objects.filter(order_products__product__name = 'B_8').delete()
        Order.objects.filter(order_products__product__name = 'C_10').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'B_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_10')
        self.assertEqual(order.count(), 0)
        
    def test_modification_delete_13_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_8')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_8')
        Order.objects.filter(order_products__product__name = 'B_10').delete()
        Order.objects.filter(order_products__product__name = 'C_8').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'B_10')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_8')
        self.assertEqual(order.count(), 0)
        
    def test_modification_delete_14_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'B_10')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'B_10')
        self.assertContains(response, 'C_10')
        Order.objects.filter(order_products__product__name = 'B_10').delete()
        Order.objects.filter(order_products__product__name = 'C_10').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'B_10')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_10')
        self.assertEqual(order.count(), 0)
        
    def test_modification_delete_15_double(self):
        orderproduct1 = OrderProduct.objects.get(product__name = 'C_8')
        orderproduct2 = OrderProduct.objects.get(product__name = 'C_10')
        order = Order.objects.get(table=1)
        order.order_products.add(orderproduct1)
        order.order_products.add(orderproduct2)
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        self.assertContains(response, 'C_8')
        self.assertContains(response, 'C_10')
        Order.objects.filter(order_products__product__name = 'C_8').delete()
        Order.objects.filter(order_products__product__name = 'C_10').delete()
        response = self.client.get(reverse('ordering:modification_order', args=[1]))
        order = Order.objects.filter(order_products__product__name = 'C_8')
        self.assertEqual(order.count(), 0)
        order = Order.objects.filter(order_products__product__name = 'C_10')
        self.assertEqual(order.count(), 0) 