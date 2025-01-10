
## Endpoints

- `/admin` - админка
- `/account/` - все пользователи
- `/account/register` - регистрация пользователя
- `/account/login` - авторизация пользователя
- `/account/logout` - выход пользователя
- `/shop/` - список товаров
- `/shop/detail/<int:pk>` - информация о товаре (Product)
- `/shop/add-to-cart/<int:product_id>` - добавление товара в корзину
- `/shop/view_cart` - просмотр корзины (Cart)
- `/shop/orders` - список заказов (Orders)
- `/shop/make-order` - оформить заказ (перенести из Cart в Orders)
## Старт

```
git clone https://github.com/a-berezhkov/django_auth.git

python -m venv .venv

source .venv/bin/activate

pip install Django

cd config

python manage.py migrate

```
