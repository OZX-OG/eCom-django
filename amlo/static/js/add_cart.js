function getToken(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getToken('csrftoken')

function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}
let device = getToken('device')

if (device == null || device == undefined){
    device = uuidv4()
}
document.cookie ='device=' + device + ";domain=;path=/"

var user = '{{request.user}}'
var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productSlug = this.dataset.product
        updateUserOrder(productSlug)
    })
}

function updateUserOrder(productSlug) {
    var url = '/products/update_item'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({ 'productSlug': productSlug})
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            // Update the cart information on the page
            var cartCountElement = document.querySelector('.cart-count');
	        cartCountElement.innerText = data.cart_items_count;
        });
}

// Function to update the cart information on the page
function updateCartInfo(cartItemsCount) {
    // Update the cart count in the navbar
    var cartCountElement = document.querySelector('.cart-count');
	cartCountElement.innerText = cartItemsCount;
}
