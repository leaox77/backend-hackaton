# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class BrandBrand(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    logo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'brand_brand'


class CartCart(models.Model):
    id = models.BigAutoField(primary_key=True)
    total_items = models.IntegerField()
    user = models.OneToOneField('UserUseraccount', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cart_cart'


class CartCartitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    count = models.IntegerField()
    cart = models.ForeignKey(CartCart, models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cart_cartitem'


class CategoryCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_category'


class ContactsContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=254)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    contact_date = models.DateTimeField()
    city = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey('UserUseraccount', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contacts_contact'


class CouponsFixedpricecoupon(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'coupons_fixedpricecoupon'


class CouponsPercentagecoupon(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    discount_percentage = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'coupons_percentagecoupon'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserUseraccount', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OrdersOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=50)
    transaction_id = models.CharField(unique=True, max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    full_name = models.CharField(max_length=255)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state_province_region = models.CharField(max_length=255)
    postal_zip_code = models.CharField(max_length=20)
    telephone_number = models.CharField(max_length=255)
    shipping_name = models.CharField(max_length=255)
    shipping_time = models.CharField(max_length=255)
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateTimeField()
    user = models.ForeignKey('UserUseraccount', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders_order'


class OrdersOrderitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    date_added = models.DateTimeField()
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders_orderitem'


class ProductProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    compare_price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    sold = models.IntegerField()
    date_created = models.DateTimeField()
    category = models.ForeignKey(CategoryCategory, models.DO_NOTHING)
    brand = models.ForeignKey(BrandBrand, models.DO_NOTHING)
    sku = models.CharField(unique=True, max_length=100)
    pdf = models.CharField(max_length=100, blank=True, null=True)
    short_description = models.TextField()
    video_url = models.CharField(max_length=200, blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    price_mayorista_1 = models.DecimalField(max_digits=7, decimal_places=2)
    price_mayorista_2 = models.DecimalField(max_digits=7, decimal_places=2)
    price_mayorista_3 = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'product_product'


class ProductProductimage(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    uploaded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_productimage'


class QrPaymentQrpayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    user = models.ForeignKey('UserUseraccount', models.DO_NOTHING, blank=True, null=True)
    qr_code = models.CharField(max_length=100, blank=True, null=True)
    qr_code_url = models.CharField(max_length=200, blank=True, null=True)
    reference = models.CharField(max_length=255)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'qr_payment_qrpayment'


class ReviewsReview(models.Model):
    id = models.BigAutoField(primary_key=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.TextField()
    date_created = models.DateTimeField()
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    user = models.ForeignKey('UserUseraccount', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reviews_review'


class ShippingShipping(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    time_to_delivery = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'shipping_shipping'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.BooleanField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    token = models.CharField(max_length=32)
    next_step = models.SmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey('UserUseraccount', models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)


class TokenBlacklistBlacklistedtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    blacklisted_at = models.DateTimeField()
    token = models.OneToOneField('TokenBlacklistOutstandingtoken', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'token_blacklist_blacklistedtoken'


class TokenBlacklistOutstandingtoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField()
    user = models.ForeignKey('UserUseraccount', models.DO_NOTHING, blank=True, null=True)
    jti = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'token_blacklist_outstandingtoken'


class UserProfileUserprofile(models.Model):
    id = models.BigAutoField(primary_key=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state_province_region = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=20)
    phone = models.CharField(max_length=255)
    user = models.OneToOneField('UserUseraccount', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_profile_userprofile'


class UserRegisterUserRegister(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    ci = models.CharField(unique=True, max_length=20)
    foto_anverso_ci = models.CharField(max_length=100)
    foto_reverso_ci = models.CharField(max_length=100)
    numero_celular = models.CharField(max_length=20)
    correo = models.CharField(unique=True, max_length=254)
    ciudad = models.CharField(max_length=100)
    direccion = models.TextField()
    actividad_economica = models.TextField()
    fecha_registro = models.DateTimeField()
    user = models.ForeignKey('UserUseraccount', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_register_user_register'


class UserUseraccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    email = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    mayorista_tipo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_useraccount'


class UserUseraccountGroups(models.Model):
    useraccount = models.ForeignKey(UserUseraccount, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_useraccount_groups'
        unique_together = (('useraccount', 'group'),)


class UserUseraccountUserPermissions(models.Model):
    useraccount = models.ForeignKey(UserUseraccount, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_useraccount_user_permissions'
        unique_together = (('useraccount', 'permission'),)


class WishlistWishlist(models.Model):
    id = models.BigAutoField(primary_key=True)
    total_items = models.IntegerField()
    user = models.OneToOneField(UserUseraccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wishlist_wishlist'


class WishlistWishlistitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    wishlist = models.ForeignKey(WishlistWishlist, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wishlist_wishlistitem'
