from django.core.management.base import BaseCommand

from apps.settings.models import Setting

class Command(BaseCommand):
    help = "Start Bot Aiogram"

    def handle(self, *args, **options):
        print("Settings Check Django")
        if not Setting.objects.filter(title='Shopify').exists():
            Setting.objects.create(title='Shopify', description='Торговая сеть «СтройДвор.KG» – перспективная компания Кыргызстана, специализирующаяся на поставках и продаже строительных товаров и товаров хозяйственного назначения. Торговая сеть «СтройДвор.KG» была основана 1 июля 2013 года. На каждой точке у нас имеются хоз. маркеты, где вы можете приобрести отделочные материалы, такие как: отрезные круги, лакокрасочная продукция, электроды, сухие строительные смеси, инструменты и многое другое.', logo='https://stroydvor.kg/wp-content/uploads/logored.png', phone='0772343206')
            print("Settings добавлен")
        else:
            print("Settings работает")