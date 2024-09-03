$(document).ready(function() {
    $('#add-to-cart-form').submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: '{% url "add_to_cart" %}',
            data: formData,
            success: function(data) {
                $('#cart-count').text(data.cart_item_count);
            }
        });
    });
});


// search query
$(document).ready(function() {
    $('#add-to-cart-form').submit(function(event) {
        event.preventDefault();
        var formData = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: '{% url "add_to_cart" %}',
            data: formData,
            success: function(data) {
                $('#cart-count').text(data.cart_item_count);
            }
        });
    });
});

// search query
const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');
const searchResults = document.getElementById('search-results');

// assume you have a products array with title property
const products = [
  { title: 'Product 1' },
  { title: 'Product 2' },
  { title: 'Product 3' },
  // ... add more products here
];

searchForm.addEventListener('submit', (e) => {
  e.preventDefault(); // prevent form submission
  const searchTerm = searchInput.value.trim();

  const matchingProducts = products.filter((product) => {
    return product.title.toLowerCase().includes(searchTerm.toLowerCase());
  });

  if (matchingProducts.length > 0) {
    const html = matchingProducts.map((product) => {
      return `<p>${product.title}</p>`;
    }).join('');
    searchResults.innerHTML = html;
  } else {
    searchResults.innerHTML = '<p>No products found</p>';
  }
});