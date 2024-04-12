document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.like-form').forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevents reload page

            const postId = this.dataset.postId;
            const likeIcon = document.getElementById('like-icon-' + postId);
            const likeCount = document.getElementById('like-count-' + postId);
            const formData = new FormData(this);

            fetch(this.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken'), // Enables you to make a legal request for Django
                },
            })
            .then(response => response.json())
            .then(data => {
                if(data.liked) {
                    likeIcon.classList.remove('fa-solid');
                    likeIcon.classList.add('fa-regular');
                } else {
                    likeIcon.classList.add('fa-solid');
                    likeIcon.classList.remove('fa-regular');
                }
                likeCount.textContent = data.likes_count;
            })
            .catch(error => console.error('Błąd:', error));
        });
    });
});

