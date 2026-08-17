import json

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import MenuItem, Order


class MenuApiStaffAccessTests(TestCase):
    def setUp(self):
        self.staff_user = User.objects.create_user(
            username='staffapi',
            password='secret123',
            is_staff=True,
        )
        self.customer = User.objects.create_user(
            username='customerapi',
            password='secret123',
        )

    def test_staff_can_create_menu_item_via_api(self):
        self.client.login(username='staffapi', password='secret123')
        payload = {
            'cat': 'mains',
            'name': 'Beef Bowl',
            'desc': 'Grilled beef with rice',
            'price': 18000,
            'badge': 'Chef Pick',
            'emoji': '🍲',
            'img': 'https://example.com/beef.jpg',
            'is_available': True,
        }
        response = self.client.post(
            reverse('menuitem-list'),
            data=json.dumps(payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(MenuItem.objects.filter(name='Beef Bowl').exists())

    def test_customer_cannot_create_menu_item_via_api(self):
        self.client.login(username='customerapi', password='secret123')
        payload = {
            'cat': 'mains',
            'name': 'Illegal Item',
            'desc': 'Should fail',
            'price': 5000,
            'emoji': '🚫',
            'img': 'https://example.com/illegal.jpg',
        }
        response = self.client.post(
            reverse('menuitem-list'),
            data=json.dumps(payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 403)
        self.assertFalse(MenuItem.objects.filter(name='Illegal Item').exists())


class OrderStatusTrackingTests(TestCase):
    def setUp(self):
        self.staff_user = User.objects.create_user(
            username='staffuser',
            password='secret123',
            is_staff=True,
        )
        self.customer = User.objects.create_user(
            username='customer',
            password='secret123',
        )
        self.order = Order.objects.create(
            first_name='Jane',
            last_name='Doe',
            email='jane@example.com',
            phone='+256700000000',
            delivery_location='Kampala',
            date='2026-08-14',
            total_price=25000,
            status='pending',
            delivery_time='18:30:00',
        )

    def test_staff_can_update_order_status(self):
        self.client.login(username='staffuser', password='secret123')

        response = self.client.post(
            reverse('update_order_status', args=[self.order.pk]),
            {'status': 'preparing'},
        )

        self.order.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.order.status, 'preparing')

    def test_non_staff_cannot_update_order_status(self):
        self.client.login(username='customer', password='secret123')

        response = self.client.post(
            reverse('update_order_status', args=[self.order.pk]),
            {'status': 'delivered'},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.order.status, 'pending')
