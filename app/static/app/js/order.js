
var confirmOrderComplete = document.querySelectorAll('.your-order .list-order .order__complete');

confirmOrderComplete.forEach(function(item){
    item.addEventListener('click', function(){
        loaddingElement.style.display = 'block';
        let orderId = item.dataset.order;

        fetch('/confirm-order-complete/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                'order-id': orderId
            })
        })
        .then(response => response.json())
        .then(data => {
            loaddingElement.style.display = 'none';

            if(data.success){
                window.location.reload();
            }else{
                alert(data.error);
            }
        })
        .catch(error => {
            loaddingElement.style.display = 'none';
            console.log(error);
        })
    })
})