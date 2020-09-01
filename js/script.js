function rate(e, star) {
    let t = $('.totalBL').text();
    if (e.classList.contains("fa-star-o") == true) {
        e.classList.remove("fa-star-o");
        e.classList.add("fa-star");
        let res = Math.round(t) + 1;
        $('.totalBL').text(res)
    }else{
        e.classList.remove("fa-star");
        e.classList.add("fa-star-o");
        let res = Math.round(t) - 11;
        $('.totalBL').text(res);
    }
}
function likeAuthor(authorId) {
    let t = Math.round($('#totalL').text());
    let res = t + 1;
    $('#totalL').text(res);
}
function followAuthor(authorId) {
    let t = Math.round($('#totalF').text());
    let res = t + 1;
    $('#totalF').text(res);
}

function sharePost(id, title, author, date) {
    $('#share-blog-title').text(title);
    $('#share-blog-author').text(author);
    $('#share-blog-date').text(date);

    let shareTo = '';
    shareTo += `<span><a href=""><i class="fa fa-facebook-square" aria-hidden="true"></i></a></span>`;
    shareTo += `<span><a href=""><i class="fa fa-whatsapp" aria-hidden="true"></i></a></span>`;
    shareTo += `<span><a href=""><i class="fa fa-instagram" aria-hidden="true"></i></a></span>`;
    shareTo += `<span><a href=""><i class="fa fa-twitter-square" aria-hidden="true"></i></a></span>`;
    $('#share-to').html(shareTo);

    $('#share-modal').show();
}

function cloSe(id) {
    $('#'+id).hide();
}