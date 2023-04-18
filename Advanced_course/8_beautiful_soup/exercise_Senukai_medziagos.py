from bs4 import BeautifulSoup
import requests

html = """
document.querySelector("body > div.site > div.site-center.ct_pusht > div > div.clearfix.categories.catalog-page > div.site-content-main.products-list-full.category-content > div.catalog-taxons-products-container > div > div:nth-child(2) > div.catalog-taxons-product__hover > div.catalog-taxons-product__price > div")
<div class="catalog-taxons-product-price">
<div class="clearfix">
<div class="catalog-taxons-product-price__block">
<div class="catalog-taxons-product-price__savings-info">
<a class="catalog-taxons-product-price__savings-info-link loyalty-modal-anchor" href="#"><span class="product-price-details__savings-info-link--inactive">Su </span><span class="product-price-details__savings-info-link--active">SMART NET</span><span class="product-price-details__savings-info-link--inactive"> sutaupai:</span>
<div id="loyalty-popup-container">
<div class="loyalty-member-modal">
<div class="loyalty-member-modal__heading">
Jau esi SMART NET narys. Pasinaudok žemesnės kainos pasiūlymu.
</div>
</div>

</div>
</a><span class="catalog-taxons-product-price__savings-info-percent">-30%</span>
</div>
</div>
<div class="catalog-taxons-product-price__block">
<div class="catalog-taxons-product-price__loyalty-price">
<img class="catalog-taxons-product-price__loyalty-image" src="/assets/loyalty_programs/smartnet_icon-d4e7ec5de32c03cdc05f4735007c87a3944ae8c83eaed0067b3e74d26a04c1d5.svg">
<span class="catalog-taxons-product-price__price-number">104,30 €</span>
<span class="catalog-taxons-product-price__price-unit">/ vnt.</span>
</div>
</div>
</div>

<span class="catalog-taxons-product-price__item-price catalog-taxons-product-price__item-price--loyalty-member">
<span>149,00</span>
<span>€</span>
<span class="amount">/ vnt.</span>
</span>


</div>
"""

# Jei noriu gauti visa puslapio koda:
# source = requests.get("https://www.senukai.lt/").text
soup = BeautifulSoup(html, "html.parser")
# gaunu elementa span su klase "......" (kurioje yra man reikalingu duomenu)

price_span = soup.find(
    "span",
    class_="catalog-taxons-product-price__item-price catalog-taxons-product-price__item-price--loyalty-member",
)
print(price_span.prettify())

# price_span = soup.find("span", class_="font-bold text-textBlack text-[22px]")
# print(price_span.prettify())
# price = price_span.text.strip()
# print(price)


# print(
#     soup.html.body.div.find("div", class_="site-center ct_pusht")
# .div.div[1]
# .div[2]
# .div[2]
# .div.div[1]
# .div[1]
# .div[0]
# .div.span.span[0]

# html/body/div[1]/div[3]/div/div[2]/div[3]/div[3]/div/div[2]/div[2]/div[1]/div/span/span[1]
