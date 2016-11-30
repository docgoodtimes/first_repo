import shopify

API_KEY='bc4b61027317e6c2a92ada3dca823b09'
PASSWORD='5979043812a64cf14014e46c474bccbb'


shop_url = "https://%s:%s@officinacollective.myshopify.com/admin" % (API_KEY, PASSWORD)
shopify.ShopifyResource.set_site(shop_url)

shop = shopify.Shop.current()

for product in shopify.Product.find():
	print product.title + '\t' +product.variants[0].compare_at_price
	#+'\t' + product.tags